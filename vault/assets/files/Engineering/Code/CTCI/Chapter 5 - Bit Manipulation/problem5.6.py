def conversion(a: int, b: int) -> int:
    diff = a ^ b
    res = 0
    while diff > 0:
        res += diff & 1
        diff >>= 1
    return res


conversion(29, 15)
