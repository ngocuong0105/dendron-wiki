# 16.16
#  https://leetcode.com/problems/shortest-unsorted-continuous-subarray/submissions/
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        minn, maxx = [nums[-1]], [nums[0]]
        for num in nums[1:]:
            maxx.append(max(num, maxx[-1]))
        for num in nums[::-1][1:]:
            minn.append(min(num, minn[-1]))
        minn.reverse()
        idx, idx1 = None, None
        for i in range(len(nums)):
            if idx == None and nums[i] > minn[i]:
                idx = i
            if nums[i] < maxx[i]:
                idx1 = i
        if idx != None and idx1 != None:
            return idx1 - idx + 1
        return 0
