# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2012-2020 GEM Foundation
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
import os
import re
import sys
import time
import logging
import operator
import collections.abc
from contextlib import contextmanager
import numpy
from scipy.spatial import cKDTree, distance

from openquake.baselib import hdf5, general
from openquake.baselib.python3compat import raise_
from openquake.hazardlib.geo.utils import (
    KM_TO_DEGREES, angular_distance, fix_lon, get_bounding_box, cross_idl,
    get_longitudinal_extent, BBoxError, spherical_to_cartesian)

U32 = numpy.uint32
MAX_DISTANCE = 2000  # km, ultra big distance used if there is no filter
grp_id = operator.attrgetter('grp_id')


@contextmanager
def context(src):
    """
    Used to add the source_id to the error message. To be used as

    with context(src):
        operation_with(src)

    Typically the operation is filtering a source, that can fail for
    tricky geometries.
    """
    try:
        yield
    except Exception:
        etype, err, tb = sys.exc_info()
        msg = 'An error occurred with source id=%s. Error: %s'
        msg %= (src.source_id, err)
        raise_(etype, msg, tb)


def getdefault(dic_with_default, key):
    """
    :param dic_with_default: a dictionary with a 'default' key
    :param key: a key that may be present in the dictionary or not
    :returns: the value associated to the key, or to 'default'
    """
    try:
        return dic_with_default[key]
    except KeyError:
        return dic_with_default['default']


class IntegrationDistance(collections.abc.Mapping):
    """
    Pickleable object wrapping a dictionary of integration distances per
    tectonic region type. Here is an example using 'default'
    as tectonic region type, so that the same values will be used for all
    tectonic region types:

    >>> maxdist = IntegrationDistance({'default': 400})
    >>> maxdist('Some TRT')
    400
    >>> maxdist('Some TRT', mag=2.5)
    400
    """
    def __init__(self, dic):
        self.dic = dic  # TRT -> float
        self.magdist = {}  # TRT -> (magnitudes, distances), set by the engine

    def __call__(self, trt, mag=None):
        if mag and trt in self.magdist:
            return self.magdist[trt]['%.2f' % mag]
        elif not self.dic:
            return MAX_DISTANCE
        return getdefault(self.dic, trt)

    def get_bounding_box(self, lon, lat, trt=None, mag=None):
        """
        Build a bounding box around the given lon, lat by computing the
        maximum_distance at the given tectonic region type and magnitude.

        :param lon: longitude
        :param lat: latitude
        :param trt: tectonic region type, possibly None
        :param mag: magnitude, possibly None
        :returns: min_lon, min_lat, max_lon, max_lat
        """
        if trt is None:  # take the greatest integration distance
            maxdist = max(self(trt, mag) for trt in self.dic)
        else:  # get the integration distance for the given TRT
            maxdist = self(trt, mag)
        a1 = min(maxdist * KM_TO_DEGREES, 90)
        a2 = min(angular_distance(maxdist, lat), 180)
        return lon - a2, lat - a1, lon + a2, lat + a1

    def get_affected_box(self, src):
        """
        Get the enlarged bounding box of a source.

        :param src: a source object
        :returns: a bounding box (min_lon, min_lat, max_lon, max_lat)
        """
        maxdist = self(src.tectonic_region_type)
        try:
            bbox = get_bounding_box(src, maxdist)
        except Exception as exc:
            raise exc.__class__('source %s: %s' % (src.source_id, exc))
        return (fix_lon(bbox[0]), bbox[1], fix_lon(bbox[2]), bbox[3])

    def get_dist_bins(self, trt, nbins=51):
        """
        :returns: an array of distance bins, from 10m to maxdist
        """
        return .01 + numpy.arange(nbins) * self(trt) / (nbins - 1)

    def __getstate__(self):
        # otherwise is not pickleable due to .piecewise
        return dict(dic=self.dic, magdist=self.magdist)

    def __getitem__(self, trt):
        return self(trt)

    def __iter__(self):
        return iter(self.dic)

    def __len__(self):
        return len(self.dic)

    def __toh5__(self):
        dic = {trt: numpy.array(dist) for trt, dist in self.dic.items()}
        return dic, {}

    def __fromh5__(self, dic, attrs):
        self.__init__({trt: dic[trt][()] for trt in dic})

    def __repr__(self):
        return repr(self.dic)


