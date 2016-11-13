#!/usr/bin/env python2.7

# File: numba_pi.py
# Author: William Scullin
# Date: 2015-11-28
#
# Sample program that does a serial monte carlo calculation of pi using
# standard library functions, but invokes the Numba JIT to speed calculation.


import random
import time
from numba import jit
import util


@jit
def calcpi(nsamples):
    """carry out Pi calculations in serial using Numba jit"""
    random.seed(0)
    inside = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()

        if (x*x)+(y*y) < 1:
            inside += 1
    return (4.0 * inside)/nsamples

if __name__ == '__main__':
    samples = util.get_sample_count()
    start_time = time.time()

    pi = calcpi(samples)

    end_time = time.time()

    util.output(samples, pi, start_time, end_time)
