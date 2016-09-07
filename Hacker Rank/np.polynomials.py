import numpy

arrA = numpy.array(raw_input().split(), numpy.float)
x = input()
print numpy.polyval(arrA,x)