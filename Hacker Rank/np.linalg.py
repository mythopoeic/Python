import numpy
N = input() # better input and array creation
arrA = numpy.array([raw_input().split() for _ in range(N)], numpy.float)

print numpy.linalg.det(arrA)