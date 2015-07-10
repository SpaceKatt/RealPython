string = raw_input("How internet are you? ")
#string = "speech to be processed into leet, abelost"

l33t = {'a':'4', 'b':'8', 'e':'3',
        'l':'1', 'o':'0', 's':'5', 't':'7'}

for a in l33t:
    string = string.replace(a, l33t[a])

print string
