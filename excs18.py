# In this excersice we will make our own function

def two_arg(*args):
    arg1, arg2 = args
    print "Here are two arguments %r and %r" % (arg1, arg2)

def two_arg_again(arg1, arg2):
    print "here are again the two of them %r and %r" % (arg1, arg2)

def none_arg():
    print 1+1

two_arg('Hello', "World")
two_arg_again('Hello World', "again")
none_arg()
