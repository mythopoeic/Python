# variable with string and format code for an integer decimal 
x = "There are %d types of people." % 10
# asign string variables
binary = "binary"
do_not = "don't"
# string variable with a format code to add other string variables.
y = "Those who know %s and those who %s." % (binary, do_not)

# print the string variables
print x
print y

# %r shows the string with its additional information.
print "I said %r." % x
print "I also said: '%s'." % y 

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# print the joke_evaluation string and include the string for %r
print joke_evaluation % hilarious

# create some more strings
w = "This is the left side of..."
e = "a string with a right side."

# combine the strings together and print them.
print w + e