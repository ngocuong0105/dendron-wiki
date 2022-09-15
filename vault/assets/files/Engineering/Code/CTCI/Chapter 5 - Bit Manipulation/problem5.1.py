def bitInsert(n: int, m: int, i: int, j: int) -> int:
    # create mask to clear all bits between i and j for n
    # that we want msk=1110000111 (zeros are between i and j)
    msk = 1 << (j - i + 2)
    msk -= 1
    msk <<= i
    msk = ~msk
    n = n & msk
    # shift m
    m <<= i
    return n | m
