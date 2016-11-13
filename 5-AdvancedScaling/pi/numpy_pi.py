#!/usr/bin/env python2.7

# File: numpy_mpi_pi.py
# Author: William Scullin
# Date: 2015-11-28
#
# Sample program that does a serial monte carlo calculation of pi using
# NumPy functions for speed. Note that performance my strongly depend on
# your NumPy build.

import time
import numpy as np
import util


def calcpi(samples):
    """calculate Pi using numpy bcast functions"""
    np.random.seed(0)
    xy = np.random.random((samples, 2))
    pi = 4.0*np.sum(np.sum(xy**2, 1) < 1)/samples
    return pi


if __name__ == '__main__':
    samples = util.get_sample_count()

    start_time = time.time()

    pi = calcpi(samples)

    end_time = time.time()

    util.output(samples, pi, start_time, end_time)
