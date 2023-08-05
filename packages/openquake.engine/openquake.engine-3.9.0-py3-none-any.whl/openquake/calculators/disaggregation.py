# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2015-2020 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.

"""
Disaggregation calculator core functionality
"""
import logging
import operator
import numpy

from openquake.baselib import parallel, hdf5
from openquake.baselib.general import (
    AccumDict, block_splitter, get_array_nbytes, humansize)
from openquake.baselib.python3compat import encode
from openquake.hazardlib import stats
from openquake.hazardlib.calc import disagg
from openquake.hazardlib.imt import from_string
from openquake.hazardlib.gsim.base import ContextMaker, DistancesContext
from openquake.hazardlib.contexts import RuptureContext
from openquake.hazardlib.tom import PoissonTOM
from openquake.commonlib import util
from openquake.calculators import getters
from openquake.calculators import base

weight = operator.attrgetter('weight')
DISAGG_RES_FMT = '%(rlz)s%(imt)s-%(sid)s-%(poe)s/'
BIN_NAMES = 'mag', 'dist', 'lon', 'lat', 'eps', 'trt'
POE_TOO_BIG = '''\
Site #%d: you are trying to disaggregate for poe=%s.
However the source model produces at most probabilities
of %.7f for rlz=#%d, IMT=%s.
The disaggregation PoE is too big or your model is wrong,
producing too small PoEs.'''


def _check_curves(sid, rlzs, curves, imtls, poes_disagg):
    # there may be sites where the sources are too small to produce
    # an effect at the given poes_disagg
    bad = 0
    for rlz, curve in zip(rlzs, curves):
        for imt in imtls:
            max_poe = curve[imt].max()
            for poe in poes_disagg:
                if poe > max_poe:
                    logging.warning(POE_TOO_BIG, sid, poe, max_poe, rlz, imt)
                    bad += 1
    return bool(bad)


def _trt_matrix(matrices, num_trts):
    # convert a dict trti -> matrix into a single matrix of shape (T, ...)
    trti = next(iter(matrices))
    mat = numpy.zeros((num_trts,) + matrices[trti].shape)
    for trti in matrices:
        mat[trti] = matrices[trti]
    return mat


def _iml4(rlzs, iml_disagg, imtls, poes_disagg, curves):
    # an array of shape (N, M, P, Z) with intensities
    N, Z = rlzs.shape
    M = len(imtls)
    P = len(poes_disagg)
    iml4 = numpy.empty((N, M, P, Z))
    iml4.fill(numpy.nan)
    for (s, z), rlz in numpy.ndenumerate(rlzs):
        curve = curves[s][z]
        if poes_disagg == (None,):
            for m, imt in enumerate(imtls):
                iml4[s, m, 0, z] = imtls[imt]
        elif curve:
            for m, imt in enumerate(imtls):
                poes = curve[imt][::-1]
                imls = imtls[imt][::-1]
                iml4[s, m, :, z] = numpy.interp(poes_disagg, poes, imls)
    return hdf5.ArrayWrapper(
        iml4, dict(imts=[from_string(imt) for imt in imtls], rlzs=rlzs))


def compute_disagg(dstore, idxs, cmaker, iml4, trti, bin_edges, monitor):
    # see https://bugs.launchpad.net/oq-engine/+bug/1279247 for an explanation
    # of the algorithm used
    """
    :param dstore
        a DataStore instance
    :param idxs:
        an array of indices to ruptures
    :param cmaker:
        a :class:`openquake.hazardlib.gsim.base.ContextMaker` instance
    :param iml4:
        an ArrayWrapper of shape (N, M, P, Z)
    :param trti:
        tectonic region type index
    :param bin_egdes:
        a quintet (mag_edges, dist_edges, lon_edges, lat_edges, eps_edges)
    :param monitor:
        monitor of the currently running job
    :returns:
        a dictionary sid -> 8D-array
    """
    with monitor('reading rupdata', measuremem=True):
        dstore.open('r')
        oq = dstore['oqparam']
        sitecol = dstore['sitecol']
        rupdata = {k: dstore['rup/' + k][idxs] for k in dstore['rup']}
    RuptureContext.temporal_occurrence_model = PoissonTOM(
        oq.investigation_time)
    pne_mon = monitor('disaggregate_pne', measuremem=False)
    mat_mon = monitor('build_disagg_matrix', measuremem=True)
    gmf_mon = monitor('disagg mean_std', measuremem=False)
    for sid, iml3 in zip(sitecol.sids, iml4):
        singlesite = sitecol.filtered([sid])
        bins = disagg.get_bins(bin_edges, sid)
        rlzs = [iml4.rlzs[sid, z] for z in range(iml4.shape[-1])]
        ctxs = []
        ok, = numpy.where(
            rupdata['rrup_'][:, sid] <= cmaker.maximum_distance(cmaker.trt))
        for ridx in ok:  # consider only the ruptures close to the site
            rctx = RuptureContext((par, rupdata[par][ridx])
                                  for par in rupdata if not par.endswith('_'))
            dctx = DistancesContext((par[:-1], rupdata[par][ridx, [sid]])
                                    for par in rupdata if par.endswith('_'))
            ctxs.append((rctx, dctx))
        matrix = disagg.build_matrix(
            cmaker, singlesite, ctxs, iml3, iml4.imts, rlzs,
            oq.num_epsilon_bins, bins, pne_mon, mat_mon, gmf_mon)
        if matrix.any():
            yield {'trti': trti, sid: matrix}


