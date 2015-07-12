from __future__ import division
from random import randint

"""
For a certian number of trials:
    A coin is flipped:
        This coin is flipped over and over until it achieves
        a different result.
    The number of times this coin is flipped is recorded and added to a list.
    Repeat
    
Then, this list is averaged to find the mean number of times you will
have to flip a coin to see both sides of said coin (assuming there are two).

This process is repeated a certian number of times. Then all is averaged again.

The overall result should be around three.
"""

def flip_coin():
    """
    Return a 1 or 0 as a head or a tails.
    
    >>> result = flip_coin()
    >>> options = [1, 0]
    >>> result in options
    True
    """
    result = randint(0, 1)
 #   print "flipped a {}".format(result)
    return result

def keep_flipping(r):
    """
    When a 1 or a 0 (heads or tails) is flipped,
    the coin is continued to flip until it reaches
    a new result. Every time a similar result is
    flipped, the flip_count is increased.
    This function returns the number of times the same
    side of a coin is flipped, along with which side that is.
    """
    flip_count = {r:1}
    result = r
    while result == r:
        flip_count[r] += 1
        result = flip_coin()
#    print 'endflip'
    return flip_count

def take_average(results):
    """
    Takes a dictionary of results, each value is a list of results,
    each key signifying head or a tails. Takes each value list, 
    finds the average, then assigns the average to the corresponding key.
    
    >>> stuff = {0:[1,2,3], 1:[2,3,4]}
    >>> avg = take_average(stuff)
    >>> print avg[0], avg[1]
    2.0 3.0
    """
    keys = results.keys()
    average = {0: 0, 1: 0}
    for key in keys:
        count = 0
        total = 0
        for i in results[key]:
            total += i
            count +=1
        average[key] = total/count
    return average

def do_the_thing(trials):
    """
    Creates a dictionary of heads and tails, both tied to empty lists.
    Then, for a certian number of trials, a coin is flipped and is 
    continually flipped until a new result is achieved, whether heads or tails.
    The number of flips this takes is added to the list which exists 
    in the heads/tails dictionary, under the corresponding heads/tails key.
    This is then averaged into a dictionary, where heads&&tails are
    still seperated, which is then further averaged into a single value.
    """
    answers = {0:[], 1:[]}
    for i in range(trials):
        count = keep_flipping(flip_coin())
        keyy = count.keys()
        key = keyy[0]
        answers[key].append(count[key])
    avg = take_average(answers)
    average = (avg[0] + avg[1]) / 2
    string = "The average number of flips needed to see both sides of a coin: {:.4}"
    print string.format((average))
    return average


def do_many_times(trials, times):
    """
    Invokes do_the_thing(trials) a certian amount of times,
    then averages and prints all results.
    """
    count, total = 0, 0
    for i in range(times):
        result = do_the_thing(trials)
        total += result
        count += 1
    avg = total / count
    print "Average after {} trials:".format(trials * times), avg
    return avg

do_many_times(100, 100)

if __name__ == "__main__":
    import doctest
    doctest.testmod()