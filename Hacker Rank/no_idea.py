n = raw_input().strip().split()
arr = raw_input().strip().split()
A =  set(raw_input().strip().split())
B = set(raw_input().strip().split())
happiness = 0

for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print happiness