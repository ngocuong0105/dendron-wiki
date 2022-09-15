#%%
import math


class Fraction:
    def __init__(self, num=0, den=1):
        g = math.gcd(num, den)
        self.num, self.den = num // g, den // g

    __add__ = lambda self, other: Fraction(
        self.num * other.den + other.num * self.den, self.den * other.den
    )
    __sub__ = lambda self, other: Fraction(
        self.num * other.den - other.num * self.den, self.den * other.den
    )
    __mul__ = lambda self, other: Fraction(self.num * other.num, self.den * other.den)
    __truediv__ = lambda self, other: Fraction(
        self.num * other.den, self.den * other.num
    )
    __floordiv__ = lambda self, other: (self.num * other.den) // (self.den * other.num)

    __pow__ = lambda self, other: Fraction(self.num ** other, self.den ** other)
    __abs__ = lambda self: self if self.num >= 0 else Fraction(-self.num, self.den)
    __neg__ = lambda self: Fraction(-self.num, self.den)
    __round__ = lambda self, ndigits: round(self.num / self.den, ndigits)

    __bool__ = lambda self: bool(self.num)
    __int__ = lambda self: self.num // self.den
    __float__ = lambda self: self.num / self.den
    __str__ = lambda self: "({}, {})".format(self.num, self.den)

    __copy__ = lambda self: Fraction(self.num, self.den)
    __hash__ = lambda self: hash((self.num, self.den))

    __eq__ = lambda self, other: self.num * other.den == other.num * self.den
    __ne__ = lambda self, other: self.num * other.den != other.num * self.den
    __lt__ = lambda self, other: self.num * other.den < other.num * self.den
    __gt__ = lambda self, other: self.num * other.den > other.num * self.den
    __le__ = lambda self, other: self.num * other.den <= other.num * self.den
    __ge__ = lambda self, other: self.num * other.den >= other.num * self.den

    __repr__ = lambda self: "Fraction({}, {})".format(self.num, self.den)


# %%
f = Fraction(2, 3)
# %%
