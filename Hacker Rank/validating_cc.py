import re
N = input()
check = True
grouped = []
for _ in range(N):
    ccn = raw_input()
    match = re.search(r'^([0-9]-*){16}$',ccn)
    start = re.search(r'^[4-6]',ccn)
    sep = re.search(r'[\s_]|\-{2,}',ccn)
    clean = re.sub(r'[-]', '', ccn)
    repeat = re.search(r'([0-9])\1{3}',clean)
    if len(clean) != len(ccn):
        grouped = re.findall(r'([0-9]+)-?',ccn)
    

    
    if match and start and sep == None and repeat == None:
        if len(grouped) != 0:
            for each in grouped:
                if len(each) != 4:
                    check = False
                
            if check == True:
                print "Valid"
            else:
                print "Invalid"
                
        else:
            print "Valid"
    else:
        print "Invalid"
    check = True
    grouped = []