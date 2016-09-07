import re
N,M = raw_input().split()
N = int(N)
M = int(M)
myList = []
Matrix = [[0 for x in range(M)] for y in range(N)]
Matrix2 = [[0 for x in range(N)] for y in range(M)]
for i in range(N):
    row = list(raw_input())
    for j in range(M):
        Matrix[i][j] = row[j]

for i in range(M):
    for j in range(N):
        Matrix2[i][j] = Matrix[j][i]

for each in Matrix2:
    myList += each

myStr = ''.join(myList)
clean = re.sub(r'(?<=\w)\W+(?=\w)', ' ', myStr)
print clean