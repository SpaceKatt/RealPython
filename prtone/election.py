from __future__ import division
from random import random

regions = {1:.87, 2:.65, 3:.17} #decimal percent chance a wins
populations = [10000, 15000, 15943]

def election(popultations, regions):
    avic = 0
    bvic = 0
    for z in regions:
        for i in range(populations[z - 1]):
            avici, bvici = 0, 0
            e = random()
            if regions[z] + e >= 1:
                avici += 1
            else:
                bvici += 1
        if avici >= bvici:
            avic += 1
#            print "A wins region {}!".format(z)
        else:
            pass
#            bvic += 1
#            print "B wins region {}!".format(z)
    return avic
            
def election_announce(p, r):
    avic = election(p, r)
    bvic = len(r) - avic
    if avic > bvic:
#        print 'A WINS!'
        win = 'A'
    elif bvic > avic:
#        print 'B WINS!'
        win = 'B'
    else:
        print "It's been rigged!"
        win = 0
    return win
    
election_announce(populations, regions)

def tally(p, r, n): #n = number of elections
    win_count = {'A':0, 'B':0}
    for i in range(n):
        win = election_announce(p, r)
        if win == 0:
            continue
        else:
            win_count[win] += 1
    string = 'Percent chance {} will win overall: {}%'
    for canidate in win_count:
        probcani = 100 * (win_count[canidate] / n)
        output = string.format(canidate, probcani)
        print output
        
tally(populations, regions, 1000)