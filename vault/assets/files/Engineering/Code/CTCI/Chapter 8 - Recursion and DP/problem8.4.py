def powerSet(nums: list[int]) -> list[list]:
    def backtrack(curr, path):
        res.add(tuple(path))
        if curr < len(nums):
            backtrack(curr + 1, path + [nums[curr]])
            backtrack(curr + 1, path)

    res = set()
    backtrack(0, [])
    return [list(t) for t in res]


powerSet([1, 2, 3])
