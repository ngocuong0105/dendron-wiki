---
id: r9lucaraliyqanyxqrsetzu
title: Sorting
desc: ''
updated: 1677661975588
created: 1677661832177
---

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