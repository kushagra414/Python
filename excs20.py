from sys import argv
script, file_name = argv

def print_all(f):
    print f.read()
	
def rewind(f):
    print f.seek(0)                           # seek function will take the pointer abck to line 0. hece i will be able to print the txt again.
	
def print_a_line(line_count, f):
    print line_count, f.readline()            # readline returns \n at end at the line hence you  will see an  empty line in output.
	

current_file = open(file_name)

print "First let us print all the txt"
print_all(current_file)

print "Now lets rewind like a kind of tape."
rewind(current_file)                           # if i dont use this function then function print_a_line will not print the txt as the pointer is on line 6 which is empty

print "Lets print 5 lines: "

current_line = 1
print_a_line(current_line, current_file)       # In the argument you pass a integer and name of the file so readline() function can read the lines
                                               # readline() functio automatically keeps shifting to the next line as you call the function
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# Inside readline() is code that scans each byte of the file until it finds a \n character, then stops reading the file to return what it found so far.
# The file f is responsible for maintaining the current position in the file after each readline() call, so that it will keep reading each line.