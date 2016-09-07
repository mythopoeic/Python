from itertools import product
K, M = map(int, raw_input().split())
mylist = []
maximum = 0
for _ in range(K):
    l = list(map(lambda x: int(x)**2, raw_input().split()))
    del l[0]
    mylist.append(l)
for x in list(product(*mylist)):
    val = sum(x) % M
    if val > maximum:
        maximum = val
print maximum