import collections

# two pass
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        d = collections.Counter(nums)
        res = 0
        for key in d:
            res += min(d.get(k - key, 0), d[key])
        return res // 2


# one pass
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        d = collections.defaultdict(int)
        res = 0
        for num in nums:
            if d[k - num] > 0:
                d[k - num] -= 1
                res += 1
            else:
                d[num] += 1
        return res
