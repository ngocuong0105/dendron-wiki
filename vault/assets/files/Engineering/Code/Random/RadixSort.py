def get_digits(num):
    return [int(s) for s in str(num)]

def to_num(digits):
    return int(''.join([str(d) for d in digits]))

def fitness(d1):
    return [len(d1)] + d1

def radix_sort(nums):
    digits = list(map(get_digits,nums))
    for i in range(len(nums)-1,-1,-1):
        digits.sort(key = fitness)
    return list(map(to_num,digits))

nums = [2,3,33,1,22,123,332,332]
print(radix_sort(nums))