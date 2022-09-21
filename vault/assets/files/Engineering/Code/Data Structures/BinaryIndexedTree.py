#%%
class BIT:
    """
    Binary Index Tree (Fenwick Tree)
    Initialization of tree -> O(n)
    Update -> O(logn)
    Query -> O(logn)
    """

    def __init__(self, nums):
        self.bit = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.bit[i] += nums[i - 1]
            if i + (i & -i) < len(nums):
                self.bit[i + (i & -i)] += self.bit[i]

    def update(self, i, val):
        """
        Adds val to self.nums[i]
        """
        while i < len(self.bit):
            self.bit[i] += val
            i += i & (i & -i)

    def query(self, i):
        """
        sum nums[:i+1]
        """
        res = 0
        i += 1
        while i:
            res += self.bit[i]
            i -= i & -i
        return res

bit = BIT([3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3])


# https://leetcode.com/problems/range-sum-query-mutable/

# https://leetcode.com/problems/range-sum-query-2d-mutable/