
from numpy.random import randint
from scipy.stats.mstats import chisquare
from collections import defaultdict

import scipy as sp
import pylab as py
import scipy.stats as stats

import bz2

piseq = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
zeros = "0"*100
ones = "1"*100
cheat = "0123456789"*10
rand1 = randint(0,10,100)
rand2 = randint(0,10,100)
human = "8530997216547843729981109810291273946273987564637882372920837467763788736434326667666672628399347829"


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

def renorm(real, exp, scale):
    return 2*sp.arctan(scale/(abs(real-exp)+1e-10))/sp.pi

########################################
## THE TESTS
########################################

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

    return max(1e-10,entropy/sp.log2(10))

def test_serial1(guys):
    arr = sp.array(list(to_ints(guys)),dtype="float")
    n = len(guys)
    mu = sp.mean(arr)
    v = sp.var(arr)

    front = arr[1:]
    back = arr[:-1]

    return 1-abs((1./n * sp.sum( (front-mu)*(back-mu) ))/(v+1e-10))

def test_mean(guys):
    good = 9./2
    sample = sp.mean(sp.array(list(to_ints(guys))))
    return renorm(good, sample, 0.5)

def test_std(guys):
    good = (10**2-1.0)/12.0
    sample = sp.std(sp.array(list(to_ints(guys))))**2
    return renorm(good, sample, 1)

def test_skew(guys):
    good = 0.0
    sample = stats.skew(sp.array(list(to_ints(guys))))
    return renorm(good, sample, 1e-1)

def test_kurtosis(guys):
    good = -6.0/5.0 * (10**2+1.0)/(10**2-1.0)
    sample = stats.kurtosis(sp.array(list(to_ints(guys))))
    return renorm(good, sample, 0.7)
