from __future__ import division

universities = [#University, Number of students, Tuition
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

#Functions should return list of students and list of tuition

def enrollment_stats(uni):
    students = []
    tuition = []
    for i in range(len(uni)):
        students.append(uni[i][1])
        tuition.append(uni[i][2])
    return students, tuition

a = enrollment_stats(universities)

def mean(list):
    total = 0
    n = len(list)
    for i in range(0, n):
        total += list[i]
    return total / n

def median(list):
    list.sort()
    while len(list) > 2:
        list.pop(0)
        list.pop(-1)
    if len(list) == 2:
        list.pop()
        return list
    elif len(list) == 0:
        print 'Error!'
    else:
        return float(list[0])

#a = enrollment_stats(universities)
#print a
#print median(a[0])    
#print '{:.2f}'.format(mean(a[1]))
string = 'The {} {} is {:.2f}.'
ops = ['average', 'median']
states = ['student population', 'tuition cost']

def sum_it(nlist):
    nlist = enrollment_stats(nlist)
    sumlist = [0 for i in range(len(nlist))]
    for j in range(len(nlist)):
        for i in range(len(nlist[j])):
            sumlist[j] += nlist[j][i]
    return sumlist

def do_it(listu):
    a = enrollment_stats(listu)
    stua = mean(a[0])
    tuta = mean(a[1])
    stum = median(a[0])
    tutm = median(a[1])
    meta = [(stua, tuta), (stum, tutm)]
    for j in range(len(ops)):
        for k in range(len(states)):
            print string.format(ops[j], states[k], meta[j][k])
            #print j, k
    
do_it(universities)
meh = '''The total number of students: {} 
The total tution fees collected: {}'''
print meh.format(*sum_it(universities))