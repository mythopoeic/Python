import re
N = input()

for _ in range(N):
    name, email = raw_input().strip().split()
    match = re.match(r'\<[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}\>$', email)
    if match:
        print name, match.group()