
from numpy.random import randint
from scipy.stats.mstats import chisquare
from collections import defaultdict

import scipy as sp
import pylab as py

import bz2

piseq = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

zeros = "0"*100

cheat = "0123456789"*10

rand1 = randint(0,10,100)
rand2 = randint(0,10,100)

def to_string(guys):
    return "".join(str(d) for d in guys)

def to_ints(guys):
    return (int(d) for d in guys)

def count_digs(guys):
    foo = (int(d) for d in guys)
    counts = defaultdict(int)
    for item in foo:
        counts[item] += 1
    return [ counts[i] for i in range(10)] 

def test_chisquare(guys):
    """ Get the chi-square p value of the stream """
    counts = count_digs(guys)
    stat, p = chisquare(counts)
    return p
    
def test_bz2(guys):
    """ Look at the bz2 compression ratio """
    tot = len(guys)
    short = len(bz2.compress("0"*tot))
    c_length = len(bz2.compress(to_string(guys)))
    
    return (c_length-short)/float(tot-short)

    
def test_shannon(guys):
    tot = float(len(guys))
    counts = count_digs(guys)

    entropy = sum( -count/tot*sp.log2(count/tot + 10**(-10)) for count in counts )

    return entropy/sp.log2(10)


if __name__ == "__main__":    
    from inspect import getmembers
    currentdir = dir()
    alltests = [guy for name,guy in getmembers(__file__) if name.startswith('test_') ]

    print getmembers(self)
    for test in alltests:
        print "test: ", test.__name__, " on piseq gives\t ", test(piseq)
        print "\t..\t on zeros gives\t ", test(zeros)
        print "\t..\t on cheat gives\t ", test(cheat)
        print "\t..\t on rand gives\t", test(rand1)
