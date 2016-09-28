#!/usr/bin/env python2.7

# File: numpy_mpi_pi.py
# Author: William Scullin
# Date: 2015-11-28
#
# Sample program that does a parallel monte carlo calculation of pi using MPI
# and NumPy functions for speed. Note that performance my strongly depend on
# your NumPy build and MPI implementation.

from mpi4py import MPI
import numpy as np
import util


def calcpi(samples):
    """calculate Pi using numpy and mpi"""
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    mpisize = comm.Get_size()
    nsamples = int(samples/mpisize)
    pi = np.zeros(1)

    np.random.seed(rank)
    xy = np.random.random((nsamples, 2))
    mypi = np.array(4.0*np.sum(np.sum(xy**2, 1) < 1)/nsamples)

    comm.Reduce(mypi, pi, op=MPI.SUM, root=0)
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
