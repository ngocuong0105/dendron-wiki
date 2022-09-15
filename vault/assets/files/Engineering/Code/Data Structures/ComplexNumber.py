import math

class ComplexNumber:
    def __init__(self, val1, val2, representation='rect'):
        if representation == "rect":
            self.real = val1
            self.imaginary = val2
            self.mag = math.sqrt(val1**2+val2**2)
            self.angle = math.atan(val2/val1)
        elif representation == 'polar':
            self.mag = val1
            self.angle = val2
            self.real = val1*math.cos(val2)
            self.imaginary = val1*math.sin(val2)
        else:
            raise ValueError("Invalid representation")

    def __str__(self):
        if self.imaginary == 0:
            return str(self.real)
        elif self.real == 0:
            return str(self.imaginary)+"i"
        elif self.imaginary > 0:
            return str(self.real)+"+"+str(self.imaginary)+"i"
        else:
            return str(self.real)+str(self.imaginary)+"i"

    def __repr__(self) -> str:
        return str(self)

    def __add__(self,other):
        return ComplexNumber(self.real+other.real,self.imaginary+other.imaginary)

    def __sub__(self,other):
        return ComplexNumber(self.real-other.real,self.imaginary-other.imaginary)

    def __mul__(self,other):
        return ComplexNumber(self.mag*other.mag,self.angle+other.angle,representation='polar')

    def __divide__(self,other):
        return ComplexNumber(self.mag/other.mag,self.angle-other.angle,representation='polar')

    def __abs__(self):
        return self.mag

    def __eq__(self,other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self,other):
        return self.real != other.real or self.imaginary != other.imaginary

    def __gt__(self,other):
        return self.mag > other.mag

    def __ge__(self,other):
        return self.mag >= other.mag

    def __lt__(self,other):
        return self.mag < other.mag

    def __le__(self,other):
        return self.mag <= other.mag

    def __neg__(self):
        return ComplexNumber(self.real,self.imaginary*-1)

    def __pos__(self):
        return ComplexNumber(self.real,self.imaginary)

    def __invert__(self):
        return ComplexNumber(self.mag,self.angle+math.pi,representation='polar')
