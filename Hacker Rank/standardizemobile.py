import re
N = input()
myArray = []

for _ in range(N):
    myArray.append(raw_input())

#print myArray

def decorate(func):
    def inner(arg):
        a = func(arg)
        for i in range(len(a)):
            firstpart, secondpart = a[i][:len(a[i])/2], a[i][len(a[i])/2:]
            a[i] = "+91 %s %s" %(firstpart,secondpart)
        return a
    return inner

@decorate
def arrSort(arg):
    
    for i in range(len(arg)):
        arg[i] = re.search(r'\d{10}$',arg[i]).group()
    arg = sorted(arg)
    return arg
    


sortedArray = arrSort(myArray)

for each in sortedArray:
    print each