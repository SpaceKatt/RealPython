z = raw_input('Enter base: ')
x = raw_input('Enter power: ')

base = float(z)
power = float(x)
result = base ** power

text = 'Base {} to the {} power is {}.'
output = text.format(z, x, result)

print output