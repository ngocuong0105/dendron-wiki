# contest question - hard 2141
class Solution:
    def maxRunTime(self, n, B):
        B = sorted(B)[::-1]
        small = sum(B[n:])

        beg, end = 0, sum(B) + 1
        while beg + 1 < end:
            mid = (beg + end) // 2
            to_do = sum(max(mid - x, 0) for x in B[:n])
            if to_do > small:
                end = mid
            else:
                beg = mid

        return beg
