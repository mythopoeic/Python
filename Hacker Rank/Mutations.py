string = raw_input()
a = raw_input().split(" ")
num = int(a[0])
char = str(a[1])

l = list(string)
l[num] = char
string = ''.join(l)
print string