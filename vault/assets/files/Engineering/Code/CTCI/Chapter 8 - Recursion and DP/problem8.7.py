def permute(nums: list[int]) -> list[list[int]]:
    def backtrack(path, nums):
        if len(path) == n:
            res.append(path)
        for num in nums:
            backtrack(path + [num], nums - {num})

    res = []
    n = len(nums)
    backtrack([], set(nums))
    return res
