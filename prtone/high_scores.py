import sys
import csv
import os

curDir = os.getcwd()
scores_file = 'scores.csv'
input = os.path.join(curDir, scores_file)

def check_file_exists(f):
    """Make certain file exists before proceeding."""
    if not os.path.exists(f):
        sys.exit('{} does not exist.'.format(f))
        
def get_names(dictionary):
    """
    Return the keys of the dictionary such that it is
    human readable as player names.
    """
    nameList = dictionary.keys()
    return nameList

def get_list_from_csv(csv_file):
    """Returns a list of rows from a csv file."""
    with open(csv_file, 'rb') as f:
        csv_reader = csv.reader(f)
        rows = []
        for row in csv_reader:
            rows.append(row)
    return rows

def check_list(list):
    """Checks if scores are valid integers."""
    for i in range(len(list)):
        assert int(list[i][1])

def create_entry(dict, key, score):
    """Creates an entry in the high scores."""
    dict[key] = score
    
def update_dict(d, k, s):
    """Different intention, same method."""
    create_entry(d, k, s)
   
def compare_scores(dict, key, score):
    """
    Compares the current score with the previous score.
    If no previous score exists, new entery is created.
    If current score is not lesser than existing Score,
        then high scores are updated.
    """
    key_list = get_names(dict)
    if key in key_list:
        existingScore = dict[key]
        if int(existingScore) > int(score):
#            print "New score is not sufficiently large."
            pass
        else:
#            print "Updating score..."
            update_dict(dict, key, score)
    else:
#        print "Creating new entry: {}, {}".format(key, score)
        create_entry(dict, key, score)
    
def process_list(list):
    """
    Takes a list, then term by term compares each
    term to the last. If comparison is sufficient,
    dictionary is updated before continuing.
    """
    dict = {}
    for i in list:
        key, score = i[0], i[1]
        compare_scores(dict, key, score)
    return dict

def save_sorted_scores(dict):
    """
    Sorts the names of the original dictionary,
    then writes them one by one to a new list.
    """
    names = get_names(dict)
    names.sort()
    high_scores = []
    for name in names:
        list = [name, dict[name]]
        high_scores.append(list)
    return high_scores
    
def print_scores(list):
    """Prints scores, one by one."""
    for i in list:
        print i[0], i[1]  
    
def do_task(inp):
    """
    Does it all.
    
    >>> curDir = os.getcwd()
    >>> scores_file = 'scores.csv'
    >>> input = os.path.join(curDir, scores_file)
    >>> do_task(input)
    Empiro 23
    L33tH4x 42
    LLCoolDave 27
    MaxxT 25
    Misha46 25
    O_O 22
    johnsmith 30
    red 12
    tom123 26
    """
    check_file_exists(inp)
    scoreList = get_list_from_csv(inp)
    check_list(scoreList)
    scoreDict = process_list(scoreList)
    sortedScores = save_sorted_scores(scoreDict)
    print_scores(sortedScores)
    
do_task(input)

if __name__ == "__main__":
    import doctest
    doctest.testmod()