import numpy
N,M = raw_input().split()
N = int(N)
M = int(M)

myList = []


for _ in range(N):
    myList.append(map(int,raw_input().split()))

myArray = numpy.array(myList)

print numpy.transpose(myArray)
print myArray.flatten()