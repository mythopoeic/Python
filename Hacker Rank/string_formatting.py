N = int(raw_input())
b = bin(N)
a = list(b)
del a[0:2]
width = len(''.join(a))

for i in xrange(1, N+1):
    b = bin(int(i)).replace('0b','').rjust(width, ' ')
    o = oct(int(i)).replace('0','', 1).rjust(width, ' ')
    h = hex(int(i)).replace('0x','').upper().rjust(width, ' ')
    j = str(i).rjust(width, ' ')
    print j, o, h, b