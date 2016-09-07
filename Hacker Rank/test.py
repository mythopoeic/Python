import math

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "{}, {}, {}".format(self.x, self.y, self.z)
        
    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Point3D(self.y * other.z - self.z * other.y, 
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)
    
    def l2norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
make_point = lambda x: Point3D(*map(float, x.strip().split()))
A = make_point(raw_input())

B = make_point(raw_input())

C = make_point(raw_input())

D = make_point(raw_input())

X = (B - A).cross(C - B)
print X
Y = (C - B).cross(D - C)
print Y
cos_angle = X.dot(Y) / (X.l2norm() * Y.l2norm())
angle_radians = math.acos(cos_angle)
angle_degree = 180 * angle_radians / math.pi
print('{:.2f}'.format(angle_degree))