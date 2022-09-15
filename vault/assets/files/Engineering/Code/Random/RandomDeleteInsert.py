import collections
import random


class RandomizedCollection:
    """
    https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/submissions/
    """

    def __init__(self):
        self.d = collections.defaultdict(set)
        self.nums = []

    def insert(self, val: int) -> bool:
        if len(self.d.get(val, set())) == 0:
            res = True
        else:
            res = False
        self.d[val].add(len(self.nums))
        self.nums.append(val)
        return res

    def remove(self, val: int) -> bool:
        if len(self.d.get(val, set())) == 0:
            return False
        else:
            res = True
        last_el = self.nums[-1]
        val_idx = next(iter(self.d[val]))  # nice way t access in O(1) element in a set
        self.d[last_el].add(val_idx)
        self.nums[-1] = val
        self.nums[val_idx] = last_el
        self.nums.pop()
        self.d[last_el].remove(len(self.nums))

        if val != last_el:
            self.d[val].remove(val_idx)
        return res

    def getRandom(self) -> int:
        """
        random.choice does not support for unordered sets
        """
        return random.choice(self.nums)


#%%
# another solution slower but does not use defaultdict(set)
class RandomizedCollection:
    def __init__(self):
        self.numbers = []
        self.map = collections.defaultdict(list)

    def insert(self, val: int) -> bool:
        res = False if val in self.map else True
        self.map[val].append(len(self.numbers))
        self.numbers.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = False if val not in self.map else True
        if res:
            idx = self.map[val].pop()
            if idx != len(self.numbers) - 1:
                self.map[self.numbers[-1]].pop()
                self.map[self.numbers[-1]].append(idx)
                self.map[self.numbers[-1]].sort()
            self.numbers[idx], self.numbers[-1] = self.numbers[-1], self.numbers[idx]
            self.numbers.pop()
            if len(self.map[val]) == 0:
                del self.map[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numbers)
