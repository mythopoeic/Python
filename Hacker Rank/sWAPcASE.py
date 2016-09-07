string = raw_input()
a = []
for i in range(len(string)):
    if string[i].isupper():
        a.append(string[i].lower())
    elif string[i].islower():
        a.append(string[i].upper())
    else:
        a.append(string[i])

print ''.join(a)