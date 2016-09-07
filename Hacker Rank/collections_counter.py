from collections import Counter
X = int(raw_input())
sizes = map(int, raw_input().split())
N = int(raw_input())
temp = []
earned = 0

for each in range(N):
    temp = map(int, raw_input().split())
    if temp[0] in Counter(sizes).keys():
        if Counter(sizes)[temp[0]] > 0:
            earned += temp[1]
            sizes.remove(temp[0])
        
print earned