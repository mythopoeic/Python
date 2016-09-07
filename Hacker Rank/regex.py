import re

# match example

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:                      
    print 'found', match.group() ## 'found word:cat'
else:
    print 'did not find'

    
# email example, doesn't catch '-' or '.'    

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print match.group()  ## 'b@google'

# square brackets indicate a set of characters
# codes \w \s etc work inside, too
# except . which just means .
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print match.group()  ## 'alice-b@google.com'
    
# findall()

  ## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

  ## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print email

# findall() with files
    
# Open file
f = open('shakespeare.txt', 'r')
  # Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'Hamlet', f.read(), re.IGNORECASE)
f.close()
print len(strings)

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print tuple[0]  ## username
    print tuple[1]  ## host

# Substitution    

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
  ## re.sub(pat, replacement, str) -- returns new string with all replacements,
  ## \1 is group(1), \2 group(2) in the replacement
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
  ## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher