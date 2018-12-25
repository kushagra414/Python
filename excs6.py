language = 'Python'
python = 'High level language'
company = "Google" # Can use single or double inverted commas in string 
level = 'Easy %d' % 1
programming = 'I love programming %r ' # Used to connect two variables in output
and1 = 'and %s'
goal = 'I want to learn python than start Artificial Intelligence in Python'
print "There are %d level languages" % 3
print "%s is a %s because it is %s to understand and is very similar to english thus hard to understand by the machine" % (language, python, level)
print programming % and1 % goal #  Can use % sign to connect two variables
#As you can see after first % sign the output is in single inverted commas 
# %r will give raw data as output where as %s and %d will give string and integer as output respectively
a = 'I am'
b = ' Awesome!'
print a + b # can also us + to connect two strings
