print "Let's practice everything we have learned till now"
print "I need to try escape\" again \\ with \t tabs and \n new lines"
poem = """Hey this a poem \n
\tThe lovely world
with logic so firmly placed
cannot discern \n the needs of love
nor comprehend passion fro intuition
\n\t\twhere there is none.
"""

print "------------------------------------"
print "poem"
print "------------------------------------"

five = 10-2-3
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started*500
    bars = jelly_beans / 100
    crates = bars / 100
    return jelly_beans, bars, crates

start_point = 1000
beans, jars, crates = secret_formula(start_point)

print "With starting point of : %d" % start_point
print "We have %d beans, %d jars, %d crates" % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, %d crates." % (secret_formula(start_point))
