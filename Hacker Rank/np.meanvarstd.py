import numpy
col, row = map(int, raw_input().split()) # better input and array creation
arr = numpy.array([raw_input().split() for _ in range(col)], numpy.float)

myArray = numpy.array(myList)

print numpy.mean(myArray, axis = 1)
print numpy.var(myArray, axis = 0)
print numpy.std(myArray)