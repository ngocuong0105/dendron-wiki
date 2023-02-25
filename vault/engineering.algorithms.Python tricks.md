---
id: x0cxhdz6m217jsrqw2pcwuk
title: Python tricks
desc: ''
updated: 1677328342886
created: 1664446506779
---

- transpose of a matrix

```Python
# transpose with unzipping
mat = [(1,2,3),(4,5,6)]
transpose_mat = list(zip((*mat)))
```

- cumulative sum,min,max,xor,gcd. Note sum and xor are semi-rings on $\Z$ (that is they have minus) - you can query subarrays in $O(1)$.
```Python
# cumulative sum array, cdf
from itertools import accumulate
nums = [1,2,3,4]
cum = list(accumulate(nums,func = lambda x,y:x+y)) # [1,3,6,10]
```

- xor cumulative
```python
xor_cum = [0] + list(accumulate(arr,lambda x,y:x^y))
def f(l,r):
    '''returns xor subarray arr[l]^arr[l+1]^...^arr[r]'''
    xor_cum[r+1]^xor_cum[l]
```

- flatten list with chain
```Python
# flatten list
from itertools import chain
equations = [[1,2,3],[4,5]]
list(chain(*equations))

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

```Python
# count occurrences of element in list
ls = [1,2,3,1,1]
ls.count(1)
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

- is a string a rotated version of another string, is rotate
```python
# Consider a string S="helloworld". Now, given another string T="lloworldhe", can we figure out if T is a rotated version of S? Yes, we can! We check if S is a substring of T+T.
def is_rotate(s,t):
    return s in t+t
```

- traverse squares quickly. If $x = a*a$ then $x = 1+3+5...$
```python
x,n = 0,1
while True:
    print(x)
    x += n
    n += 2
```
- [Binary operations laws](https://stackoverflow.com/questions/12764670/are-there-any-bitwise-operator-laws)
- bitwise tricks, binary operations
```Python
class Binary:

    """
    This is a class for basic manipulation methods for bits.
    Arguments: Integer in base 10
    Returns:
    binary representation;
    get, set, clear, update specific bits;
    count number of bits;
    least significant bit;
    """

    def __init__(self, num: int):
        self.decimal = num

    # binary representation
    def __str__(self) -> str:
        res = []
        num = self.decimal
        while num > 0:
            res.append(str(num % 2))
            num //= 2
        return f"{self.decimal} has binary representation {''.join(res[::-1])}"

    def __repr__(self) -> str:
        res = []
        num = self.decimal
        while num > 0:
            res.append(str(num % 2))
            num //= 2
        return "".join(res[::-1])

    # get bit
    def get(self, i: int) -> int:
        msk = 1 << i
        if self.decimal & msk != 0:
            return 1
        return 0

    # set bit
    def set(self, i: int) -> int:
        msk = 1 << i
        self.num = self.decimal | msk
        return self.decimal

    # clear specific bit i
    def clear(self, i: int) -> int:
        msk = ~(1 << i)  # ~ reverses bits, 0 -> 1 and 1 -> 0
        self.decimal = self.decimal & msk
        return self.decimal

    # clear all bits from beginning to bit i
    def clearFirstBits(self, i: int) -> int:
        msk = (1 << i) - 1
        self.decimal = self.decimal & msk
        return self.decimal

    # clear all bits from end to bit i
    def clearEndBits(self, i: int) -> int:
        msk = -1 << (i + 1)  # note -1 is 11111..1
        self.decimal = self.decimal & msk
        return self.decimal

    # update bit i to value val
    def update(self, i: int, val: bool) -> int:
        msk = ~(1 << i) | (val << i)
        self.decimal = self.decimal & msk
        return self.decimal

    # returns number of bits
    def countBits(self) -> int:
        res = 0
        while self.decimal > 0:
            # res+=self.decimal%2
            res += self.decimal & 1
            self.decimal >>= 1
        return res

    # least significant bit
    def lsb(self) -> int:
        # negative numbers are represented as two's complement
        # two's complement = one's complement + 1
        return self.decimal & -self.decimal
```

- print + assignment
```python
print(x:=10)
```

- window multiply
```python
def window_multiply(filter_window: np.ndarray, target: np.ndarray):
    """
    Example:filter_window = np.array([1,2,3]),  target = np.array([4,5,6,7,8,9,10]), 
    out = [
        [ 4, 10, 18],
        [ 5, 12, 21],
        [ 6, 14, 24],
        [ 7, 16, 27],
        [ 8, 18, 30]
        ]
    out[0] = [1*4, 2*5, 3*6] = [4, 10, 18]
    out[1] = [1*5, 2*6, 3*7] = [5, 12, 21]
    etc.
    """
    w = len(filter_window)
    indices = np.arange(len(target) - w + 1)[:, None] + np.arange(w)
    out = filter_window * target[indices]
    return out

```

- itertools.groupby()
```python
for k,v in groupby('aaabbcddd'):
    print(k,list(v)) # a, [a,a,a]

groups = []
for k,v in groupby(s):
    groups.append((k,len(list(v))))
```

- [negative power modulus](https://math.stackexchange.com/questions/2592324/how-to-do-a-modular-arithmetic-with-negative-exponents). You can use it as of Python 3.8. Useful for solving linear Diophantine equality. First and third argument need to be coprime.
```python
pow(23,-1,2)
```

- binary to decimal
```python
int('101',2)
```

- careful with instantiation and constructor
```python

class Node:
    def __init__(self,val,children=[]):
        self.val = val
        self.children = children

a = Node('a')
b = Node('b')
a.children.append(12)
print(b.children) # prints [12]
# modification on object a modifies b too, children is a class variable... if not set
```