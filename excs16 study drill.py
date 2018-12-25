
# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

print 'Going to open the file for reading purpose'
opentxt = open(filename, 'r')

print "Now reading the file.."
print opentxt.read()
opentxt.close

# Before opening the file in another mode, first you must close the file.
# w mode deletes all the txt in the file before writing in the file
print 'Going to open the file to write purpose'
opentxt = open(filename, 'w+')

# You cannot read the file in w mode.
print 'Reading the file in "w" mode'
opentxt.close
opentxt = open(filename)
print opentxt.read()

opentxt.close
opentxt = open(filename, 'w')

print "I am going to ask you for 3 lines that you want to put in the txt file"
line1 = raw_input('line1 :')
line2 = raw_input("line2 :")
line3 = raw_input("line3 :")
line4 = line1 + '\n' + line2 + '\n' + line3 + '\n' 

print "Writing the txt you entered to the file..."
opentxt.write(line4)

print "Reading the file after adding the 3 lines..."
print opentxt.read
opentxt.close

print 'Now opening the file in "a" '
opentxt = open(filename, 'a')

print "I am going to ask you for 3 lines that you want to put in the txt file"
line1 = raw_input('line1 :')
line2 = raw_input("line2 :")
line3 = raw_input("line3 :")
line4 = line1 + '\n' + line2 + '\n' + line3 + '\n' 

print "Adding the txt you entered to the file..."
opentxt.write(line4)

print 'Final reading of the file'
opentxt.close
opentxt = open(filename)
print opentxt.read