# Binary Search
# Assuming unique elements.
# Idea is simple but tricky to implement with/witout duplicates
def search(nums: list[int], target: int) -> int:
    begin, end = nums[0], nums[-1]
    left, right = 0, len(nums) - 1
    m = (left + right) // 2
    if begin < end:
        lower = None  # no rotation, do usual binary search
    else:
        lower = True  # should I look before or after rotation point
        if target <= end:
            lower = False
    while left < right:
        if nums[m] >= target:
            if lower != None and nums[m] >= begin and not lower:
                left = m + 1
                m = (left + right) // 2
            else:
                right = m
                m = (left + right) // 2
        else:
            if lower != None and nums[m] <= end and lower:
                right = m - 1
                m = (left + right) // 2
            else:
                left = m + 1
                m = (left + right) // 2
    return left if nums[left] == target else -1
