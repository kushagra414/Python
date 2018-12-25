# THIS IS VERY IMPORTANT  -----   ALWAYS USE PARANTESIS IN FUNCTION I ALMOST WASTED 1 HR TO FIND THAT OUT

from sys import argv

from os.path import exists

script, from_file, to_file = argv

print "Copying data from %s to %s" % (from_file, to_file)

in_file = open(from_file)
in_data = in_file.read()
# Instead of above two lines we can use indata = open(from_file).read() 

print "Does the output file exist? %r" % exists(to_file)

 # Checks if the file with given name is in the system
print "READY, hit return to continue, hit CTRL-C to leave"

raw_input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Every thing is dane check the files.."

out_file.close()
in_file.close()