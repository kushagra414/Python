ten_things = "Apple Orange Crows Telephone Light Sugar"

print "There are only six elements in the list!. Let's add some more!"

stuff = ten_things.split(' ')
#split - Breaks all keywords with spaces between them
more_stuff ='Spoon Roohafza Glucose Squash Grapes Lemonade IceTrays ColdCoffe'
more_stuff = more_stuff.split(' ')

while len(stuff) != 10:
    next_one = more_stuff.pop() #By default the pop function have -1 as argument
    print "Adding:  ",next_one
    stuff.append(next_one)
    print "There's %d item now." % len(stuff)

print 'There we go:', stuff

print "Let's do some things like stuff."

print stuff[1]
print stuff[-7]
print stuff.pop()
print ' '.join(stuff)  #joins all the elements by space
print '#'.join(stuff[3:5]) #add '#' between 3 and 4. in this just like range(1,5) 5 is excluded
print '@'.join(stuff[0:8])
