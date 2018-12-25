i = 0
number = []

while i<6:
    print "At the top i is %d" % i
    number.append(i)

    i = i+1

    print "Now the list is ", number
    print "In the bottom value of i is %d" % i


print "The numbers :"

for num in number:
    print num
