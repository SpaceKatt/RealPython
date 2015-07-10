mapper = dict(key='value', order='optomized for hasing', thing='relationship')

def p():
    print mapper
    
p()
mapper['new'] = 'stuff'
mapper['new'] = 'stuffzz'
p()
#del(mapper['thing'])
print mapper.keys()
print 'thing' in mapper

for stuff in sorted(mapper):
    print '{}, {}'.format(stuff, mapper[stuff])
    
nest = dict(layer='cake', reason='rhyme')
masterd = dict(something=mapper, nothing=nest)


def g():
    print masterd
    
g()

print masterd['nothing']['layer']

simple_dict = dict([("string1","value1"), ("string2",2), ("string3",3.0)])
    
