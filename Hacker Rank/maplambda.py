N = int(raw_input())
cube = lambda x: x**3
A = [0,1]
if N > 1:
    [A.append(A[-2]+A[-1]) for i in xrange(N-2)]
elif N == 1:
    del A[1]
else:
    A = []

B = map(cube,A)

print B