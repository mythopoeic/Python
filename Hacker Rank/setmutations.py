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
        comm = "s.%s(%s)" % (lis[0],set(map(int, raw_input().split())))
        exec comm
print sum(s)

## Better with getattr to run method. getattr is preferred to exec
'''
(_, A) = (
    raw_input(),
    set(map(int, raw_input().split()))
)

for _ in xrange(input()):
    (command, newSet) = (
        raw_input().split()[0],
        set(map(int, raw_input().split()))
    )

    # Cool trick. Since our commands are method names, just
    # execute the method on A with our new set as its argument.
    getattr(A, command)(newSet)

print str(sum(A))
'''