from itertools import product
A = map(int,raw_input().split())
B = map(int,raw_input().split())
AxB = product(A,B)

for i in list(AxB):
    print i,