from collections import OrderedDict
myDict = OrderedDict()
N = int(raw_input())
for i in range(N):
    string = raw_input().strip()
    if string in myDict:
        myDict[string] += 1
    else:
        myDict[string] = 1

print len(myDict)
for key in myDict:
    print myDict[key],