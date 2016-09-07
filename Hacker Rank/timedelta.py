'''
import time
T = input()
lis = []
for _ in range(T):
    s1 = raw_input().split()
    tz1 = s1.pop()
    s1 = ' '.join(s1)
    t1 = time.strptime(s1, "%a %d %b %Y %H:%M:%S")
    print t1
    s2 = raw_input().split()
    tz2 = s2.pop()
    s2 = ' '.join(s2)
    t2 = time.strptime(s2, "%a %d %b %Y %H:%M:%S")
    print t2
    t3 = abs(t1-t2)
    lis.append(t3)

for each in lis:
    print each
'''    
import calendar
import operator
from time import strptime
def parseTime(str):
    ops = { "+": operator.sub, "-": operator.add } 
    spl = str.rsplit(" ",1)
    t = strptime(spl[0], "%a %d %b %Y %H:%M:%S")
    tz = ops[spl[1][0]](0,int(spl[1][1:3]) * 3600 + int(spl[1][3:]) * 60)
    return calendar.timegm(t) + tz
for _ in range(int(input())):
    print(abs(parseTime(raw_input()) - parseTime(raw_input())))