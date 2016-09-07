import numpy
N,M, P = raw_input().split()
N = int(N)
M = int(M)
P = int(P)

NList = []
MList = []

for _ in range(N):
    NList.append(map(int,raw_input().split()))
    

for _ in range(M):
    MList.append(map(int,raw_input().split()))
    
NArray = numpy.array(NList)
MArray = numpy.array(MList)

print numpy.concatenate((NArray,MArray))