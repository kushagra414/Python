# Using return in functions

def add(a, b):
    print "Adding %r and %r" % (a, b)
    return a+b
	
def sub(a, b):
    print "Subtracting %r and %r" % (a, b)
    return a-b
	
def mult(a, b):
    print "Multiplying %r and %r" % (a, b)
    return a*b
	
def div(a, b):
    print "Dividing %r and %r" % (a, b)
    return a/b
	
age = add(18, 2)
height = sub(190, 7)
weight = mult(35, 2)
iq = div(2000, 10)

print """Following are my confidential details:
1. My age = %r
2. My height = %r
3. My weight = %r
4. My iq = %r""" % (age, height, weight, iq)

# A puzzle for mind boggling-------------------------------------------------------------------------------------------------------------------------------------------

print "HeRe's A pUzZlE"
what = add(age, sub(height, mult(weight, div(iq, 2))))

print "That becomes:", what, "Can you do it by hand??"