def split_sources(srcs):
    """
    :param srcs: sources
    :returns: a pair (split sources, split time) or just the split_sources
    """
    from openquake.hazardlib.source import splittable
    sources = []
    split_time = {}  # src.id -> time
    for src in srcs:
        if not splittable(src):
            sources.append(src)
            continue
        t0 = time.time()
        if not src.num_ruptures:  # not set yet
            src.num_ruptures = src.count_ruptures()
        mag_a, mag_b = src.get_min_max_mag()
        min_mag = src.min_mag
        if mag_b < min_mag:  # discard the source completely
            continue
        if min_mag:
            splits = []
            for s in src:
                s.min_mag = min_mag
                mag_a, mag_b = s.get_min_max_mag()
                if mag_b < min_mag:
                    continue
                s.num_ruptures = s.count_ruptures()
                if s.num_ruptures:
                    splits.append(s)
        else:
            splits = list(src)
        split_time[src.id] = time.time() - t0
        sources.extend(splits)
        has_samples = hasattr(src, 'samples')
        has_scaling_rate = hasattr(src, 'scaling_rate')
        if len(splits) > 1:
            for i, split in enumerate(splits):
                split.source_id = '%s:%s' % (src.source_id, i)
                split.grp_id = src.grp_id
                split.id = src.id
                if has_samples:
                    split.samples = src.samples
                if has_scaling_rate:
                    s.scaling_rate = src.scaling_rate
        elif splits:  # single source
            [s] = splits
            s.source_id = src.source_id
            s.grp_id = src.grp_id
            s.id = src.id
            if has_samples:
                s.samples = src.samples
            if has_scaling_rate:
                s.scaling_rate = src.scaling_rate
    return sources, split_time


