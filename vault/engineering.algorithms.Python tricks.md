---
id: x0cxhdz6m217jsrqw2pcwuk
title: Python tricks
desc: ''
updated: 1668105065439
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

- adjacency list
```Python
from collections import defaultdict
adj = defaultdict(list) # default dict takes a function
for u,v in edges:
    adf[u].append(v)

```

- Counter
```Python
# Counter dict
from collections import Counter
arr = [1,2,3,1,2,4,4,2]
c = Counter(arr)
c.most_common() # returns tuple of all elements and counts in sorted order
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

- xor cumulative
```python
xor_cum = [0] + list(accumulate(arr,lambda x,y:x^y))
def f(l,r):
    '''returns xor subarray arr[l]^arr[l+1]^...^arr[r]'''
    xor_cum[r+1]^xor_cum[l]
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

- python does not have tail [recursion](https://stackoverflow.com/questions/13591970/does-python-optimize-tail-recursion) (unlike Lisp)

- get groups, groupby

```Python
from itertools import groupby
s = 'aaabbddca'
groups = [(ch,len(list(g))) for ch,g in groupby(s)] # [(a,3),(b,2),(d,2),(c,1),(a,1)]
```

- concurrent, multithreaded programming, [web crawler](https://leetcode.com/problems/web-crawler-multithreaded/)
```Python
# simple DFS
class Solution:
    def crawl(self, start: str, parser: 'HtmlParser') -> List[str]:
        hostname = lambda x: x.split('/')[2]
        visited,stack= set([start]),[start]
        while stack:
            s = stack.pop()
            for u in parser.getUrls(s):
                if u not in visited and hostname(start) == hostname(u):
                    visited.add(u)
                    stack.append(u)
        return visited

# concurrent DFS
from concurrent import futures
class Solution:
    def crawl(self, s: str, parser: 'HtmlParser') -> List[str]:
        hostname = lambda x: x.split('/')[2]
        visited = set([s])
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = [executor.submit(parser.getUrls, s)]
            while tasks:
                neigh = tasks.pop().result()
                for u in neigh:
                    if u not in visited and hostname(s) == hostname(u):
                        visited.add(u)
                        tasks.append(executor.submit(parser.getUrls, u))
        return visited
```

- string operations/methods
```Python
char.islower()
char.isupper()
char.lower()
char.upper()
ch.isnumeric() # is an integer
ch.isalpha() # is a character
```

- permutations
```python
from itertools import permutations
nums = [2,1,3,5]
for p in permutations(nums):
    print(p)
```