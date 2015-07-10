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
    """Returns a list from a csv file."""
    with open(csv_file, 'rb') as f:
        csv_reader = csv.reader(f)
        rows = []
        for row in csv_reader:
            rows.append(row)
    return rows

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
            print "New score is not sufficiently large."
        else:
            update_dict(dict, key, score)
    else:
        create_entry(dict, key, score)
    
#print get_list_from_csv(input)

def create_entry(dict, key, score):
    """Creates an entery in the high scores."""
    dict[key] = score
    
def update_dict(d, k, s):
    """Different intention, same method."""
    create_entry(d, k, s)
    
def process_list(list):
    dict = {}
    for i in list:
        key, score = i[0], i[1]
        compare_scores(dict, key, score)
    return dict

def save_sorted_scores(dict):
    names = get_names(dict)
    names.sort()
    high_scores = []
    for name in names:
        list = [name, dict[name]]
        high_scores.append(list)
    return high_scores
    
def do_task(inp):
    check_file_exists(inp)
    scoreList = get_list_from_csv(inp)
    scoreDict = process_list(scoreList)
    sortedScores = save_sorted_scores(scoreDict)
    for i in sortedScores:
        print i[0], i[1]
    
do_task(input)