# This file is part of atooms
# Copyright 2010-2018, Daniele Coslovich

"""Radial distribution function."""

import math

import numpy

from .helpers import linear_grid
from .correlation import Correlation
from .progress import progress

__all__ = ['RadialDistributionFunction',
           'RadialDistributionFunctionLegacy',
           'RadialDistributionFunctionFast']


def gr_kernel(x, y, L, *args):
    # Precalculating 1/L does not improve timings
    # r is an array of array distances
    r = x-y
    r = r - numpy.rint(r/L) * L
    return numpy.sqrt(numpy.sum(r**2, axis=1))


def gr_kernel_square(x, y, L, *args):
    """Return square distances."""
    # r is an array of array distances
    r = x-y
    r = r - numpy.rint(r/L) * L
    return numpy.sum(r**2, axis=1)

def pairs_newton_hist(f, x, y, L, bins):
    """
    Apply function f to all pairs in x[i] and y[j] and update the
    |hist| histogram using the |bins| bin edges.
    """
    hist, bins = numpy.histogram([], bins)
    # Do the calculation in batches to optimize
    bl = max(1, int(1e5 / len(y)))
    for ib in range(0, len(y)-1, bl):
        fxy = []
        # batch must never exceed len(y)-1
        for i in range(ib, min(ib+bl, len(y)-1)):
            for value in f(x[i+1:], y[i], L):
                fxy.append(value)
        hist_tmp, bins = numpy.histogram(fxy, bins)
        hist += hist_tmp
    return hist


def pairs_hist(f, x, y, L, bins):
    """
    Apply function f to all pairs in x[i] and y[j] and update the
    |hist| histogram using the |bins| bin edges.
    """
    hist, bins = numpy.histogram([], bins)
    for i in range(len(y)):
        fxy = f(x[:], y[i], L)
        hist_tmp, bins = numpy.histogram(fxy, bins)
        hist += hist_tmp
    return hist


class RadialDistributionFunctionLegacy(Correlation):
    """
    Radial distribution function.

    The correlation function g(r) is computed over a grid of distances
    `rgrid`. If the latter is `None`, the grid is linear from 0 to L/2
    with a spacing of `dr`. Here, L is the side of the simulation cell
    along the x axis at the first step.

    Additional parameters:
    ----------------------

    - norigins: controls the number of trajectory frames to compute
      the time average
    """

    nbodies = 2
    symbol = 'gr'
    short_name = 'g(r)'
    long_name = 'radial distribution function'
    phasespace = 'pos'

    def __init__(self, trajectory, rgrid=None, norigins=None, dr=0.04, ndim=-1):
        Correlation.__init__(self, trajectory, rgrid, norigins=norigins)
        self._side = self.trajectory.read(0).cell.side
        if ndim > 0:
            # Only the first ndim coordinates are retained
            self._ndim = ndim
            self._volume = self._side[:ndim].prod()
        else:
            self._ndim = len(self._side)
            self._volume = self._side.prod()
        if rgrid is not None:
            # Reconstruct bounds of grid for numpy histogram
            self.grid = []
            for i in range(len(rgrid)):
                self.grid.append(rgrid[i] - (rgrid[1] - rgrid[0]) / 2)
            self.grid.append(rgrid[-1] + (rgrid[1] - rgrid[0]) / 2)
        else:
            L = min(self._side)
            self.grid = linear_grid(0.0, L / 2.0, dr)

    def _compute(self):
        ncfg = len(self.trajectory)
        # Assume grandcanonical trajectory for generality.
        # Note that testing if the trajectory is grandcanonical or
        # semigrandcanonical is useless when applying filters.  
        # N_0, N_1 = len(self._pos_0[0]), len(self._pos_1[0])
        N_0 = numpy.average([len(x) for x in self._pos_0])
        N_1 = numpy.average([len(x) for x in self._pos_1])

        gr_all = []
        _, r = numpy.histogram([], bins=self.grid)
        origins = range(0, ncfg, self.skip)
        for i in progress(origins):
            self._side = self.trajectory.read(i).cell.side
            if len(self._pos_0[i]) == 0 or len(self._pos_1[i]) == 0:
                continue
            if self._pos_0 is self._pos_1:
                gr = pairs_newton_hist(gr_kernel, self._pos_0[i], self._pos_1[i],
                                       self._side, r)
            else:
                gr = pairs_hist(gr_kernel, self._pos_0[i], self._pos_1[i],
                                self._side, r)
            gr_all.append(gr)

        # Normalization
        if self._ndim == 2:
            vol = math.pi * (r[1:]**2 - r[:-1]**2)
        elif self._ndim == 3:
            vol = 4 * math.pi / 3.0 * (r[1:]**3 - r[:-1]**3)
        else:
            from math import gamma
            n2 = int(float(self._ndim) / 2)
            vol = math.pi**n2 * (r[1:]**self._ndim-r[:-1]**self._ndim) / gamma(n2+1)
        rho = N_1 / self._volume
        if self._pos_0 is self._pos_1:
            norm = rho * vol * N_0 * 0.5  # use Newton III
        else:
            norm = rho * vol * N_0
        gr = numpy.average(gr_all, axis=0)
        self.grid = (r[:-1] + r[1:]) / 2.0
        self.value = gr / norm


