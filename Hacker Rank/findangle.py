import math
AB = int(raw_input())
BC = int(raw_input())
AC = (AB**2 + BC**2)**0.5
MC = AC/2.0
deg = u'°'.encode('“ISO-8859-1', 'replace')
x = math.asin(MC/BC)
x = int(round(math.degrees(x),0))
print "%d%s" % (x,deg)
'''
from math import atan,degrees
a=input()
b=input()
thet=atan(1.0*a/b)
print str(int(round(degrees(thet))))+'°'
'''