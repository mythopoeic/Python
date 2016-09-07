import re
match = re.split(r'[,.]', raw_input())
for each in match:
    if each.isdigit():
        print each