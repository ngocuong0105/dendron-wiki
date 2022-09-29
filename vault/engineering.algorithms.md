---
id: 7m3gais9ll8mlmzqlw08s7g
title: Algorithms
desc: ''
updated: 1664446534151
created: 1658766702063
---

**Jivota e bolka i zadachi!**

Resources:
- [cp algos](https://cp-algorithms.com/)
- [dbabichev](https://flykiller.github.io/)
- [pyrival](https://github.com/ngocuong0105/PyRival)

#TODOs 
- add from dbabichev link for [patterns](https://flykiller.github.io/coding%20ideas/).
- add from pyrival
# Buzz words
BIT, AVL trees, B-trees (used in databses?), Red Black Trees, Segment Trees, A* Search, Dijkstra, Kruskal, Prim algo, Trie. String algorithms KMP, State machines. Prime numbers algos, Sieve of Eratosthenes, union find, Morris Traversal [inorder](https://leetcode.com/problems/binary-tree-inorder-traversal/), Palindrome algo, Manacher, Combinations, Permutations smart ways to get (yield) + no duplicated calls, BFS, DFS, [Fractional Cascading](https://en.wikipedia.org/wiki/Fractional_cascading)
[TSP](https://leetcode.com/problems/find-the-shortest-superstring/)


# Algos

- Manacher, [p1](https://leetcode.com/problems/longest-palindromic-substring/), [p2](https://leetcode.com/problems/shortest-palindrome/)
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

- monotonic queue, [p1](https://leetcode.com/problems/constrained-subsequence-sum/), the cnt variable below defines the enqueue priority, can have different priority implementations, e.g in max sliding window [problem](https://leetcode.com/problems/sliding-window-maximum/) it would be the index of the element

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

class MonoQueue(collections.deque):
    def enqueue(self,i,num): # enqueue dequeu depending on index value, useful when you need monotonic queue used as sliding window
        while self and self[-1][1] <= num:
            self.pop()
        self.append((i,num))
    def dequeue(self,i):
        if self and self[0][0] <= i:
            self.popleft()
    def max(self):
        if not self: return 0
        return self[0][1]
```

- kth element in sorted matrix [p](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/), #TODO check
[paper](https://github.com/ngocuong0105/dendron-wiki/blob/main/vault/assets/files/Engineering/X%2BY.pdf)

- order statistic tree, Red Black tree implementation I think
```
from sortedcontainers import SortedList
sl.add(num)
sl.bisect_left(num) # get order statistic
sl.remove(num)
```

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
        for i in range(n):BIT
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

- BIT, 1D, [problem](https://leetcode.com/problems/range-sum-query-mutable/)
- supports cumulutaive computations only on functions which have inverse like sum
- min function has limited support. cannot do min_range(i,j) and also whenever you do an update the new value should be smaller than the old one
- BIT needs functions which form a **group**, such as $\Z$ with operator + 
- $\Z$ and min form a semi-ring and that is not enough. 

- A Fenwick tree can support the following range operations:
    - Point Update and Range Query (classical one with implementation below)
    - Range Update and Point Query (initialize to 0-s, range update = update(l,x), update(r+1,-x), query(l) becomes a point query. Cumulative sum trick)
    - Range Update and Range Query [math trick using two BIT-s](https://cp-algorithms.com/data_structures/fenwick.html#2-range-update-and-point-query)



```python
class BIT:
    
    def __init__(self, nums):
        self.nums = nums
        self.bit = [0]*(len(nums)+1)
        for i in range(1,len(self.bit)):
            self.bit[i] += nums[i-1]
            if i + (i & -i) < len(self.bit):
                self.bit[i + (i & -i)] += self.bit[i]

    def update(self, i, val):
        diff = val-self.nums[i]
        self.nums[i] += diff
        i += 1
        while i < len(self.bit):
            self.bit[i] += diff
            i += (i & -i)

    def query(self, i):
        '''sum nums[:i+1] '''
        i += 1
        res = 0
        while i:
            res += self.bit[i]
            i -= (i & -i)
        return res

    def sum_range(self, l, r):
        return self.query(r) - self.query(l-1)
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.bit = BIT(nums)

    def update(self, i: int, val: int) -> None:
        self.bit.update(i,val)

    def sumRange(self, l: int, r: int) -> int:
        return self.bit.sum_range(l,r)

```

- BIT, Fenwick Tree, Binary Index Tree, 2D, [problem](https://leetcode.com/problems/range-sum-query-2d-mutable/)
- think BIT on x axis, then recursively create another BIT on Y axis.
- $O(log(n) log(n))$ for updates and queries. Linear initialization is a bit tricky.
- nesting loops in update and query methods

```Python
class BIT:
    
    def __init__(self, mat):
        self.nums = mat
        self.bit = [[0]*(len(mat[0])+1) for _ in range(len(mat)+1)]
        
        # build O(n*m*logn*logm)
        # self.mat = [[0]*len(mat[0]) for _ in range(len(mat))]
        # self.bit = [[0]*(len(mat[0])+1) for _ in range(len(mat)+1)]
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         self.update(i,j,mat[i][j])   
        
        # build O(m*n), order of loops matter
        for i in range(1,len(self.bit)):
            for j in range(1,len(self.bit[0])):
                self.bit[i][j] += mat[i-1][j-1]
                if self.next(i) < len(self.bit):
                    self.bit[self.next(i)][j] += self.bit[i][j]
        
        for i in range(1,len(self.bit)):
            for j in range(1,len(self.bit[0])):
                if self.next(j) < len(self.bit[0]):
                    self.bit[i][self.next(j)] += self.bit[i][j]

    def next(self, i):
        return i + (i&-i)
    
    def update(self, i, j, val):
        diff = val - self.nums[i][j]
        self.nums[i][j] += diff
        i,j = i+1, j+1
        while i < len(self.bit):
            jj = j
            while jj < len(self.bit[0]):
                self.bit[i][jj] += diff
                jj += (jj & -jj)
            i += (i & -i)

    def query(self, i, j):
        res,i,j = 0,i+1,j+1
        while i:
            jj = j
            while jj:
                res += self.bit[i][jj]
                jj -= (jj & -jj)
            i -= (i & -i)
        return res

    def sum_range(self,i,j,x,y):
        return self.query(x,y) - self.query(x,j-1) - self.query(i-1,y) + self.query(i-1,j-1) 

class NumMatrix:

    def __init__(self, mat: List[List[int]]):
        self.bit = BIT(mat)

    def update(self, i: int, j: int, val: int) -> None:
        self.bit.update(i,j,val)

    def sumRegion(self, i: int, j: int, x: int, y: int) -> int:
        return self.bit.sum_range(i,j,x,y)

```
- Segment Tree recursive, slower than iterative 2,3 times in practice
- below is point update, range query
- query can be sum, max, gcd. lcd etc (as long as it is a semi-ring)

```Python

class SegmentTree:
    def __init__(self, update_fn, query_fn):
        '''
        for summation tree: query_fn = update_fn = lambda x,y: x+y 
        works if these two with the space of the values form a semi-ring
        '''
        self.UF, self.QF = update_fn, query_fn
        self.T = defaultdict(int) # [0]*4*n

    def update(self, v, tl, tr, pos, delta):
        '''
        v is the index of the node (we use 1-indexing, as v has children 2v, 2(v+1))
        (v,tl,tr) is root node, e.g. (1,0,n-1)
        The tree nodes are represented using the index v and INCLUSIVE intervals [tl,tr]
        Updates SINGLE value at position pos by coposing delta with UF (e.g. adding delta)
        '''
        if tl == tr: 
            self.T[v] = self.UF(self.T[v], delta)
        else:
            tm = (tl + tr)//2
            if pos <= tm:
                self.update(v*2, tl, tm, pos, delta)
            else:
                self.update(v*2+1, tm+1, tr, pos, delta)
            self.T[v] = self.QF(self.T[v*2], self.T[v*2+1])

    def query(self, v, tl, tr, l, r):
        '''
        (v,tl,tr) is root node, e.g. (1,0,n-1)
        returns QF[l:r+1], e.g. sum(nums[l:l+r]) if QF = lambda x,y: x+y 
        '''        
        if l > r: return 0
        if l == tl and r == tr: return self.T[v]
        tm = (tl + tr)//2
        return self.QF(self.query(v*2, tl, tm, l, min(r, tm)), self.query(v*2+1, tm+1, tr, max(l, tm+1), r))

st = SegmentTree(lambda x,y:x+y, lambda x,y: x+y)
```


- Segment tree, range update, range query
- in both segment trees if you have been given array `nums` in advance you can do build in `__init__` in $O(n)$ time (recursively)

```Python
class SegmentTree:
    def __init__(self, update_fn, query_fn):
        self.UF, self.QF = update_fn, query_fn
        self.T = defaultdict(int)   # [0] * (4*N)
        self.L = defaultdict(int)   # [0] * (4*N), keep info for whole segment when making range updates
 
    # lazy propagation
    def push(self, v):
        for u in [2*v, 2*v+1]:
            self.T[u] = self.UF(self.T[u], self.L[v])
            self.L[u] = self.UF(self.L[u], self.L[v])
        self.L[v] = 0

    def update(self, v, tl, tr, l, r, h):
        '''changes nums[l,r+1]'''
        if l > r: return
        if l == tl and r == tr:
            self.T[v] = self.UF(self.T[v], h)
            self.L[v] = self.UF(self.L[v], h)
        else:
            self.push(v)
            tm = (tl + tr)//2
            self.update(v*2, tl, tm, l, min(r, tm), h)
            self.update(v*2+1, tm+1, tr, max(l, tm+1), r, h)
            self.T[v] = self.QF(self.T[v*2], self.T[v*2+1])

    def query(self, v, tl, tr, l, r):
        '''max(nums[l:r+1])'''
        if l > r: return -float("inf")
        if l == tl and tr == r: return self.T[v]
        self.push(v)
        tm = (tl + tr)//2
        return self.QF(self.query(v*2, tl, tm, l, min(r, tm)), self.query(v*2+1, tm+1, tr, max(l, tm+1), r))

```
