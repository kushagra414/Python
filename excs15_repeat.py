from sys import argv
script, filename = argv

txt = open(filename)

print txt.read()

print 'enter file name again :'
file_again = raw_input('>')

txt_again = open(file_again)

print txt_again.read()
