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