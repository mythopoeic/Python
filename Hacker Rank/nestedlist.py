N = int(raw_input())
nlist = []

for i in range(N):
    nlist.append([raw_input(), float(raw_input())])

scores = sorted({s[1] for s in nlist})
result = sorted(s[0] for s in nlist if s[1] == scores[1])

print '\n'.join(result)