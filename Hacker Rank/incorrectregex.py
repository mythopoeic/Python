import re
N = input()
for _ in range(N):
    try:
        match = re.search(raw_input(),'test')
        print True
    except:
        print False