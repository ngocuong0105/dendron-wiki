#%%
class Binary:

    """
    This is a class for basic manipulation methods for bits.
    Arguments: Integer in base 10
    Returns:
    binary representation;
    get, set, clear, update specific bits;
    count number of bits;
    least significant bit;
    """

    def __init__(self, num: int):
        self.decimal = num

    # binary representation
    def __str__(self) -> str:
        res = []
        num = self.decimal
        while num > 0:
            res.append(str(num % 2))
            num //= 2
        return f"{self.decimal} has binary representation {''.join(res[::-1])}"

    def __repr__(self) -> str:
        res = []
        num = self.decimal
        while num > 0:
            res.append(str(num % 2))
            num //= 2
        return "".join(res[::-1])

    # get bit
    def get(self, i: int) -> int:
        msk = 1 << i
        if self.decimal & msk != 0:
            return 1
        return 0

    # set bit
    def set(self, i: int) -> int:
        msk = 1 << i
        self.num = self.decimal | msk
        return self.decimal

    # clear specific bit i
    def clear(self, i: int) -> int:
        msk = ~(1 << i)  # ~ reverses bits, 0 -> 1 and 1 -> 0
        self.decimal = self.decimal & msk
        return self.decimal

    # clear all bits from beginning to bit i
    def clearFirstBits(self, i: int) -> int:
        msk = (1 << i) - 1
        self.decimal = self.decimal & msk
        return self.decimal

    # clear all bits from end to bit i
    def clearEndBits(self, i: int) -> int:
        msk = -1 << (i + 1)  # not -1 is 11111..1
        self.decimal = self.decimal & msk
        return self.decimal

    # update bit i to value val
    def update(self, i: int, val: bool) -> int:
        msk = ~(1 << i) | (val << i)
        self.decimal = self.decimal & msk
        return self.decimal

    # returns number of bits
    def countBits(self) -> int:
        res = 0
        while self.decimal > 0:
            # res+=self.decimal%2
            res += self.decimal & 1
            self.decimal >>= 1
        return res

    # least significant bit
    def lsb(self) -> int:
        # negative numbers are represented as two's complement
        # two's complement = one's complement + 1
        return self.decimal & -self.decimal


# %%
