# test input to see if it is a valid float without letters.
import re
N = input()
for _ in range(N):
    print bool(re.match(r"^\W*{0,1}[0-9]*\.[0-9]+$",raw_input()))