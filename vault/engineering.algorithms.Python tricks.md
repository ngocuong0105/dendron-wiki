---
id: x0cxhdz6m217jsrqw2pcwuk
title: Python tricks
desc: ''
updated: 1666556290379
created: 1664446506779
---



```Python
# transpose with unzipping
mat = [(1,2,3),(4,5,6)]
transpose_mat = list(zip((*mat)))
```

```Python
# cumulative sum array, cdf
from itertools import accumulate
nums = [1,2,3,4]
cum = list(accumulate(nums)) # [1,3,6,10]
```

```Python
# flatten list
from itertools import chain
equations = [[1,2,3],[4,5]]
list(chain(*equations))

```

```Python
# count occurrences of element in list
ls = [1,2,3,1,1]
ls.count(1)
```

```Python
# adjacency list
from collections import defaultdict
adj = defaultdict(list) # default dict takes a function
for u,v in edges:
    adf[u].append(v)

```


```Python
# Counter dict
from collections import Counter
arr = [1,2,3,1,2,4,4,2]
c = Counter(arr)
```

- [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/), diagonals have constant values
```Python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]: return False
        return True
    
class Solution:
    def isToeplitzMatrix(self, m: List[List[int]]) -> bool:
        return all(m[i][j] == m[i+1][j+1] for i,j in product(range(len(m)-1),range(len(m[0])-1)))

class Solution:
    def isToeplitzMatrix(self, m: List[List[int]]) -> bool:
        return all(r1[:-1] == r2[1:] for r1,r2 in zip(m,m[1:]))

```

- check if two intervals overlap

```Python
# [a,b], [x,y]
def overlap(a,b,x,y):
    return a < y and x < b
```
- suffix and prefix sum
```python
from itertools import accumulate
suff = list(accumulate(nums[::-1]))[::-1]
pref = list(accumulate(nums))
```

- max with key, array of arrays, return array of max length
```Python
max(arrs, key = len) # gives array of maximul length
```

- custom comparator in sorting, sorted(), sort, key, compare
```Python
from functools import cmp_to_key
def compare(x, y):
     return x[0] - y[0]
 
data = [(4, None), (3, None), (2, None), (1, None)]
sorted(data, key=cmp_to_key(compare))
```