def agg_probs(*probs):
    """
    Aggregate probabilities withe the usual formula 1 - (1 - P1) ... (1 - Pn)
    """
    acc = 1. - probs[0]
    for prob in probs[1:]:
        acc *= 1. - prob
    return 1. - acc


def get_indices(dstore, concurrent_tasks):
    acc = AccumDict(accum=[])  # grp_id -> indices
    n = 0
    grp_ids = dstore['grp_ids'][()]
    for idx, gidx in enumerate(dstore['rup/grp_id'][()]):
        n += len(grp_ids[gidx])
        for grp_id in grp_ids[gidx]:
            acc[grp_id].append(idx)
    blocksize = numpy.ceil(n / concurrent_tasks)
    indices = []
    for grp_id in dstore['full_lt'].trt_by_grp:
        blocks = list(block_splitter(acc[grp_id], blocksize))
        indices.append(blocks)
    return indices


@base.calculators.add('disaggregation')
class DisaggregationCalculator(base.HazardCalculator):
    """
    Classical PSHA disaggregation calculator
    """
    precalc = 'classical'
    accept_precalc = ['classical', 'disaggregation']

    def init(self):
        if self.N >= 32768:
            raise ValueError('You can disaggregate at max 32,768 sites')
        few = self.oqparam.max_sites_disagg
        if self.N > few:
            raise ValueError(
                'The number of sites is to disaggregate is %d, but you have '
                'max_sites_disagg=%d' % (self.N, few))
        super().init()

    def execute(self):
        """Performs the disaggregation"""
        return self.full_disaggregation()

    def get_curve(self, sid, rlzs):
        """
        Get the hazard curves for the given site ID and realizations.

        :param sid: site ID
        :param rlzs: a matrix of indices of shape Z
        :returns: a list of Z arrays of PoEs
        """
        poes = []
        for rlz in rlzs:
            pmap = self.pgetter.get(rlz)
            poes.append(pmap[sid].convert(self.oqparam.imtls)
                        if sid in pmap else None)
        return poes

    def check_poes_disagg(self, curves, rlzs):
        """
        Raise an error if the given poes_disagg are too small compared to
        the hazard curves.
        """
        oq = self.oqparam
        # there may be sites where the sources are too small to produce
        # an effect at the given poes_disagg
        ok_sites = []
        for sid in self.sitecol.sids:
            if all(curve is None for curve in curves[sid]):
                ok_sites.append(sid)
                continue
            bad = _check_curves(sid, rlzs[sid], curves[sid],
                                oq.imtls, oq.poes_disagg)
            if not bad:
                ok_sites.append(sid)
        if len(ok_sites) == 0:
            raise SystemExit('Cannot do any disaggregation')
        elif len(ok_sites) < self.N:
            logging.warning('Doing the disaggregation on' % self.sitecol)
        return ok_sites

    def full_disaggregation(self):
        """
        Run the disaggregation phase.
        """
        oq = self.oqparam
        tl = oq.truncation_level
        src_filter = self.src_filter()
        if hasattr(self, 'csm'):
            for sg in self.csm.src_groups:
                if sg.atomic:
                    raise NotImplementedError(
                        'Atomic groups are not supported yet')

        self.full_lt = self.datastore['full_lt']
        self.poes_disagg = oq.poes_disagg or (None,)
        self.imts = list(oq.imtls)

        self.ws = [rlz.weight for rlz in self.full_lt.get_realizations()]
        self.pgetter = getters.PmapGetter(
            self.datastore, self.ws, self.sitecol.sids)

        # build array rlzs (N, Z)
        if oq.rlz_index is None:
            Z = oq.num_rlzs_disagg
            rlzs = numpy.zeros((self.N, Z), int)
            if self.R > 1:
                for sid in self.sitecol.sids:
                    curves = numpy.array(
                        [pc.array for pc in self.pgetter.get_pcurves(sid)])
                    mean = getters.build_stat_curve(
                        curves, oq.imtls, stats.mean_curve, self.ws)
                    rlzs[sid] = util.closest_to_ref(curves, mean.array)[:Z]
                self.datastore['best_rlzs'] = rlzs
        else:
            Z = len(oq.rlz_index)
            rlzs = numpy.zeros((self.N, Z), int)
            for z in range(Z):
                rlzs[:, z] = oq.rlz_index[z]
        assert Z <= self.R, (Z, self.R)
        self.Z = Z
        self.rlzs = rlzs

        if oq.iml_disagg:
            # no hazard curves are needed
            self.poe_id = {None: 0}
            curves = [[None for z in range(Z)] for s in range(self.N)]
            self.ok_sites = set(self.sitecol.sids)
        else:
            self.poe_id = {poe: i for i, poe in enumerate(oq.poes_disagg)}
            curves = [self.get_curve(sid, rlzs[sid])
                      for sid in self.sitecol.sids]
            self.ok_sites = set(self.check_poes_disagg(curves, rlzs))
        self.iml4 = _iml4(rlzs, oq.iml_disagg, oq.imtls,
                          self.poes_disagg, curves)
        if oq.disagg_by_src:
            self.build_disagg_by_src(rlzs)

        eps_edges = numpy.linspace(-tl, tl, oq.num_epsilon_bins + 1)

        # build trt_edges
        trts = tuple(self.full_lt.trts)
        trt_num = {trt: i for i, trt in enumerate(trts)}
        self.trts = trts

        # build mag_edges
        mags = set()
        for trt, dset in self.datastore['source_mags'].items():
            mags.update(float(mag) for mag in dset[()])
        mags = sorted(mags)
        mag_edges = oq.mag_bin_width * numpy.arange(
            int(numpy.floor(min(mags) / oq.mag_bin_width)),
            int(numpy.ceil(max(mags) / oq.mag_bin_width) + 1))

        # build dist_edges
        maxdist = max(oq.maximum_distance(trt) for trt in trts)
        dist_edges = oq.distance_bin_width * numpy.arange(
            0, int(numpy.ceil(maxdist / oq.distance_bin_width) + 1))

        # build eps_edges
        eps_edges = numpy.linspace(-tl, tl, oq.num_epsilon_bins + 1)

        # build lon_edges, lat_edges per sid
        bbs = src_filter.get_bounding_boxes(mag=max(mags))
        lon_edges, lat_edges = {}, {}  # by sid
        for sid, bb in zip(self.sitecol.sids, bbs):
            lon_edges[sid], lat_edges[sid] = disagg.lon_lat_bins(
                bb, oq.coordinate_bin_width)
        self.bin_edges = mag_edges, dist_edges, lon_edges, lat_edges, eps_edges
        shapedic = self.save_bin_edges()
        del shapedic['trt']
        shapedic['N'] = self.N
        shapedic['M'] = len(oq.imtls)
        shapedic['P'] = len(oq.poes_disagg)
        shapedic['Z'] = Z
        shapedic['concurrent_tasks'] = oq.concurrent_tasks
        nbytes, msg = get_array_nbytes(shapedic)
        if nbytes > oq.max_data_transfer:
            raise ValueError(
                'Estimated data transfer too big\n%s > max_data_transfer=%s' %
                (msg, humansize(oq.max_data_transfer)))
        logging.info('Estimated data transfer: %s', msg)
        self.imldict = {}  # sid, rlz, poe, imt -> iml
        for s in self.sitecol.sids:
            for z, rlz in enumerate(rlzs[s]):
                for p, poe in enumerate(self.poes_disagg):
                    for m, imt in enumerate(oq.imtls):
                        self.imldict[s, rlz, poe, imt] = self.iml4[s, m, p, z]

        # submit #groups disaggregation tasks
        dstore = (self.datastore.parent if self.datastore.parent
                  else self.datastore)
        indices = get_indices(dstore, oq.concurrent_tasks or 1)
        self.datastore.swmr_on()
        smap = parallel.Starmap(compute_disagg, h5=self.datastore.hdf5)
        for grp_id, trt in self.full_lt.trt_by_grp.items():
            logging.info('Group #%d, sending rup_data for %s', grp_id, trt)
            trti = trt_num[trt]
            cmaker = ContextMaker(
                trt, self.full_lt.get_rlzs_by_gsim(grp_id),
                {'truncation_level': oq.truncation_level,
                 'maximum_distance': src_filter.integration_distance,
                 'filter_distance': oq.filter_distance, 'imtls': oq.imtls})
            for idxs in indices[grp_id]:
                smap.submit((dstore, idxs, cmaker, self.iml4, trti,
                             self.bin_edges))
        results = smap.reduce(self.agg_result, AccumDict(accum={}))
        return results  # sid -> trti-> 8D array

    def agg_result(self, acc, result):
        """
        Collect the results coming from compute_disagg into self.results.

        :param acc: dictionary sid -> trti -> 8D array
        :param result: dictionary with the result coming from a task
        """
        with self.monitor('aggregating disagg matrices'):
            trti = result.pop('trti')
            for sid, arr in result.items():
                acc[sid][trti] = agg_probs(acc[sid].get(trti, 0), arr)
        return acc

    def save_bin_edges(self):
        """
        Save disagg-bins
        """
        b = self.bin_edges
        T = len(self.trts)
        for sid in self.sitecol.sids:
            bins = disagg.get_bins(b, sid)
            shape = [len(bin) - 1 for bin in bins] + [T]
            shape_dic = dict(zip(BIN_NAMES, shape))
            if sid == 0:
                logging.info('nbins=%s for site=#%d', shape_dic, sid)
            matrix_size = numpy.prod(shape)  # 6D
            if matrix_size > 1E6:
                raise ValueError(
                    'The disaggregation matrix for site #%d is too large '
                    '(%d elements): fix the binning!' % (sid, matrix_size))
        self.datastore['disagg-bins/mags'] = b[0]
        self.datastore['disagg-bins/dists'] = b[1]
        for sid in self.sitecol.sids:
            self.datastore['disagg-bins/lons/sid-%d' % sid] = b[2][sid]
            self.datastore['disagg-bins/lats/sid-%d' % sid] = b[3][sid]
        self.datastore['disagg-bins/eps'] = b[4]
        return shape_dic

    def post_execute(self, results):
        """
        Save all the results of the disaggregation. NB: the number of results
        to save is #sites * #rlzs * #disagg_poes * #IMTs.

        :param results:
            a dictionary sid -> trti -> disagg matrix
        """
        T = len(self.trts)
        # build a dictionary sid -> 9D matrix of shape (T, ..., E, M, P)
        results = {sid: _trt_matrix(dic, T) for sid, dic in results.items()}

        # get the number of outputs
        shp = (self.N, len(self.poes_disagg), len(self.imts), self.Z)
        logging.info('Extracting and saving the PMFs for %d outputs '
                     '(N=%s, P=%d, M=%d, Z=%d)', numpy.prod(shp), *shp)
        self.save_disagg_results(results, trts=encode(self.trts))

    def save_disagg_results(self, results, **attrs):
        """
        Save the computed PMFs in the datastore

        :param results:
            an 8D-matrix of shape (T, .., E, M, P)
        :param attrs:
            dictionary of attributes to add to the dataset
        """
        for sid, mat9 in results.items():
            rlzs = self.rlzs[sid]
            many_rlzs = len(rlzs) > 1
            for m, imt in enumerate(self.imts):
                if many_rlzs:  # rescale the weights
                    weights = numpy.array([self.ws[r][imt] for r in rlzs])
                    weights /= weights.sum()  # normalize to 1
                for p, poe in enumerate(self.poes_disagg):
                    mat7 = mat9[..., m, p, :]
                    for z in range(self.Z):
                        mat6 = mat7[..., z]
                        if mat6.any():  # nonzero
                            self._save('disagg', sid, rlzs[z], poe, imt, mat6)
                    if many_rlzs:  # compute the mean matrices
                        mean = numpy.average(mat7, -1, weights)
                        if mean.any():  # nonzero
                            self._save('disagg', sid, 'mean', poe, imt, mean)
        self.datastore.set_attrs('disagg', **attrs)

    def _save(self, dskey, site_id, rlz_id, poe, imt_str, matrix6):
        disagg_outputs = self.oqparam.disagg_outputs
        lon = self.sitecol.lons[site_id]
        lat = self.sitecol.lats[site_id]
        try:
            rlz = 'rlz-%d-' % rlz_id
        except TypeError:  # for the mean
            rlz = ''
        disp_name = dskey + '/' + DISAGG_RES_FMT % dict(
            rlz=rlz, imt=imt_str, sid='sid-%d' % site_id,
            poe='poe-%d' % self.poe_id[poe])
        mag, dist, lonsd, latsd, eps = self.bin_edges
        lons, lats = lonsd[site_id], latsd[site_id]
        with self.monitor('extracting PMFs'):
            poe_agg = []
            aggmatrix = agg_probs(*matrix6)
            for key, fn in disagg.pmf_map.items():
                if not disagg_outputs or key in disagg_outputs:
                    pmf = fn(matrix6 if key.endswith('TRT') else aggmatrix)
                    self.datastore[disp_name + key] = pmf
                    poe_agg.append(1. - numpy.prod(1. - pmf))

        attrs = self.datastore.hdf5[disp_name].attrs
        attrs['site_id'] = site_id
        attrs['rlzi'] = rlz_id
        attrs['imt'] = imt_str
        try:
            attrs['iml'] = self.imldict[site_id, rlz_id, poe, imt_str]
        except KeyError:  # for the mean
            pass
        attrs['mag_bin_edges'] = mag
        attrs['dist_bin_edges'] = dist
        attrs['lon_bin_edges'] = lons
        attrs['lat_bin_edges'] = lats
        attrs['eps_bin_edges'] = eps
        attrs['trt_bin_edges'] = self.trts
        attrs['location'] = (lon, lat)
        # sanity check: all poe_agg should be the same
        attrs['poe_agg'] = poe_agg
        if poe and site_id in self.ok_sites:
            attrs['poe'] = poe
            poe_agg = numpy.mean(attrs['poe_agg'])
            if abs(1 - poe_agg / poe) > .1:
                logging.warning(
                    'Site #%d: poe_agg=%s is quite different from the expected'
                    ' poe=%s; perhaps the number of intensity measure'
                    ' levels is too small?', site_id, poe_agg, poe)

    def build_disagg_by_src(self, rlzs):
        logging.warning('Disaggregation by source is experimental')
        oq = self.oqparam
        groups = list(self.full_lt.get_rlzs_by_grp())
        M = len(oq.imtls)
        P = len(self.poes_disagg)
        for (s, z), rlz in numpy.ndenumerate(rlzs):
            poes = numpy.zeros((M, P, len(groups)))
            iml2 = self.iml4[s, :, :, z]
            rlz = rlzs[s, z]
            for g, grp_id in enumerate(groups):
                pcurve = self.pgetter.get_pcurve(s, rlz, int(grp_id[4:]))
                if pcurve is None:
                    continue
                for m, imt in enumerate(oq.imtls):
                    xs = oq.imtls[imt]
                    ys = pcurve.array[oq.imtls(imt), 0]
                    poes[m, :, g] = numpy.interp(iml2[m], xs, ys)
            for m, imt in enumerate(oq.imtls):
                for p, poe in enumerate(self.poes_disagg):
                    pref = ('iml-%s' % oq.iml_disagg[imt] if poe is None
                            else 'poe-%s' % poe)
                    name = 'disagg_by_src/%s-%s-sid-%s' % (pref, imt, s)
                    if poes[m, p].sum():  # nonzero contribution
                        poe_agg = 1 - numpy.prod(1 - poes[m, p])
                        if poe and abs(1 - poe_agg / poe) > .1:
                            logging.warning(
                                'poe_agg=%s is quite different from '
                                'the expected poe=%s', poe_agg, poe)
                        self.datastore[name] = poes[m, p]
                        self.datastore.set_attrs(name, poe_agg=poe_agg)
