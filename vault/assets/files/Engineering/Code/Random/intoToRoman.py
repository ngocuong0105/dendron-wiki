# https://leetcode.com/problems/integer-to-roman/submissions/
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }
        res = []
        for n, roman in sorted(list(d.items()), reverse=True):
            res.append((num // n) * roman)
            num %= n
        return "".join(res)
