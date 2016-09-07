# gets the argument variable feature from the sys package
from sys import argv

# assigns the arguments to two variables
script, filename = argv

#opens the file and assigns it to a text file object
txt = open(filename)

#reads the file and prints the contents to the screen.
print "Here's your file %r:" % filename
print txt.read()

#asks for the filename again, this time via raw_input
print "Type the filename again:"
file_again = raw_input("> ")

#assigns the raw_input file to a text file object
txt_again = open(file_again)

#reads the raw_input object and prints the contents to the screen
print txt_again.read()
txt.close()
txt_again.close()
