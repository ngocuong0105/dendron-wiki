# https://leetcode.com/problems/minimize-deviation-in-array/

# DFS traversing all paths
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        def dfs(i, maxx, minn):
            nonlocal res
            if i == len(nums):
                res = min(maxx - minn, res)
                return
            for s in states[i]:
                dfs(i + 1, max(maxx, s), min(minn, s))

        states = []
        for num in nums:
            if num % 2:
                s = [num, num * 2]
            else:
                s = []
                while num % 2 == 0:
                    s.append(num)
                    num //= 2
                s.append(num)
            states.append(s)
        res = float("inf")
        dfs(0, -float("inf"), float("inf"))
        return res


import heapq
from typing import List

# level by level in a smart way with a heap
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        h = []
        for num in nums:
            tmp = num
            while tmp % 2 == 0:
                tmp //= 2
            heapq.heappush(h, (tmp, max(num, tmp * 2)))
        maxx = max([num for num, _ in h])
        res = float("inf")
        while len(h) == len(nums):
            num, limit = heapq.heappop(h)
            res = min(res, abs(maxx - num))
            if num * 2 <= limit:
                maxx = max(num * 2, maxx)
                heapq.heappush(h, (num * 2, limit))
        return res
