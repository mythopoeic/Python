import numpy

arrA = numpy.array(raw_input().split(), numpy.int)
arrB = numpy.array(raw_input().split(), numpy.int)

print numpy.inner(arrA,arrB)
print numpy.outer(arrA,arrB)