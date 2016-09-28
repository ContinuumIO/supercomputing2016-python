#!/usr/bin/env python
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
mpisize = comm.Get_size()

def output(var,nomen,rank,method=None,operation=None):
    if method==None and operation==None:
        print "Rank %d sees %s as %s" %(rank,nomen,var)
    else:
        print "Rank %d sees %s as %s after %s using %s" %(rank,nomen,var,method,operation)
        

if rank == 0:
    local_dict={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':'gee whiz', 'h':('hi', 'there') }
    local_list_max=[rank+i for i in range(mpisize/2)]
    local_list_sum=[rank+i for i in range(mpisize/2)]
    local_string="""This is a string."""
    local_tuple=(rank,)*mpisize
    local_np_array=np.array(range(10))
else:
    local_dict=None
    local_list_max=[rank*i for i in range(mpisize/2)]
    local_list_sum=[rank*i for i in range(mpisize/2)]
    local_string="""This should be fun!"""
    local_tuple=(rank,)*mpisize
    local_np_array=np.array(range(10))

comm.Barrier()

if rank == 0:
    print "#"*78
    output(local_dict,'local_dict',rank)
    output(local_list_max,'local_list_max',rank)
    output(local_list_sum,'local_list_sum',rank)
    output(local_string,'local_string',rank)
    output(local_tuple,'local_tuple',rank)
    output(local_np_array,'local_np_array',rank)

comm.Barrier()

if rank == 6:
    print "#"*78
    output(local_dict,'local_dict',rank)
    output(local_list_max,'local_list_max',rank)
    output(local_list_sum,'local_list_sum',rank)
    output(local_string,'local_string',rank)
    output(local_tuple,'local_tuple',rank)
    output(local_np_array,'local_np_array',rank)

comm.Barrier()

if rank == 0:
    print "#"*78
    print ""
    print "Running collective operations"
    print ""

comm.Barrier()

local_dict = comm.scatter(local_dict)
local_list_max = comm.allreduce(local_list_max,op=MPI.MAX)
local_list_sum = comm.allreduce(local_list_sum,op=MPI.SUM)
local_string = comm.bcast(local_string)
local_tuple = comm.alltoall(local_tuple)
local_np_array = comm.allreduce(local_np_array,op=MPI.SUM)

comm.Barrier()
if rank == 0:
    print "#"*78
    output(local_dict,'local_dict',rank)
    output(local_list_max,'local_list_max',rank,'allreduce','max')
    output(local_list_sum,'local_list_sum',rank,'allreduce','sum')
    output(local_string,'local_string',rank,'bcast')
    output(local_tuple,'local_tuple',rank,'alltoall')
    output(local_np_array,'local_np_array',rank,'allreduce')

comm.Barrier()
if rank == 6:
    print "#"*78
    output(local_dict,'local_dict',rank)
    output(local_list_max,'local_list_max',rank,'allreduce','max')
    output(local_list_sum,'local_list_sum',rank,'allreduce','sum')
    output(local_string,'local_string',rank,'bcast')
    output(local_tuple,'local_tuple',rank,'alltoall')
    output(local_np_array,'local_np_array',rank,'allreduce')