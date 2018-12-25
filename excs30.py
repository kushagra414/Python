print "Enter no. of people:"
people = int(raw_input('>'))

print "Enter no. of cars:"
cars = int(raw_input(">"))

print "Enter no. of buses:"
buses = int(raw_input('>'))

if people>cars:
    print "Let's go by car."

elif people <cars:
    print "we should not take the cars."

else:
    print "We can't decide."


if cars>buses:
    print "Maybe we should take the buses."

elif cars<buses:
    print "That's too many buses."

else:
    print "We still can't decide."


if people>buses:
    print "Let's go by the bus"

else:
    print "Fine, Let's stay at home then."
