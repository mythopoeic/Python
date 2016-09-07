from sys import argv

script , filename = argv

print "We're going to read %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'r')

print "Let's read the file!"
lines = target.read()
print lines
