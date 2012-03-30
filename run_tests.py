
from numpy.random import randint

piseq = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
zeros = "0"*100
ones = "1"*100
alternate = "56"*50
cheat = "0123456789"*10
rand1 = randint(0,10,100)
rand2 = randint(0,10,100)
human = "8530997216547843729981109810291273946273987564637882372920837467763788736434326667666672628399347829"

import scipy as sp

def logit(p):
	if p == 0:
		p = 1e-5
	elif p == 1:
		p = 1 - 1e-5
	return sp.log(p) - sp.log(1-p)

def arclogit(a):
	return sp.exp(a)/(1 + sp.exp(a))

from inspect import getmembers
import tests

alltests = [guy for name,guy in getmembers(tests) if name.startswith('test_') ]

for test in alltests:
    print "test: ", test.__name__
    print "\t..\t on zeros gives\t ", test(zeros)
    print "\t..\t on ones gives\t ", test(ones)
    print "\t..\t on alternate gives\t ", test(alternate)
    print "\t..\t on cheat gives\t ", test(cheat)
    print "\t..\t on rand1 gives\t", test(rand1)
    print "\t..\t on rand2 gives\t", test(rand2)
    print "\t..\t on piseq gives\t", test(piseq)
    print "\t..\t on human gives\t", test(human)
    print


allseqs = [("zeros",zeros),("ones",ones),("alternate",alternate),("cheat",cheat),("rand1",rand1),("rand2",rand2),("piseq",piseq),("human",human)]



print "As for their average"

for name,seq in allseqs:
	score = 0.
	for test in alltests:
		score += test(seq)
	score /= float(len(alltests))

	print "Seq: ", name, " got a:\t ", score

print
print "As for their logit average"

for name,seq in allseqs:
	score = 0.
	for test in alltests:
		score += logit(test(seq))
	score /= float(len(alltests))

	score = arclogit(score)

	print "Seq: ", name, " got a:\t ", score