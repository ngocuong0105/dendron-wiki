# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(path, curr):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            for char in d[digits[curr]]:
                backtrack(path + [char], curr + 1)

        res = []
        if digits == "":
            return res
        backtrack([], 0)
        return res
