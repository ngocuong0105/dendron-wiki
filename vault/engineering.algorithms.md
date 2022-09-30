---
id: 7m3gais9ll8mlmzqlw08s7g
title: Algorithms
desc: ''
updated: 1664518101958
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
- add from cp algos
# Buzz words
BIT, AVL trees, B-trees (used in databses?), Red Black Trees, Segment Trees, A* Search, Dijkstra, Kruskal, Prim algo, Trie. String algorithms KMP, State machines. Prime numbers algos, Sieve of Eratosthenes, union find, Morris Traversal [inorder](https://leetcode.com/problems/binary-tree-inorder-traversal/), Palindrome algo, Manacher, Combinations, Permutations smart ways to get (yield) + no duplicated calls, BFS, DFS, [Fractional Cascading](https://en.wikipedia.org/wiki/Fractional_cascading)
[TSP](https://leetcode.com/problems/find-the-shortest-superstring/)


# Algos

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
