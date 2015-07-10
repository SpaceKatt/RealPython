from capitals import capitals_dict as di
from random import randint

states = di.keys()
sele = randint(0, len(states) - 1)
correct = False
state = states[sele]
cap = di[state]
prompt = 'What is the capitol of {}? '.format(state)

while correct != True:
    answer = raw_input(prompt)
    answer = answer.lower()
    if answer == 'exit':
        print 'The capitol of {} is {}. Goodbye!'.format(state, cap)
        break
    elif answer == cap.lower():
        print 'Correct! {} is the capitol of {}!'.format(cap, state)
        correct = True
    else:
        letdown = 'Sorry... {} is not the capitol of {}...'
        print letdown.format(answer, state)