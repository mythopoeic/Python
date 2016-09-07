N,X = raw_input().split()
N = int(N)
X = int(X)
grades = []
stID = [i + 1 for i in range(N)]
for _ in range(X):
    lis = map(float, raw_input().split()) 
    grades += [lis]

Z = zip(stID, *grades)

for i in range(N):
    print "%.1f" % (sum(Z[i][1:])/X)
    
