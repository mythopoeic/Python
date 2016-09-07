import re
vowels = "AEIOUaeiou"
cons = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"

myString = raw_input()
match = re.findall(r'['+cons+'](['+vowels+']{2,})(?=['+cons+'])', myString) # (?=...) is Positive lookahead
if match:
    for each in match:
        print each
else:
    print -1