---
id: r9lucaraliyqanyxqrsetzu
title: Sorting
desc: ''
updated: 1759579417801
created: 1677661832177
---

- [leetcode](https://leetcode.com/problems/sort-an-array/)


Comparison sort algorithms determine the order of elements based on pairwise comparison between elements. Insertion sort, bubble sort, quick sort, and merge sort are all examples of comparison sort algorithms.


Count, bucket, radix sort are examples of non-comparison sort algorithms. They do not compare elements directly but instead use the properties of the elements (like their range or digits) to sort them.

# Quick Sort
- Expected time complexity $O(nlogn)$, worse case $O(n^2)$.

# Merge Sort
- Time complexity $O(nlogn)$ - always


# Examples

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
            i = l
            for j in range(l,r):
                if nums[j] < pivot:
                    nums[j],nums[i] = nums[i],nums[j]
                    i += 1
            nums[i],nums[r] = nums[r],nums[i]
            return i

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
            i = l-1 # weird implementation see above. This one comes from the Intro to Algo book, but mine is a bit clearer
            for j in range(l,r):
                #fix the case when there are many equal numbers, want to have more balanced split
                if j%2:
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
            if l >= r: return None
            q = partition(l,r)
            quick_sort(l,q-1)
            quick_sort(q+1,r)
        
        quick_sort(0,len(nums)-1)
        return nums

"""
Quick Sort - not implace but easy to remember
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums):
            if len(nums) <= 1: return nums
            pivot = nums[random.randint(0,len(nums)-1)]
            smaller, equal, greater = [],[],[]
            for num in nums:
                if num < pivot: smaller.append(num)
                elif num > pivot: greater.append(num)
                else: equal.append(num)

            return quick_sort(smaller) + equal + quick_sort(greater)

        return quick_sort(nums)
```

Comparative vs non-comparative sorting algorithms



# Count Sort
- $O(n+k)$ where all numbers in nums are in the range (0,k)
- count array such that arr[i] is the count of element i

# Bucket Sort
- put numbers in buckets, sort each bucket using comparison sort (usually insertion), as buckets are relatively small




# K-th order statistic

## Quick Select

- [leetcode](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- Expected run time $O(n)$. Note it is as if we search for min and max. The reason for this is because unlike in quick_sort where we solve both branches of subproblems here we solve only the branch that contains the k-th order statistic element.


```python

# Quick Select (Not sure if it is called like this). Could be called Merge Sort Select?
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums,k):
            pivot = nums[random.randint(0,len(nums)-1)]
            smaller,equal,greater = [],[],[]
            for i in range(len(nums)):
                if nums[i] < pivot:
                    smaller.append(nums[i])
                elif nums[i] == pivot:
                    equal.append(nums[i])
                else:
                    greater.append(nums[i])
            if len(smaller)+len(equal) < k:
                return quick_select(greater,k-len(smaller)-len(equal))
            elif len(smaller) >= k:
                return quick_select(smaller,k)
            return pivot

        nums = [-num for num in nums]
        return -quick_select(nums,k)

# Quick Select, but no xtra memory
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l,r):
            idx = random.randint(l,r)
            pivot = nums[r]
            nums[idx],nums[r] = nums[idx],nums[r]
            i = l-1
            for j in range(l,r):
                if j %2:
                    if nums[j] < pivot:
                        i += 1
                        nums[i],nums[j] = nums[j],nums[i]
                else:
                    if nums[j] <= pivot:
                        i += 1
                        nums[i],nums[j] = nums[j],nums[i]

            nums[i+1],nums[r] = nums[r],nums[i+1]
            return i+1

        def quick_select(l,r,k):
            if l == r: return nums[l]
            q = partition(l,r)
            # q is index between l,r
            # k is count!, it is the first element in array[l:r+1]
            # q-l+1 becomes a count
            if q-l+1 == k: return nums[q]
            if k < q-l+1:
                return quick_select(l,q-1,k)
            else:
                return quick_select(q+1,r,k-(q-l+1)) # WTF

        nums = [-num for num in nums]
        return -quick_select(0,len(nums)-1,k)

```