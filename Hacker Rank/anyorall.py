N = input()
a = map(int,raw_input().split())
b = []
for each in a:
    b.append(each > 0)

if all(b):
    print any([str(i) == str(i)[::-1] for i in a])
else:
    print all(b)