# Hard coding means putting things in your code alredy that should be coming from user insead.
from sys import argv
script, filename = argv

txt = open(filename) # Opens the file in python

print 'Here is your file %r' % filename
print txt.read() # Prints tthe content of the file in python

print 'Type your file name again :'
file_again = raw_input('>')

txt_again = open(file_again)

print txt_again.read()
print 'Now closing the txt file'

txt_again = close(file_again)
