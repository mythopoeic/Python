from collections import Counter


for k,v in sorted( Counter(raw_input()).most_common(3) , key = lambda x: (-x[1],x[0])):
    print k,v


'''
string = raw_input()
mylist = list(string)
mylist = sorted(mylist, key=itemgetter(1,0))
A = Counter(mylist)

B = A.most_common()
print B
'''
'''
temp = []
earned = 0

for each in range(N):
    temp = map(int, raw_input().split())
    if temp[0] in Counter(sizes).keys():
        if Counter(sizes)[temp[0]] > 0:
            earned += temp[1]
            sizes.remove(temp[0])
        
print earned
'''