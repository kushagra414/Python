class Y  :
    def stuff(self):
        return 'I love to print random stuff'

class X(Y):
    pass

printY = Y()
print printY.stuff

printX = X()
print printX.stuff
