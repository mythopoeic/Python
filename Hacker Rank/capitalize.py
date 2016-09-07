list = raw_input().split(' ')
a = []
for each in list:
    for i in range(len(each)):
        if each[i].isdigit():
            a.append(each)
            break
    else:
        a.append(each.capitalize())

print ' '.join(a)