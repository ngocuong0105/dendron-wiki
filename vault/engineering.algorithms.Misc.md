---
id: 62fr2x24gm8h0m2x4c3r862
title: Misc
desc: ''
updated: 1664724269692
created: 1664382870554
---
# Sequences

## Binary Search
- template for finding smallest element $i$ in array such that `func(i)` is `True`
```Python
def bs(i,j,func):
    while i < j:
        mid = i+j >> 1
        if func(mid):
            j = mid
        else:
            i = mid + 1
    return i
```

- 2D problems often treat columns/rows as elements. E.g each column is element and we do binary search on columns $O(m*logn)$
    - [black pixels](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/)
    - [peak element](https://leetcode.com/problems/find-a-peak-element-ii/)

## RMQ task (Range Minimum Query - the smallest element in an interval)
## Longest increasing subsequence
## Maximum/minimum subarray sum
- [leetcode](https://leetcode.com/problems/maximum-subarray/)

**Solution 1.**
- goal find `nums[l:r+1]` with max sum
- use cumulative sums `nums[l:r+1] = cum[r]-cum[l-1]`
- redefined goal for each $r$ find $l$ which maximizes `sum(nums[l:r+1])`
- compute $cum[r]$ as we go, and maintain minimum possible value for $cum[l-1]$

```Python
def maxSubArray(nums: List[int]) -> int:
    res,min_sum,sm = -float('inf'),0,0
    for r in range(len(nums)):
        sm += nums[r]
        res = max(res,sm-min_sum)
        min_sum = min(min_sum,sm)
    return res
```

**Solution 2.**
- Kadane algo
- compute partial/cumulative sum `sm` as we go. If negative rest to 0
- our maximum subarray must start at a critical point when $sm < 0$

```Python
def maxSubArray(nums: List[int]) -> int:
    res,curr = -float('inf'),0
    for num in nums:
        curr += num
        res = max(res,curr)
        curr = max(curr,0)
    return res
```

#QED


## K-th order statistic in O(N)
# Game Theory
## Games on arbitrary graphs
## Sprague-Grundy theorem. Nim
# Schedules
## Scheduling jobs on one machine
## Scheduling jobs on two machines
## Optimal schedule of jobs given their deadlines and durations
# Miscellaneous
## Josephus problem
## 15 Puzzle Game: Existence Of The Solution
## The Stern-Brocot Tree and Farey Sequences

## Rotate image

- rotate image, [p1](https://leetcode.com/problems/rotate-image/)
- 90 degree rotation = flip + transpose
```Python
def rotate(matrix):
    matrix.reverse()
    return list(zip(*matrix))

def rotate_inplace(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
```

## Longest valid parenthesis
- [leetcode](https://leetcode.com/problems/longest-valid-parentheses/)

```Python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def compute(ch,s):
            bal,res,curr = 0,0,0
            for p in s:
                bal += (p == ch)
                bal -= (p != ch)
                curr += 2*(p == ch)
                if bal == 0: 
                    res = max(res,curr)
                elif bal<0:
                    curr,bal = 0,0
            return res
        return max(compute('(',s),compute(')',s[::-1]))
```

