# lists
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

i = 0

while 0 <= i < 6:
	i = int(raw_input('Enter a number between 0 and 6: '))
	if 0 <= i < 6:
		print "The animal at %d is:" % i
		print animals[i]
		
