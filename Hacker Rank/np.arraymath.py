import numpy
N,M = raw_input().split()
N = int(N)
M = int(M)

AList = []
BList = []

for _ in range(N):
    AList.append(map(int,raw_input().split()))
    
for _ in range(N):
    BList.append(map(int,raw_input().split()))
    
A = numpy.array(AList)
B = numpy.array(BList)

print A + B

print A - B

print A * B

print A / B

print A % B

print A ** B 
