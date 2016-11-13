#!/usr/bin/env python2.7

# File: builtins_pi.py
# Author: William Scullin
# Date: 2015-11-28
#
# Sample program that does a serial monte carlo calculation of pi using only
# functions from the standard library.

from threading import Thread, Lock
import thread
import random
import time
import util
import sys


def calcpi_threads(samples, thread_count=4):
    global inside
    inside = 0

    global lock
    lock = Lock()

    nsamples = int(samples/thread_count)

    threads = [Thread(target=calcpi, args=(nsamples, ), name=i) for i in range(thread_count)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return (4.0 * inside)/samples

def calcpi(nsamples):
    """calculate Pi using threads and standard library functions"""
     
    global inside
    global lock

    # set seed per-thread
    random.seed(thread.get_ident())
    
    # use a local variable to avoid locking
    # the variable inside until we have a final result
    local_inside = 0

    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2)+(y**2) < 1:
            local_inside += 1

    # The GIL doesn't always save you, each thread
    # acquires and releases a lock on the global
    # inside to avoid collisions
    lock.acquire()
    inside += local_inside
    lock.release()


if __name__ == '__main__':
    samples = util.get_sample_count()

    thread_count = 4

    if int(sys.argv[-1]) != samples:
	if int(sys.argv[-1]) >= 4 and int(sys.argv[-1]) <= 64:
	    thread_count=int(sys.argv[-1])

    start_time = time.time()

    pi = calcpi_threads(samples, thread_count)

    end_time = time.time()

    util.output(samples, pi, start_time, end_time)
