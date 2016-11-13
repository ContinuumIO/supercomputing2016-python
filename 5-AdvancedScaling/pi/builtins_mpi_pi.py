#!/usr/bin/env python2.7

# File: builtins_mpi_pi.py
# Author: William Scullin
# Date: 2015-11-28
#
# Sample program that does a parallel monte carlo calculation of pi using MPI
# and standard library functions. NumPy is only invoked to create mutable
# buffers for mpi4py to read and write to/from.

from mpi4py import MPI
import numpy as np
import random
import util


def calcpi(samples):
    """calculate Pi in parallel using standard library functions"""
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    mpisize = comm.Get_size()

    # we need this to have a muteable buffer for mpi4py
    # to write into so we don't need to serialize data
    pi = np.zeros(1)


    nsamples = int(samples/mpisize)
    inside = 0
    random.seed(rank)
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x*x)+(y*y) < 1:
            inside += 1
    mypi = (4.0*inside)/nsamples

    # capital Reduce works with C/NumPy compatible data
    # -types and avoids the need to serialize data at 
    # transmission and receipt. Lowercase reduce would
    # work on Python objects.
    #
    # The value of mypi will be summed into pi on rank 0
    comm.Reduce(np.array(mypi), pi, op=MPI.SUM, root=0)
    return pi/mpisize

if __name__ == '__main__':
    samples = util.get_sample_count()

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    start_time = MPI.Wtime()

    pi = calcpi(samples)

    end_time = MPI.Wtime()

    if rank == 0:
        util.output(samples, pi, start_time, end_time)