class RadialDistributionFunctionFast(RadialDistributionFunctionLegacy):
    """
    Radial distribution function using f90 kernel.

    The correlation function g(r) is computed over a grid of distances
    `rgrid`. If the latter is `None`, the grid is linear from 0 to L/2
    with a spacing of `dr`. Here, L is the side of the simulation cell
    along the x axis at the first step.

    Additional parameters:
    ----------------------

    - norigins: controls the number of trajectory frames to compute
      the time average
    """

    def _compute(self):
        from atooms.postprocessing.realspace_wrap import compute

        ncfg = len(self.trajectory)
        # Assume grandcanonical trajectory for generality.
        # Note that testing if the trajectory is grandcanonical or
        # semigrandcanonical is useless when applying filters.  
        N_0, N_1 = [], []
        gr_all = []
        _, bins = numpy.histogram([], bins=self.grid)
        origins = range(0, ncfg, self.skip)
        for i in progress(origins):
            self._side = self.trajectory.read(i).cell.side
            if len(self._pos_0[i]) == 0 or len(self._pos_1[i]) == 0:
                continue
            hist, bins = numpy.histogram([], bins)
            if self._pos_0 is self._pos_1:
                x = self._pos_0[i].transpose()
                idx = numpy.array(range(1, x.shape[1]+1))
                N_0.append(len(idx))
                N_1.append(x.shape[1])
                distances = numpy.ndarray(len(idx)*x.shape[1])
                k = compute.gr_self(idx, x, self._side, self._side/2, distances)
                gr, bins = numpy.histogram(distances[:k], bins)                
            else:
                x = self._pos_0[i].transpose()
                y = self._pos_1[i].transpose()
                idx = numpy.array(range(1, x.shape[1]+1))
                N_0.append(len(idx))
                N_1.append(y.shape[1])
                distances = numpy.ndarray(len(idx)*y.shape[1])
                k = compute.gr_distinct(idx, x, y, self._side, self._side/2, distances)
                gr, bins = numpy.histogram(distances[:k], bins)

            gr_all.append(gr)

        # Normalization
        r = bins
        N_0 = numpy.average(N_0)
        N_1 = numpy.average(N_1)
        if self._ndim == 2:
            vol = math.pi * (r[1:]**2 - r[:-1]**2)
        elif self._ndim == 3:
            vol = 4 * math.pi / 3.0 * (r[1:]**3 - r[:-1]**3)
        else:
            from math import gamma
            n2 = int(float(self._ndim) / 2)
            vol = math.pi**n2 * (r[1:]**self._ndim-r[:-1]**self._ndim) / gamma(n2+1)
        rho = N_1 / self._volume
        if self._pos_0 is self._pos_1:
            norm = rho * vol * N_0 * 0.5  # use Newton III
        else:
            norm = rho * vol * N_0
        gr = numpy.average(gr_all, axis=0)
        self.grid = (r[:-1] + r[1:]) / 2.0
        self.value = gr / norm

# Defaults to fast 
RadialDistributionFunction = RadialDistributionFunctionFast
