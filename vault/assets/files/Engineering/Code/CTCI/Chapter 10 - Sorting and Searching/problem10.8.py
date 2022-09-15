# Find duplicate in linear time constant space
def findDuplicate(nums: list[int]) -> int:
    n = len(nums)
    for num in nums:
        nums[num] += n
    for i in range(len(nums)):
        if nums[i] // n > 1:
            return i
