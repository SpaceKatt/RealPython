"""
Determine which cats have hats on their heads,
after walking about and switching their hat status.
"""

def create_cats(number_of_cats):
    """
    Create a dictionary consisting of a cat index number
    and a binary hat counter. (0 = no hat, 1 = hat)
    
    >>> create_cats(3)
    {0: 0, 1: 0, 2: 0}
    """
    cat_hats = {}
    cats = [0 for cat in range(number_of_cats)]
    for i in range(len(cats)):
        cat_hats[i] = cats[i]
    return cat_hats
    
def test_hat(dict):
    """
    Prints out each cat and their hat status.
    
    >>> cats = {1: 0, 2: 1, 3: 0}
    >>> test_hat(cats)
    Cat 1 has no hat.
    Cat 2 has a hat.
    Cat 3 has no hat.
    """
    string = 'Cat {} has {} hat.'
    cat_list = dict.keys()
    for i in cat_list:
        if dict[i] == 1:
            print string.format(i, 'a')
        else:
            print string.format(i, 'no')

def cat_walk(cats, walks):
    """
    Cats should be a dictionary.
    Walk around the cats, counting every one, then every other,
    then every 3rd, every 4th..., every walk-th time.
    
    >>> cats = {0: 0, 1: 0, 2: 0}
    >>> cat_walk(cats, len(cats))
    >>> test_hat(cats)
    Cat 0 has a hat.
    Cat 1 has no hat.
    Cat 2 has no hat.
    """
    walk = 1
    while walk <= walks:
        cat_index = walk - 1
        while cat_index <= (walks - 1):
            if cats[cat_index] == 0:
                cats[cat_index] = 1
            else:
                cats[cat_index] = 0
            cat_index += walk
        walk += 1

def do_thing(number_of_cats):
    """
    Does all the things to do the thing.
    
    >>> do_thing(100) # doctest: +ELLIPSIS
    Cat 0 has a hat.
    Cat 1 has no hat.
    ...
    Cat 99 has a hat.
    """
    walks = number_of_cats
    cat_hats = create_cats(walks)
    cat_walk(cat_hats, walks)
    test_hat(cat_hats)

do_thing(100)

if __name__ == "__main__":
    import doctest
    doctest.testmod()