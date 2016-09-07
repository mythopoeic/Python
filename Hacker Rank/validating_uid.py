import re
T = input()

for _ in range(T):
    string = raw_input()
    match = re.match(r'[a-zA-Z0-9]{10}$',string)
    digs = re.search(r'([0-9].*){3}',string)
    caps = re.search(r'([A-Z].*){2}',string)
    
    if match:
        if len(set(list(match.group()))) == 10 and digs and caps:
            print "Valid"       
        else:
            print "Invalid"
    else:
        print "Invalid"