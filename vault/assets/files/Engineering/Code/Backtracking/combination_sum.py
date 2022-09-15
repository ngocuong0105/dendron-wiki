# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(path, curr, last):
            if curr >= target:
                if curr == target:
                    res.append(path)
                return
            for i in range(last, len(candidates)):
                can = candidates[i]
                backtrack(path + [can], curr + can, i)

        res = []
        backtrack([], 0, 0)
        return res
