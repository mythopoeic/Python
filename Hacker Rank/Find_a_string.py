string = raw_input()
substring = raw_input()
score = 0
for i in range(len(string)):
   if string[i:i+len(substring)] == substring:
        score += 1
print score