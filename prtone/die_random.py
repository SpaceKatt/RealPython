from __future__ import division
from random import randint

die_count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
trials = 10000

for trial in range(trials):
    i = randint(1,6)
    die_count[i] += 1
#print die_count

intro = 'When considering a sample size of: {}\n...'
string = 'Chance of rolling a {}: {}%'
chance = []

print intro.format(trials)
for i in die_count:
    prob = (die_count[i] / trials)
    print string.format(i, 100 * prob)
    chance.append(prob)
    
original = '...\nThe avereage nuumber rolled is: {}'
average = 0

for i in die_count:
    average += chance[i - 1] * i

print original.format(average)