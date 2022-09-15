# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/
class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        i, j = self.bs(nums, target - 0.1), self.bs(nums, target + 0.1)
        return j - i > len(nums) // 2

    def bs(self, nums, t):
        l, r = 0, len(nums)
        m = (l + r) // 2
        while l < r:
            if nums[m] > t:
                r = m
                m = (l + r) // 2
            else:
                l = m + 1
                m = (l + r) // 2
        return l
