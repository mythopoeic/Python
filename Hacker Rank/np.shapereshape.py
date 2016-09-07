import numpy
myList = numpy.array(raw_input().split(), int)

#myList.shape = (3,3)

print numpy.reshape(myList, (3,3))
