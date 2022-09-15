from ast import List

# https://leetcode.com/problems/range-sum-query-mutable/
class NumArray:
    """
    Binary tree index implementation = Fenwick tree
    The Fenwick tree achieves a much better balance between two operations: element update and prefix sum calculation
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = [0] * (len(nums) + 1)
        for i in range(1, len(self.bit)):
            self.bit[i] += nums[i - 1]
            if i + (i & -i) < len(self.bit):
                self.bit[i + (i & -i)] += self.bit[i]

    def query(self, i):
        """
        Find sum of first i numbers in self.nums
        """
        res = 0
        j = i + 1
        while j > 0:
            res += self.bit[j]
            j -= j & -j
        return res

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index < len(self.bit):
            self.bit[index] += diff
            index += index & -index

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)



    def sqrt(x):
        return x**0.5

    sqrt(16) # 4.0


