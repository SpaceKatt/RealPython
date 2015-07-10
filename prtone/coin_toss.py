from __future__ import division
from random import randint

avg = 0
trials = 10000
times = 100
answers = {0:0, 1:0}

def flip_coin():
    result = randint(0, 1)
 #   print "flipped a {}".format(result)
    return result

def keep_flipping(r):
    flip_count = {r:1}
    result = r
    while result == r:
        answers[r] += 1
        result = flip_coin()
#    print 'endflip'
    return flip_count

def do_the_thing():
    for i in range(trials):
        count = keep_flipping(flip_coin())
        keyy = count.keys()
        key = keyy[0]
        answers[key] = (answers[key] + count[key]) / 2
    string = "The average number of flips needed to see both sides of a coin: {:.4}"
    return string.format((answers[0] + answers[1]) / 2)

first = do_the_thing()
string = "The average number of flips needed to see both sides of a coin: "
avg = float(first.replace(string, ''))

for i in range(times):
    result = do_the_thing()
    print result
    avg = (avg + float(result.replace(string, ''))) / 2

print "Average after {} trials:".format(trials * times), avg