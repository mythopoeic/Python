import numpy
N,M = raw_input().split()
N = int(N)
M = int(M)

myList = []


for _ in range(N):
    myList.append(map(int,raw_input().split()))

myArray = numpy.array(myList)

myMin = numpy.min(myArray, axis = 1)

print numpy.max(myMin)