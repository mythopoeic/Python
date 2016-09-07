from collections import OrderedDict
N = int(raw_input())
myDict = OrderedDict()
for i in range(N):
    entry = raw_input().split()
    price = int(entry.pop())
    string = ' '.join(entry)
    if string in myDict.keys():
        myDict[string] = myDict[string] + price
    else:
        myDict[string] = price

for key, value in myDict.items():
    print key, value