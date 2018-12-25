# ----------------------------This excersice is for the FOR loop-----------------------------------------

#First you have to make a list. Python takes the elements of the list and assigns the in to yhe variables

the_count = [1,2,3,4,5]
fruits = ['orange', 'grapes', 'mango', 'papaya', 'apple']
change = [1,'pennies', 2 , 'dimes', 3, 'quaters']

print the_count

#First kind of for loop
for number in the_count:
    print 'This is count :%d' % number

#Same as above with string to print
for fruit in fruits:
    print 'A fruit of type :%s' % fruit

#Here we will use %r as we don't have fixed data type
for i in change:
    print "I got %r" % i

#We can also built lists. First we have to start with an empty list
elements = []

#Then use range fn to do 0 to 5 counts
for i in range(0, 6):   #In range fn its like this -- range[0, 6)
    print "Adding %d to the list." % i
    #append is a function to add things to list
    elements.append(i)

#now we can print the list
for i in elements:
    print "This list was empty just a sec ago: %d" % i

elements = range(0, 6)

print elements
