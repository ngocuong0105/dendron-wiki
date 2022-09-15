# not the same questions as in the book.
# this one is from Leetcode and has API for isBadVersion function.
class Solution:
    def firstBadVersion(self, n):
        def isBadVersion():
            pass

        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        mid = (left + right) // 2
        while left < right:
            if isBadVersion(mid):
                right = mid
                mid = (left + right) // 2
            else:
                left = mid + 1
                mid = (left + right) // 2
        return left
