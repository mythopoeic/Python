from collections import namedtuple
N = int(raw_input())
Students = namedtuple('Students',raw_input())

mySum = 0

for i in range(N):
    grade = Students(*raw_input().strip().split())
    mySum += int(grade.MARKS)
   
average = mySum/float(N)
print "%.2f" % average