class Complex:
    '''creates a complex number from an input and defines basic math operations'''
    def __init__(self, real, imag):
        self.real = float(real)
        self.imag = float(imag)

    def __repr__(self):
        if self.imag < 0:
            return '%.2f-%.2fi' % (self.real, abs(self.imag))
        else:
            return '%.2f+%.2fi' % (self.real, self.imag)
    
    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        if i < 0:
            return '%.2f-%.2fi' % (r, abs(i))
        else:
            return '%.2f+%.2fi' % (r, i)
        
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        if i < 0:
            return '%.2f-%.2fi' % (r, abs(i))
        else:
            return '%.2f+%.2fi' % (r, i)
    
    def __mul__(self, other):
        f = self.real * other.real
        o = self.real * other.imag
        i = self.imag * other.real
        l = self.imag * other.imag
        im = o + i
        if l < 0:
            r = f + abs(l)
        else:
            r = f - abs(l)
        if im < 0:
            return '%.2f-%.2fi' % (r, abs(im))
        else:
            return '%.2f+%.2fi' % (r, im)
        
    def __div__(self, other):
        conjr = other.real
        conji = -other.imag
        conj = Complex(conjr,conji)
        f1 = self.real * conj.real
        o1 = self.real * conj.imag
        i1 = self.imag * conj.real
        l1 = self.imag * conj.imag
        im1 = o1 + i1
        if l1 < 0:
            r1 = f1 + abs(l1)
        else:
            r1 = f1 - abs(l1)
        
        
        f2 = other.real * conj.real
        o2 = other.real * conj.imag
        i2 = other.imag * conj.real
        l2 = other.imag * conj.imag
        im2 = o2 + i2
        if l2 < 0:
            r2 = f2 + abs(l2)
        else:
            r2 = f2 - abs(l2)
        denominator = r2 + im2
        r3 = r1/denominator
        im3 = im1/denominator
        if im3 < 0:
            return '%.2f-%.2fi' % (r3, abs(im3))
        else:
            return '%.2f+%.2fi' % (r3, im3)
       
    def mod(self):
        z = (self.real**2 + self.imag**2)**0.5
        im = 0.00
        return '%.2f+%.2fi' % (z, im)

r,i = map(float,raw_input().split())
C = Complex(r,i)
r,i = map(float,raw_input().split())
D = Complex(r,i)

print C + D
print C - D
print C * D
print C / D 
print C.mod()
print D.mod()