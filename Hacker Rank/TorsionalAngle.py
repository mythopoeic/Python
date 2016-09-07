class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return "{}, {}, {}".format(self.x, self.y, self.z)

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)

    def __add__(self, point):
        return Point(self.x+point.x, self.y+point.y, self.z+point.z)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y, self.z - point.z)
  
    def dot(self, point):
        return self.x*point.x + self.y*point.y + self.z*point.z
    
    def cross(self, point):
        return Point(self.y * point.z - self.z * point.y, 
                    self.z * point.x - self.x * point.z, 
                    self.x * point.y - self.y * point.x)
    
    def abs(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

from math import acos, degrees

myList = map(float, raw_input().split())
A = Point(myList[0], myList[1], myList[2])

myList = map(float, raw_input().split())
B = Point(myList[0], myList[1], myList[2])

myList = map(float, raw_input().split())
C = Point(myList[0], myList[1], myList[2])

myList = map(float, raw_input().split())
D = Point(myList[0], myList[1], myList[2])

AB = B - A

BC = C - B

CD = D - C

X = AB.cross(BC)

Y = BC.cross(CD)

PHI = acos(X.dot(Y)/(X.abs()*Y.abs()))

print('{:.2f}'.format(degrees(PHI)))
