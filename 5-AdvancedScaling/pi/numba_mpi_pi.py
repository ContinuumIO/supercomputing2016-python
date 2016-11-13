#!/usr/bin/env python2.7

# File: numba_mpi_pi.py
# Author: William Scullin
# Date: 2015-11-28
#
# Sample program that does a parallel monte carlo calculation of pi using MPI
# and standard library functions, but invokes the Numba JIT to speed
# calculation. NumPy is only invoked to create mutable buffers for mpi4py to
# read and write into.

from mpi4py import MPI
import numpy as np
import random
from numba import jit
import util


@jit
def calcpi(nsamples):
    """calculate Pi using Numba jit"""
    inside = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()

        if (x*x)+(y*y) < 1:
            inside += 1

    return (4.0 * inside)/nsamples


@jit
def calcpi_mpi(samples):
    """carry out Pi calculations in parallel using MPI"""

    # Needed to provide mpi4py a writable buffer
    pi = np.zeros(1)

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    mpisize = comm.Get_size()

    nsamples = int(samples/mpisize)
    random.seed(rank)
    mypi = np.array(calcpi(nsamples))

    comm.Reduce(mypi, pi, op=MPI.SUM, root=0)
    return pi/mpisize


if __name__ == '__main__':
    samples = util.get_sample_count()

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    start_time = MPI.Wtime()

    pi = calcpi_mpi(samples)

    end_time = MPI.Wtime()

    if rank == 0:
        util.output(samples, pi, start_time, end_time)
