from collections import deque
'''
n = input()
s = set(map(int, raw_input().split())) 
N = input()
for i in range(N):
    string = raw_input()
    if string == "pop":
        comm = "s.%s()" % string
        exec comm
    else:
        lis = string.split()
        comm = "s.%s(%s)" % (lis[0],lis[1])
        exec comm

print sum(s)
'''
d = deque()

from collections import deque
d = deque()

for _ in xrange(input()):
    string = raw_input().strip()
    if string == "pop" or string == "popleft":
        command = string
        getattr(d, command)()
    else:
        command, newSet = string.split()
        getattr(d, command)(newSet)
    
for each in d:
    print each,