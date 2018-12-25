# -*- coding: utf-8 -*-
# open(file, 'w')
# The first argument is a string containing the filename.
# The second argument is another string containing a few characters describing the way in which the file will be used. 
# mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased),
# 'a' opens the file for appending; any data written to the file is automatically added to the end.
# 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

from sys import argv

script, filename = argv

print "We are erasing the file"
print "Hit Ctrl-c, if you do not wish t delete the file"
print "Hit RETURN, to continue deleting the file"

raw_input('?')

print "Opening the file..."
target = open(filename, 'w')

print "deleting the txt in file..."
target.truncate()

print "Now i am going to ask you three lines to put in the file"

line1 = raw_input('Line 1:')
line2 = raw_input('Line 2 :')
line3 = raw_input('Line 3:')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And finally closing the file"
target.close()