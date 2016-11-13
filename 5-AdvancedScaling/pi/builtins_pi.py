#!/usr/bin/env python2.7

# File: builtins_pi.py
# Author: William Scullin
# Date: 2015-11-28
#
# Sample program that does a serial monte carlo calculation of pi using only
# functions from the standard library.

import random
import time
import util


def calcpi(nsamples):
    """serially calculate Pi using only standard library functions"""
    inside = 0
    random.seed(0)
    for i in range(int(samples)):
        x = random.random()
        y = random.random()
        if (x*x)+(y*y) < 1:
            inside += 1
    return (4.0 * inside)/samples

if __name__ == '__main__':
    samples = util.get_sample_count()

    start_time = time.time()

    pi = calcpi(samples)

    end_time = time.time()

    util.output(samples, pi, start_time, end_time)
