---
id: rbnr57rs5a1y8goym1j1npl
title: Data Structures
desc: ''
updated: 1685439577871
created: 1664382752052
---

# Fundamentals


## Hash Tables
Tags: Hashing, Open Addressing, Open-Addressing, Chaining

[Design HashSet](https://leetcode.com/problems/design-hashset/)

```Python
# Chaining
class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(1999)]
        
    def hash(self, key):
        return key%len(self.buckets)
        
    def add(self, key: int) -> None:
        i = self.hash(key)
        self.remove(key)
        self.buckets[i].append(key)
        
    def remove(self, key: int) -> None:
        if self.contains(key):
            i = self.hash(key)
            self.buckets[i].remove(key)
            
    def contains(self, key: int) -> bool:
        i = self.hash(key)
        return key in self.buckets[i]

# Open addressing
class MyHashSet:

    def __init__(self):
        self.size = 10069
        self.hash_table = [None for _ in range(self.size)]

    def hash(self, key, probe):
        return (key%1999 + probe + probe**2) % self.size
    
    def add(self, key: int) -> None:
        for probe in range(self.size):
            i = self.hash(key,probe)
            if self.hash_table[i] in [key,-1,None]:
                break
        self.hash_table[i] = key
        
    def remove(self, key: int) -> None:
        for probe in range(self.size):
            i = self.hash(key,probe)
            if self.hash_table[i] in [key,-1,None]:
                self.hash_table[i] = -1
                break    
                
    def contains(self, key: int) -> bool:
        for probe in range(self.size):
            i  = self.hash(key, probe)
            if self.hash_table[i] == None:
                return False
            elif self.hash_table[i] == key:
                return True
        return False
        
        
```


## Minimum Stack / Minimum Queue
- monotonic queue, [p1](https://leetcode.com/problems/constrained-subsequence-sum/), the cnt variable below defines the enqueue priority, can have different priority implementations, e.g in max sliding window [problem](https://leetcode.com/problems/sliding-window-maximum/) it would be the index of the element

Queue solves sliding window minimum problem, which means that we should report the smallest value inside each window.

Stack solves next nearest element problem
<details>
<summary> <b>CODE</b> </summary>

```Python
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
</details>

- [max stack](https://leetcode.com/problems/max-stack/)

<details>
<summary> <b>CODE</b> </summary>

```Python
class MaxStack:

    def __init__(self):
        self.heap = []
        self.stack = []
        self.del_stack = set()
        self.del_heap = set()
        self.id = 0
        
    def push(self, x: int) -> None:
        heappush(self.heap,(-x,-self.id))
        self.stack.append((x,self.id))
        self.id += 1
        
    def pop(self) -> int:
        self._update_stack()
        self.del_heap.add(self.stack[-1][1])
        return self.stack.pop()[0]

    def top(self) -> int:
        self._update_stack()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        self._update_heap()
        return -self.heap[0][0]

    def popMax(self) -> int:
        self._update_heap()
        self.del_stack.add(-self.heap[0][1])
        return -heappop(self.heap)[0]

    def _update_heap(self):
        while self.heap and -self.heap[0][1] in self.del_heap:
            heappop(self.heap)
            
    def _update_stack(self):
        while self.stack and self.stack[-1][1] in self.del_stack:
            self.stack.pop()

```
</details>


- Most Recently Used Queue [p](https://leetcode.com/problems/design-most-recently-used-queue/)


<details>
<summary> <b>CODE</b> </summary>

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
</details>


- [heights queue](https://leetcode.com/problems/number-of-visible-people-in-a-queue/)

## Sparse Table

# Trees
## Disjoint Set Union = DSU = Union Find
- Complexity:
- If we make $N$ requestis to the union method it would take
- $O(alpha(N))$ amortised time per ops and alpha is the Inverse-Ackermann function. This is approximately constant
- To perform a sequence of m addition, union, or find operations on a disjoint-set forest with n nodes requires total time
- $O(mα(n))$, where $α(n)$ is the extremely slow-growing inverse Ackermann function.

<details>
<summary> <b>CODE</b> </summary>

```Python
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    # path compression
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # keep tree's rank small
    def union(self, x: int, y: int) -> None:
        u, v = self.find(x), self.find(y)
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u] += 1

```
</details>

<details>
<summary> <b>CODE</b> </summary>

```Python
class DSU:
    
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def add(self,x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
    
    # path compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # keep tree's rank small
    def union(self, x, y) -> None:
        u, v = self.find(x), self.find(y)
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u] += 1
```
</details>

- [Google onsite question](https://leetcode.com/problems/number-of-good-paths/)

## Balanced binary search tree

```Python
from sortedcontainers import SortedList
```
#Zadachi
- [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)
- [Closest Room](https://leetcode.com/problems/closest-room/)
- [Traffic lights](https://cses.fi/problemset/task/1163/)
- [Movie Festiva](https://usaco.guide/problems/cses-1632-movie-festival-ii/solution)
## Fenwick Tree = BIT = Binary index tree

- light weight BIT

<details>
<summary> <b>CODE</b> </summary>

```Python
class BIT:
    def __init__(self,n):
        self.bit = [0]*(n+1)
    def update(self,i,val):
        '''adds val to nums[i]'''
        i += 1
        while i<len(self.bit):
            self.bit[i] += val
            i += (i & -i)
    def query(self,i):
        '''sum(nums[:i+1])'''
        i += 1
        res = 0
        while i:
            res += self.bit[i]
            i -= (i & -i)
        return res
        
    def sum_range(self, l, r):
        '''sum(nums[l:r+1])'''
        return self.query(r) - self.query(l-1)
```
</details>

- BIT, 1D, [problem](https://leetcode.com/problems/range-sum-query-mutable/), [problem](https://leetcode.com/problems/count-of-smaller-numbers-after-self/?envType=study-plan&id=algorithm-iii)
- supports cumulutaive computations only on functions which have inverse like sum
- min function has limited support. cannot do min_range(i,j) and also whenever you do an update the new value should be smaller than the old one
- BIT needs functions which form a **group**, such as $\Z$ with operator + 
- $\Z$ and min form a semi-ring and that is not enough. 

- A Fenwick tree can support the following range operations:
    - Point Update and Range Query (classical one with implementation below)
    - Range Update and Point Query (initialize to 0-s, range update = update(l,x), update(r+1,-x), query(l) becomes a point query. Cumulative sum trick)
    - Range Update and Range Query [math trick using two BIT-s](https://cp-algorithms.com/data_structures/fenwick.html#2-range-update-and-point-query)




<details>
<summary> <b>CODE</b> </summary>

```Python
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
</details>

- BIT, Fenwick Tree, Binary Index Tree, 2D, [problem](https://leetcode.com/problems/range-sum-query-2d-mutable/)
- think BIT on x axis, then recursively create another BIT on Y axis.
- $O(log(n) log(n))$ for updates and queries. Linear initialization is a bit tricky.
- nesting loops in update and query methods


<details>
<summary> <b>CODE</b> </summary>

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
</details>


## Sqrt Decomposition
## Segment Tree

- [Increments on subarrays](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/)

- Questions: [Falling Squares](https://leetcode.com/problems/falling-squares/), [Skyline](https://leetcode.com/problems/the-skyline-problem/)

- Segment Tree recursive, slower than iterative 2,3 times in practice
- below is **point update, range query** - both $O(log(n))$
- query can be sum, max, gcd. lcd etc (as long as it is a semi-ring)


<details>
<summary> <b>CODE</b> </summary>

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
</details>

- Segment tree with **range update, range query** - both $O(log(n))$
- lazy update to have query in $O(logn)$
- in both segment trees if you have been given array `nums` in advance you can do build in `__init__` in $O(n)$ time (recursively)


<details>
<summary> <b>CODE</b> </summary>

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
</details>


**Assignment on segments**

Suppose now that the modification query asks to assign each element of a certain segment `a[l...r]` to some value $x$.

- store at each vertex of the Segment Tree whether the corresponding segment is covered entirely with the same value or not. Augment the segment tree with `self.marked = defaultdict(bool)`
- "lazy" update: instead of changing all segments in the tree that cover the query segment, we only change some, and leave others unchanged. 

- A marked vertex will mean, that every element of the corresponding segment is assigned to that value, and actually also the complete subtree should only contain this value.

Small problem: assume you do `update(0,n-1)` and you keep info only in the root. Then you do a second `update(0,n//2)`. the info in the root is irrelevant as half of the values are with one value and the other half with another.

The way to solve this is to push the information of the root to its children and then do the second update.

- Question: [Range module](https://leetcode.com/problems/range-module/)


<details>
<summary> <b>CODE</b> </summary>

```Python
class SegmentTree:
    def __init__(self):
        self.T = defaultdict(bool)   # [0] * (4*N) takes values 0 or 1 whether segment is covered or not
        self.marked = defaultdict(bool)
        
    # lazy propagation
    def push(self, v):
        if self.marked[v]:
            for u in [2*v, 2*v+1]:
                self.T[u] = self.T[v]
                self.marked[u] = True
            self.marked[v] = False

    def update(self, v, tl, tr, l, r, h):
        '''changes nums[l,r+1]'''
        if l > r: return
        if l == tl and r == tr:
            self.T[v] = h
            self.marked[v] = True
        else:
            self.push(v)
            tm = (tl + tr)//2
            self.update(v*2, tl, tm, l, min(r, tm), h)
            self.update(v*2+1, tm+1, tr, max(l, tm+1), r, h)
            self.T[v] = self.T[v*2] and self.T[v*2+1]

    def query(self, v, tl, tr, l, r):
        if l > r: return 1
        if l == tl and tr == r: return self.T[v]
        self.push(v)
        tm = (tl + tr)//2
        return self.query(v*2, tl, tm, l, min(r, tm)) and self.query(v*2+1, tm+1, tr, max(l, tm+1), r)

class RangeModule:

    def __init__(self):
        self.sl = SegmentTree()
        self.n = 10**9+1
        
    def addRange(self, l: int, r: int) -> None:
        self.sl.update(1,0,self.n-1,l,r-1,True)

    def queryRange(self, l: int, r: int) -> bool:
        return self.sl.query(1,0,self.n-1,l,r-1) == 1

    def removeRange(self, l: int, r: int) -> None:
        self.sl.update(1,0,self.n-1,l,r-1,False)
```

</details>

## Treap
## Sqrt Tree
## Randomized Heap

Advanced
    Deleting from a data structure in O(T(n) log n)



## LRU cache

`LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.

`int get(int key)` Return the value of the key if the key exists, otherwise return -1.

`void put(int key, int value)` Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If reach capacity **evict** the least recently used key.

**Algorithm:**

- [LRU](https://leetcode.com/problems/lru-cache)
- $O(1)$ amortised for put and get
- use hashmap to map keys to nodes (nodes has key, val, prev and next)
- use Dlink (represented below as `self.head` and `self.tail`) to track least recently used element (it would be at the tail)

`__init__`
```Python
self.cache = {}
self.cap = cap
self.head = Node()
self.tail = Node()
```

`get(key)`
1. if key not in cache return -1
2. else: update(key) 
3. return `self.cache[key].val`

`put(key,val)`
1. if key in cache: update(key) and change the val
2. else: 
    - if cache is full: evict()
    - add(key,val)

<details>
<summary> <b>CODE</b> </summary>

```Python
class Node:
    def __init__(self, key = None, val = None, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, cap: int):
        self.cache = {}
        self.cap = cap
        self.head = Node()
        self.tail = Node()
        self.link(self.head,self.tail)
        
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.update(key)
        return self.cache[key].val

    def put(self, key: int, val: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.cap:
                self.evict()
            self.add(key,val)
        else:
            self.remove(key)
            self.add(key,val)
    
    def add(self,key,val):
        node = Node(key,val)
        self.link(node,self.head.next)
        self.link(self.head,node)
        self.cache[key] = node
        
    def remove(self,key):
        node = self.cache[key]
        self.link(node.prev,node.next)
        del self.cache[key]
    
    def evict(self):
        self.remove(self.tail.prev.key)
        
    def link(self,a,b):
        a.next,b.prev = b,a
    
    def update(self,key):
        node = self.cache[key]
        self.link(node.prev,node.next)
        self.link(node,self.head.next)
        self.link(self.head,node)
```

</details>


## LFU cache

`LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.

`int get(int key)` Gets the value of the key if the key exists in the cache. Otherwise, returns -1.

`void put(int key, int value)` Update the value of the key if present, or inserts the key if not already present. If reach capacity **evict** least frequently used. Ties are resolved using least recently used. (LFU,LRU)

- [LFU](https://leetcode.com/problems/lfu-cache/)
- $O(1)$ amortised for put and get
- idea: for every frequency create a doubly linked list (LRU idea)

**Algorithm:**

`get(key)`
1. query the node by calling self._node[key]
2. find the frequency by checking node.freq, assigned as f, and query the DLinkedList that this node is in, through calling self._freq[f]
3. pop this node
4. update node's frequence, append the node to the new DLinkedList with frequency f+1
5. if the DLinkedList is empty and self._minfreq == f, update self._minfreq to f+1.
6. return node.val

`put(key, value)`
1. If key is already in cache, do the same thing as get(key), and update node.val as value
2. Otherwise:
    - if the cache is full, pop the least frequenly used element (*)
    - add new node to self._node
    - add new node to self._freq[1]
    - reset self._minfreq to 1

<details>
<summary> <b>CODE</b> </summary>

```Python
class Node:
    def __init__(self, key=None, val=None, freq=1, prev=None, next=None):
        self.key = key
        self.val = val  
        self.freq = freq
        self.prev = prev    
        self.next = next
        
class DLink:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.link(self.head,self.tail)
        
    def pop(self,node):
        self.link(node.prev,node.next)
        
    def append(self,node):
        self.link(node,self.head.next)
        self.link(self.head,node)
    
    def link(self,a,b):
        a.next,b.prev = b,a
    
    def is_empty(self):
        return self.head.next == self.tail

class LFUCache:

    def __init__(self, cap: int):
        self.cap = cap
        self.cache = {}
        self.freq = defaultdict(DLink)
        self.min_freq = 0
        
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.update(key)
        return self.cache[key].val

    def put(self, key: int, val: int) -> None:
        if self.cap == 0: return
        if key in self.cache:
            self.update(key)
            self.cache[key].val = val
        else:
            if len(self.cache) == self.cap:
                self.evict()
            self.add(key,val)
    
    def update(self,key):
        node = self.cache[key]
        self.freq[node.freq].pop(node)
        if self.freq[node.freq].is_empty() and self.min_freq == node.freq:
            self.min_freq += 1
        node.freq += 1
        self.freq[node.freq].append(node)

    def add(self, key, val):
        node = Node(key,val)
        self.freq[1].append(node)
        self.cache[key] = node
        self.min_freq = 1

    def evict(self):
        node = self.freq[self.min_freq].tail.prev
        self.freq[self.min_freq].pop(node)
        del self.cache[node.key]
```
</details>

Additionally, you can implement a dynamic balanced binary tree `SortedList()` solution by adding the notion of frequency and time. get and put would be $O(logn)$.

<details>
<summary> <b>CODE</b> </summary>

```Python
from sortedcontainers import SortedList

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.sl = SortedList() # [counter,time,key,value]
        self.time = 0
        
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        el = self.cache[key]
        self._increase_count(el)
        self.time += 1
        # print(self.sl, self.cache)
        return el[-1]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return
        old_freq = 0
        if key in self.cache:
            old_freq = self.cache[key][0]
            self._delete(self.cache[key])
            del self.cache[key]    
            
        if len(self.cache) == self.cap:
            el = self.sl.pop(0)
            del self.cache[el[2]]
            
        el = (1+old_freq, self.time, key, value)
        self.cache[key] = el
        self._add(el)        
        self.time += 1
            
    def _add(self, el):
        self.sl.add(el)
        
    def _delete(self, el):
        self.sl.remove(el)
        
    def _increase_count(self, el):
        self.sl.remove(el)
        del self.cache[el[2]]
        new_el = list(el)
        new_el[0] += 1
        new_el[1] = self.time
        new_el = tuple(new_el)
        self.sl.add(new_el)
        self.cache[new_el[2]] = new_el 
```
</details>
