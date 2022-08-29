---
id: 7m3gais9ll8mlmzqlw08s7g
title: Algorithms
desc: ''
updated: 1661773382808
created: 1658766702063
---

Should add some tricky algos/data structures here.

**Buzz words**
BIT, Red Black Trees, Segment Trees, A* Search, Dijkstra, Kruskal, Prim algo, Trie. String algorithms KMP, State machines. Prime numbers algos, Sieve of Eratosthenes, union find, Morris Traversal, Palindrome algo, Manacher

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

# Algos

- Manacher, [problem](https://leetcode.com/problems/longest-palindromic-substring/)
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