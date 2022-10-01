---
id: rbnr57rs5a1y8goym1j1npl
title: Data Structures
desc: ''
updated: 1664611836388
created: 1664382752052
---

# Fundamentals
## Minimum Stack / Minimum Queue
## Sparse Table

# Trees
## Disjoint Set Union
## Fenwick Tree = BIT = Binary index tree

- BIT, 1D, [problem](https://leetcode.com/problems/range-sum-query-mutable/), [problem](https://leetcode.com/problems/count-of-smaller-numbers-after-self/?envType=study-plan&id=algorithm-iii)
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



## Sqrt Decomposition
## Segment Tree

**Questions**
- [Falling Squares](https://leetcode.com/problems/falling-squares/), [Skyline](https://leetcode.com/problems/the-skyline-problem/)

- Segment Tree recursive, slower than iterative 2,3 times in practice
- below is point update, range query - both $O(log(n))$
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


- Segment tree, range update, range query - both $O(log(n))$
- lazy update to have query in $O(logn)$
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



## Treap
## Sqrt Tree
## Randomized Heap

Advanced
    Deleting from a data structure in O(T(n) log n)

