import re
myString = raw_input()
match = re.search(r'([a-z0-9A-Z])(\1)', myString)
if match:
    print match.group(1)
else:
    print -1