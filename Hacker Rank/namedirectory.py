from operator import itemgetter
import re

def decorator(func):
    def inner(arg):
        a = func(arg)
        b = []
        for i in range(len(a)):
            a[i][3] = re.sub(r'M','Mr.',a[i][3])
            a[i][3] = re.sub(r'F','Ms.',a[i][3])
            string = "%s %s %s" % (a[i][3], a[i][0], a[i][1])
            b.append(string)
        return b
    return inner
        

@decorator
def agesorter(arg):
    arg.sort(key=itemgetter(2))
    return arg

N = input()
array = []


for _ in range(N):
    array.append(raw_input().split())



sortedarray = agesorter(array)

for each in sortedarray:
    print each