class SourceFilter(object):
    """
    Filter objects have a .filter method yielding filtered sources,
    i.e. sources with an attribute .indices, containg the IDs of the sites
    within the given maximum distance. There is also a .new method
    that filters the sources in parallel and returns a dictionary
    grp_id -> filtered sources.
    Filter the sources by using `self.sitecol.within_bbox` which is
    based on numpy.
    """
    def __init__(self, sitecol, integration_distance, filename=None):
        if sitecol is not None and len(sitecol) < len(sitecol.complete):
            raise ValueError('%s is not complete!' % sitecol)
        elif sitecol is None:
            integration_distance = {}
        self.filename = filename
        self.integration_distance = (
            IntegrationDistance(integration_distance)
            if isinstance(integration_distance, dict)
            else integration_distance)
        if not filename:  # keep the sitecol in memory
            self.__dict__['sitecol'] = sitecol

    def __getstate__(self):
        if self.filename:
            # in the engine self.filename is the .hdf5 cache file
            return dict(filename=self.filename,
                        integration_distance=self.integration_distance)
        else:
            # when using calc_hazard_curves without an .hdf5 cache file
            return dict(filename=None, sitecol=self.sitecol,
                        integration_distance=self.integration_distance)

    @property
    def sitecol(self):
        """
        Read the site collection from .filename and cache it
        """
        if 'sitecol' in vars(self):
            return self.__dict__['sitecol']
        if self.filename is None:
            return
        elif not os.path.exists(self.filename):
            raise FileNotFoundError('%s: shared_dir issue?' % self.filename)
        with hdf5.File(self.filename, 'r') as h5:
            self.__dict__['sitecol'] = sc = h5.get('sitecol')
        return sc

    def get_rectangle(self, src):
        """
        :param src: a source object
        :returns: ((min_lon, min_lat), width, height), useful for plotting
        """
        min_lon, min_lat, max_lon, max_lat = (
            self.integration_distance.get_affected_box(src))
        return (min_lon, min_lat), (max_lon - min_lon) % 360, max_lat - min_lat

    def get_close_sites(self, source):
        """
        Returns the sites within the integration distance from the source,
        or None.
        """
        source_sites = list(self([source]))
        if source_sites:
            return source_sites[0][1]

    def __call__(self, sources):
        """
        :yields: pairs (src, sites)
        """
        if not self.integration_distance:  # do not filter
            for src in sources:
                yield src, self.sitecol
            return
        for src in self.filter(sources):
            yield src, self.sitecol.filtered(src.indices)

    def get_sources_sites(self, sources):
        """
        :yields:
            pairs (srcs, sites) where the sources have the same source_id,
            the same grp_ids and affect the same sites
        """
        acc = general.AccumDict(accum=[])  # indices -> srcs
        srcs, _split_time = split_sources(sources)
        for src in self.filter(srcs):
            src_id = re.sub(r':\d+$', '', src.source_id)
            acc[(src_id, src.grp_id) + tuple(src.indices)].append(src)
        for tup, srcs in acc.items():
            yield srcs, self.sitecol.filtered(tup[2:])

    # used in the disaggregation calculator
    def get_bounding_boxes(self, trt=None, mag=None):
        """
        :param trt: a tectonic region type (used for the integration distance)
        :param mag: a magnitude (used for the integration distance)
        :returns: a list of bounding boxes, one per site
        """
        bbs = []
        for site in self.sitecol:
            bb = self.integration_distance.get_bounding_box(
                site.location.longitude, site.location.latitude, trt, mag)
            bbs.append(bb)
        return bbs

    # used in the rupture prefiltering: it should not discard too much
    def close_sids(self, rec, trt):
        """
        :param rec:
           a record with fields mag, minlon, minlat, maxlon, maxlat, hypo
        :param trt:
           tectonic region type string
        :returns:
           the site indices within the maximum_distance of the hypocenter,
           plus the maximum size of the bounding box
        """
        if self.sitecol is None:
            return []
        elif not self.integration_distance:  # do not filter
            return self.sitecol.sids
        if not hasattr(self, 'kdt'):
            self.kdt = cKDTree(self.sitecol.xyz)
        xyz = spherical_to_cartesian(*rec['hypo'])
        dlon = get_longitudinal_extent(rec['minlon'], rec['maxlon'])
        dlat = rec['maxlat'] - rec['minlat']
        delta = max(dlon, dlat) / KM_TO_DEGREES
        maxradius = self.integration_distance(trt) + delta
        sids = U32(self.kdt.query_ball_point(xyz, maxradius, eps=.001))
        sids.sort()
        return sids

    # used for debugging purposes
    def get_cdist(self, rec):
        """
        :returns: array of N euclidean distances from rec['hypo']
        """
        xyz = spherical_to_cartesian(*rec['hypo']).reshape(1, 3)
        return distance.cdist(self.sitecol.xyz, xyz)[:, 0]

    def filter(self, sources):
        """
        :param sources: a sequence of sources
        :yields: sources with .indices
        """
        if self.sitecol is None:  # nofilter
            yield from sources
            return
        for src in sources:
            if hasattr(src, 'indices'):   # already filtered
                yield src
                continue
            try:
                box = self.integration_distance.get_affected_box(src)
            except BBoxError:  # too large, don't filter
                src.indices = self.sitecol.sids
                yield src
                continue
            indices = self.sitecol.within_bbox(box)
            if len(indices):
                src.indices = indices
                yield src

    def within_bbox(self, srcs):
        """
        :param srcs: a list of source objects
        :returns: the site IDs within the enlarged bounding box of the sources
        """
        if self.sitecol is None:  # for test_case_1_ruptures
            return [0]
        lons = []
        lats = []
        for src in srcs:
            try:
                box = self.integration_distance.get_affected_box(src)
            except BBoxError as exc:
                logging.error(exc)
                continue
            lons.append(box[0])
            lats.append(box[1])
            lons.append(box[2])
            lats.append(box[3])
        if cross_idl(*(list(self.sitecol.lons) + lons)):
            lons = numpy.array(lons) % 360
        else:
            lons = numpy.array(lons)
        bbox = (lons.min(), min(lats), lons.max(), max(lats))
        if bbox[2] - bbox[0] > 180:
            raise BBoxError(
                'The bounding box of the sources is larger than half '
                'the globe: %d degrees' % (bbox[2] - bbox[0]))
        return self.sitecol.within_bbox(bbox)


nofilter = SourceFilter(None, {})
