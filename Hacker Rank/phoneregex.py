'''
In this example a valid phone number is 10 digits and starts with a 7,8, or 9
'''
import re
N = input()
for _ in range (N):
    match = re.match(r'[7-9]\d{9}$', raw_input())
    if match:
        print 'YES'
    else:
        print 'NO'