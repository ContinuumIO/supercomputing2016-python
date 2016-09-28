# File: util.py
# Author: William Scullin
# Date: 2015-11-28
#
# Utility functions used by all demo programs
#

"""This module contains utility functions used by pi calculating
demo programs.
"""


from sys import argv
from math import pi as const_pi
from decimal import Decimal, InvalidOperation


def output(samples=0, pi=0, start_time=0, end_time=0):
    """Print the program output"""
    perr = (abs(const_pi-pi)/const_pi)*100
    print "Pi value is %f, with error %02f%%" % (pi, perr)
    print "Run time for %s samples was %s" % (samples, end_time-start_time)


def get_sample_count(samples=1.2e7):
    """get input from argv or set default"""
    if len(argv) > 1:
        try:
            samples = int(Decimal(argv[1]))
        except (ValueError, InvalidOperation):
            return samples
    return samples
