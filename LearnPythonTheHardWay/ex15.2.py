from sys import argv

script = argv

print "Please type a filename:"
filename = raw_input("> ")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()
