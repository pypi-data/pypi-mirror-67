# -*- coding: utf-8 -*-
# ===============================================================================
# PROGRAMMERS:
#
# Florian de Boissieu <fdeboiss@gmail.com>
# https://gitlab.irstea.fr/florian.deboissieu/gdecomp
#
# Creation date: 2019-05-24
#
# This file is part of the gdecomp python package.
#
# gdecomp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#
# ===============================================================================
# Binding of Guassian Decompostion function
# Author: Florian de Boissieu <fdeboiss@gmail.com>

# Import the Python-level symbols of numpy
import numpy as np

# Import the C-level symbols of numpy
cimport numpy as np

cimport cython # to disable bounds checks
# Numpy must be initialized. When using numpy from C or Cython you must
# _always_ do that, or you will have segfaults
np.import_array()

from libcpp.vector cimport vector

cdef extern from "PulseGaussianFitting.h":
    # double GaussianFunc(double x, double amp, double cen, double wid);
    # vector[int] peaksDetectFisrtOrderZeroCrosssing(vector[double] y, double thres, int min_dist);
    # vector[vector[int]] flexion_detect(vector[double] y, vector[int] peaks);
    vector[double] GaussianFitting(vector[double] waveform, double thres, int min_dist);



# def Gaussian(double x, double amp, double cen, double wid):
#     return GaussianFunc(x, amp, cen, wid)
#
# def peaksDetection(np.ndarray[np.double_t,ndim=1] y not None, double thres, int min_dist):
#     return peaksDetectFisrtOrderZeroCrosssing(y, thres, min_dist)
#
# def gflexion(np.ndarray[np.double_t, ndim=1] y, np.ndarray[np.int_t, ndim=1] peaks):
#     return flexion_detect(y, peaks)

def GaussianDecomposition(np.ndarray[np.double_t,ndim=1] y, double thres=0.005, int min_dist=3):
    """
    Gaussian decomposition of a signal.

    Parameters
    ----------

    y : numpy.ndarray
        The signal to decompose as a sum of gaussians.

    thres : float
        threshold underwhich peak is not considered as an echo.

    min_dist : int
        minimum distance from waveform begining under which the detected peaks are not considered.

    Notes
    -----

    The Gaussian is fomulated as: amplitude / (sigma*sqrt(2*pi)) * exp(-(x-mu)^2/sigma^2).

    Returns
    -------
    numpy.ndarray
        numpy array of length 3*number_peaks of form:
        [amplitude_0, mu_0, sigma_0, amplitude_1, mu_1, sigma_1, ...]

    """
    return GaussianFitting(y, thres, min_dist)



