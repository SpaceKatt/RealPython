print "Hello, world"

variable = "Vixen"

print 'H' + variable[1:]

class Test:
  
  list = [1,2,3,4]

  def __init__(self):
    print "int,.," 
  
  def len(self):
    print "Does this create a local len()?"
    

a = Test()

a.len()

print len(a.list)

abc = raw_input("Spagetti Breath? ")

not_gross = 'Huh...'

if 'y' in abc:
    print "Gross..."
else:
    print not_gross