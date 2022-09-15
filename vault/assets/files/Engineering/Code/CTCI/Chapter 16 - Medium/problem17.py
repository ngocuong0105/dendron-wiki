# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = nums[0]
        res = nums[0]
        for num in nums[1:]:
            if dp > 0:
                dp += num
            else:
                dp = num
            res = max(dp, res)
        return res
