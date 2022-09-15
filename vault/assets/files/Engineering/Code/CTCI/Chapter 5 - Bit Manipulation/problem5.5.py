def isPowTwo(num: int) -> bool:
    return num & (num - 1) == 0


isPowTwo(2147483648)
