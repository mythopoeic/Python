import re
P = raw_input().strip()
match = []
alter = []

match = re.findall(r'^[1-9][0-9]{5}$',P)
alter = re.findall(r'(.)(?=\d\1)',P)

print len(match) == 1 and len(alter) <= 1 