import string

albet = string.ascii_lowercase
N = int(raw_input())
w = 4 * (N - 1) + 1

for i in range(N - 1,-N,-1):
    l = [albet[j] for j in range(N-1,abs(i),-1)]
    l.append(albet[abs(i)])
    l.extend([albet[j] for j in range(abs(i)+1,N)])
    print '-'.join(l).center(w,'-')