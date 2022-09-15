def flip(n: int) -> int:
    binary = []
    while n > 0:
        binary.append(n & 1)
        n >>= 1
    c = []
    binary.reverse()
    i = 0
    while i < len(binary):
        count = 0
        while i < len(binary) and binary[i] == 1:
            count += 1
            i += 1
        c.append((count, 1))
        count = 0
        while i < len(binary) and binary[i] == 0:
            count += 1
            i += 1
        c.append((count, 0))
    res = 0
    for i in range(1, len(c) - 1):
        if c[i][1] == 0 and c[i][0] == 1:
            res = max(res, c[i - 1][0] + c[i + 1][0] + 1)
        if c[i][1] == 0 and c[i][0] > 1:
            res = max(res, c[i - 1][0] + 1)
            res = max(res, c[i + 1][0] + 1)
    return res


#%%
flip(1775)
