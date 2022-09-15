# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

from typing import List


class BIT:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        i += 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i:
            res += self.bit[i]
            i -= i & -i
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        mp = {e: i for i, e in enumerate(sorted(nums))}
        nums.reverse()
        ranks = [mp[e] for e in nums]
        res = []
        bit = BIT(len(nums))
        for r in ranks:
            res.append(bit.query(r - 1))
            bit.update(r, 1)
        res.reverse()
        return res
