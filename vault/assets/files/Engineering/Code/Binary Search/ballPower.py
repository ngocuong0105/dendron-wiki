# https://leetcode.com/problems/magnetic-force-between-two-balls/submissions/
class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        n = len(position)
        position.sort()

        def count(d):
            res = 1
            curr = position[0]
            for i in range(1, n):
                if position[i] - d >= curr:
                    res += 1
                    curr = position[i]
            return res

        l, r = 0, max(position) - min(position)
        while l < r:
            d = (l + r + 1) // 2
            # without the +1 will be stuck in infinite loop
            # if the mid point d==l and count(d)>=m forever
            # Rule of thumb: use m = l + (r-l)//2 with l = m + 1 and r = m,
            # and use m = r - (r-l)//2 with l = m and r = m - 1
            if count(d) >= m:
                l = d
            else:
                r = d - 1
        return l
