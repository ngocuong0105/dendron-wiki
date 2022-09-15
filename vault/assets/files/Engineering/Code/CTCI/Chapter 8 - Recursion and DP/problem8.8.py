import collections


def permuteUnique(nums: list[int]) -> list[list[int]]:
    def backtrack(path, nums):
        if len(path) == n:
            res.append(path)
            return
        for key in nums:
            if nums[key] > 0:
                nums[key] -= 1
                backtrack(path + [key], nums)
                nums[key] += 1

    n = len(nums)
    nums = collections.Counter(nums)
    res = []
    backtrack([], nums)
    return res
