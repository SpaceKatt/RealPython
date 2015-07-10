try:
    integer = raw_input('Enter a whole, real number: ')
    real = int(integer)
except  ValueError:
    print 'Next time, try following the criteria...'

real = int(integer)
factors = []

for a in range(1, real + 1):
    remainder = real % a
    if remainder == 0:
        factors.append(a)
    else:
        pass

string = '{} is a factor of {}.'
#print factors

for z in range(len(factors)):
    print string.format(factors[z], real)