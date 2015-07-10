number_of_cats = 100
walks = number_of_cats
cat_hats = {}
cats = [0 for cat in range(number_of_cats)]
for i in range(len(cats)):
    cat_hats[i] = cats[i]
    
def test_hat(dict):
    string = 'Cat {} has {} hat.'
    cat_list = dict.keys()
    for i in cat_list:
        if dict[i] == 1:
            print string.format(i, 'a')
        else:
            print string.format(i, 'no')

def cat_walk(cats, walks):
    """Cats should be a dictionary.
    Walk around the cats, counting every one, then every other,
    then every 3rd, every 4th..., every walk-th time.
    """
    walk = 1
    while walk <= walks:
        cat_index = 0
        while cat_index <= (number_of_cats - 1):
            if cat_hats[cat_index] == 0:
                cat_hats[cat_index] = 1
            else:
                cat_hats[cat_index] = 0
            cat_index += walk
        walk += 1

cat_walk(cat_hats, walks)
test_hat(cat_hats)