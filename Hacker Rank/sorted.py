N,M = raw_input().split()
N = int(N)
M = int(M)
table = []
for _ in range(N):
    lis = map(int, raw_input().split())
    table += [lis]

k = input()


print sorted(table, key=lambda place: place[k])