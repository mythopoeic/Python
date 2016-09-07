string = raw_input()
presence = False
for i in range(len(string)):
    if string[i].isalnum():
        presence = True
        break
    else:
        presence = False
print presence

for i in range(len(string)):
    if string[i].isalpha():
        presence = True
        break
    else:
        presence = False
print presence

for i in range(len(string)):
    if string[i].isdigit():
        presence = True
        break
    else:
        presence = False
print presence

for i in range(len(string)):
    if string[i].islower():
        presence = True
        break
    else:
        presence = False
print presence

for i in range(len(string)):
    if string[i].isupper():
        presence = True
        break
    else:
        presence = False
print presence