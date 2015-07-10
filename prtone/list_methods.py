desserts = ['ice cream', 'cookies']
desserts.sort()
#print desserts.index('cookies')
print desserts

food = desserts[:]
other = ['broccoli', 'more foo stuff']
food.extend(other)
a = food.index('cookies')
food.pop(a)

print food[:2], desserts

string = 'cookies, cookies, cookies'
breakfast = string.split(", ")
print breakfast

list = [2 ** i for i in range(8)]
exclusivelist = []

for i in range(len(list)):
    j = list[i]
    if 0 < j <= 20:
        exclusivelist.append(j)
    else:
        pass
    
print exclusivelist