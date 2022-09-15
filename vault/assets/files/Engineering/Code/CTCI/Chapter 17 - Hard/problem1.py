# going back to the fundamentals
while a & b != 0:
    a, b = a ^ b, (a & b) << 1
print(a | b)
