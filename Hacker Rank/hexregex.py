import re
N = input()
valid = False
for _ in range(N):
    myString = raw_input()
    match = re.findall(r'#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3}', myString)
    if valid = True:
        if len(match)>0:
            print '\n'.join(match)
    
    if '{' in myString:
        valid = True
    
    if '}' in myString:
        valid = False 