---
id: r9lucaraliyqanyxqrsetzu
title: Sorting
desc: ''
updated: 1759502888201
created: 1677661832177
---

- [leetcode](https://leetcode.com/problems/sort-an-array/)

```python
'''
Insertion Sort, inplace O(n^2)
get the min, swap place
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_idx = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i],nums[min_idx] = nums[min_idx],nums[i]
        return nums

'''
Bubble Sort - Inplace O(n^2)
keep nums[:j] sorted
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while i and nums[i] < nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
                i -= 1
        return nums

'''
Merge Sort O(nlogn)
sort(nums[:mid]) sort(nums[mid:])
merge()
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) == 1: return nums
            mid = len(nums)//2
            left, right = merge_sort(nums[:mid]), merge_sort(nums[mid:])
            merged = []
            i,j = 0,0
            while i<len(left) or j<len(right):
                l = left[i] if i < len(left) else float('inf')
                r = right[j] if j < len(right) else float('inf')
                if l < r:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            return merged
        
        return merge_sort(nums)


'''
Quick Sort
pivot + merge
worse case is O(n^2), every time we hit a bad split (imbalnces, 1 vs n-1)
average case is O(nlogn). Intuiton bad splits and good splits cancel each other. Draw a tree with depth 2 one bad and one good split. the sized of your remaining arrays is like you had 1 good split.

good split is when it is balanced


O(n^2) worst case reached when array is decreasing or all elements are eqaul
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(l,r):
            pivot = nums[r]
            i = l-1
            for j in range(l,r):
                if nums[j] < pivot:
                    i += 1
                    nums[j],nums[i] = nums[i],nums[j]
            nums[i+1],nums[r] = nums[r],nums[i+1]
            return i+1

        def quick_sort(l,r):
            if l >= r: return
            q = partition(l,r)
            quick_sort(l,q-1)
            quick_sort(q+1,r)

        quick_sort(0,len(nums)-1)
        return nums

'''
Randomised Quick Sort
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(l,r):
            
            idx = random.randint(l,r)
            # randomized
            nums[idx],nums[r] = nums[r],nums[idx]
            pivot = nums[idx]
            i = l-1
            for j in range(l,r):
                #fix the case when there are many equal numbers, want to have more balanced split
                if random.randint(1,2) ==  1:
                    if nums[j] < pivot:
                        i += 1
                        nums[i],nums[j] = nums[j],nums[i]
                else:
                    if nums[j] <= pivot:
                        i += 1
                        nums[i],nums[j] = nums[j],nums[i]

                
            nums[i+1],nums[r] = nums[r],nums[i+1]
            return i+1

        def quick_sort(l,r):
            if l >= r: return
            q = partition(l,r)
            quick_sort(l,q-1)
            quick_sort(q+1,r)
        
        quick_sort(0,len(nums)-1)
        return nums

```

Comparative vs non-comparative sorting algorithms

# Quick Sort

In-place quick sort. Expected time complexity $O(nlogn)$, worse case $O(n^2)$.
```python
def quick_sort(s,e):
    if s>e: return
    idx = random.randint(s,e)
    nums[idx],nums[e] = nums[e],nums[idx]
    x,i = nums[e],s-1
    for j in range(s,e):
        if nums[j] <= x:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
    nums[i+1],nums[e] = nums[e],nums[i+1]
    quick_sort(s,i)
    quick_sort(i+2,e)
```


# Count Sort

