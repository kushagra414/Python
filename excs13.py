from sys import argv
# Import adds the argument variable module to the script.


script, first, second, third = argv
# Argument variable is a variable that can hold argument that are passed to python script when we run it.
# Now in this line, argv is unpacks and values from it are stored in variables from left to right


print "The script is called:", script
print "Your first variable is:", first 
print "Your second variable is:", second
print 'Your third variable is:', third


# Note: Remember before running the script enter arguments or else you will get error
# Eg - python excs13.py apple pineapple pen