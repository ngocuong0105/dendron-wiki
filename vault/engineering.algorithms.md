---
id: 7m3gais9ll8mlmzqlw08s7g
title: Algorithms
desc: ''
updated: 1663361054630
created: 1658766702063
---

Should add some tricky algos/data structures here.

**Buzz words**
BIT, Red Black Trees, Segment Trees, A* Search, Dijkstra, Kruskal, Prim algo, Trie. String algorithms KMP, State machines. Prime numbers algos, Sieve of Eratosthenes, union find, Morris Traversal [inorder](https://leetcode.com/problems/binary-tree-inorder-traversal/), Palindrome algo, Manacher, Combinations, Permutations mart ways to get (yield) + no duplicated calls, BFS, DFS
[TSP](https://leetcode.com/problems/find-the-shortest-superstring/)

See dbabichev link for [patterns](https://flykiller.github.io/coding%20ideas/).

# The Pythonic Way

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

# Algos

- , [p1](https://leetcode.com/problems/longest-palindromic-substring/), [p2](https://leetcode.com/problems/shortest-palindrome/)
```Python
# O(n**2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palin(i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        res = ''
        for i in range(len(s)):
            odd = palin(i,i)
            even = palin(i,i+1)
            if len(res)<len(odd): res = odd
            if len(res)<len(even): res = even
        return res

# Manacher Algorithm. Find Longest Palindrome in O(n) time.
class Solution:
    def longestPalindrome(self, s: str) -> str:  
        T = '$#'+'#'.join(s)+'#&'
        P = [0]*len(T)
        C,R = 0,0
        for i in range(len(T)-1):
            P[i] = (R>i) and min(R-i,P[2*C-i])
            while T[i+P[i]+1] == T[i-P[i]-1]:
                P[i] += 1
            if R < i+P[i]:
                C,R = i,i+P[i]
        l = max(P)
        i = P.index(l)
        return s[(i-l)//2:(i+l)//2]

```

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


- guess the algo, [p1](https://leetcode.com/problems/shortest-path-with-alternating-colors/)

- BFS with smart states [p1](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)

- sliding window with augmented/additional data structure heap + queue, [p1](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)

- monotonic queue, [p1](https://leetcode.com/problems/constrained-subsequence-sum/)

```python

class Monoqueue(collections.deque):
    def enqueue(self, val):
        count = 1 # counts the number of elements which value is greater or equal than
        while self and self[-1][0] < val:
            count += self.pop()[1]
        self.append([val, count])

    def dequeue(self):
        ans = self.max()
        self[0][1] == 1
        if self[0][1] =S= 0:
            self.popleft()
        return ans

    def max(self):
        return self[0][0] if self else 0
```

- kth element in sorted matrix [p](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/), check
[paper](https://github.com/ngocuong0105/dendron-wiki/blob/main/vault/assets/files/Engineering/X%2BY.pdf)

- Most Recently Used Queue [p](https://leetcode.com/problems/design-most-recently-used-queue/)

```Python
# O(nlogn) initialization, O(logn) fetch
from sortedcontainers import SortedList

class MRUQueue:

    def __init__(self, n: int):
        self.ls = SortedList([(i-1,i) for i in range(1,n+1)])
        self.rank = n
        
    def fetch(self, k: int) -> int:
        res = self.ls.pop(k-1)
        res = res[1]
        self.ls.add((self.rank,res))
        self.rank += 1
        return res


# BIT solutions are hard to come up with?
class BIT:
    
    def __init__(self, n) -> None:
        self.bit = [0]*(n+1)

    def add(self, index, delta) -> None:
        index += 1
        while index < len(self.bit):
            self.bit[index] += delta
            index += index & -index
        
    def query(self, index) -> int:
        res = 0
        while index:
            res += self.bit[index]
            index -= index & -index
        return res

# O(NlogN) initialization, O(log^2n)fetch
class MRUQueue:

    def __init__(self, n: int):
        self.bit = BIT(n+2000)
        self.vals = [0]*(n+2000)
        for i in range(n):
            self.vals[i] = i+1
            self.bit.add(i,1)
        self.size = n
    
    # O(log^2n)
    def fetch(self, k: int) -> int:
        l,r = 1, self.size
        while l<r:
            m = l+r >> 1 
            if self.bit.query(m) >= k:
                r = m
            else:
                l = m+1
        self.bit.add(l-1, -1)
        self.bit.add(self.size, 1)
        self.vals[self.size] = self.vals[l-1]
        self.size += 1
        return self.vals[l-1]
    
# Square root decomposition technique - O(n) init, O(sqrt(n)) fetch
class MRUQueue:

    def __init__(self, n: int):
        self.buckets = []
        self.indecies = []
        self.n = n
        self.nn = int(n**0.5)
        for i in range(1,n+1):
            ii = (i-1)//self.nn
            if ii == len(self.buckets):
                self.indecies.append(i)
                self.buckets.append([])
            self.buckets[-1].append(i)
            
    def fetch(self, k: int) -> int:
        i = self._bs(self.indecies, k)-1
        res = self.buckets[i].pop(k-self.indecies[i])
        for ii in range(i+1,len(self.indecies)):
            self.indecies[ii] -= 1
            
        if len(self.buckets[-1]) >= self.nn:
            self.buckets.append([])
            self.indecies.append(self.n)
        self.buckets[-1].append(res)
        
        if not self.buckets[i]:
            self.buckets.pop(i)
            self.indecies.pop(i)
            
        return res
        
    def _bs(self, nums, num):
        l,r = 1,len(nums)
        while l<r:
            m = l+r>>1
            if nums[m] > num:
                r = m
            else:
                l = m+1
        return l
```

