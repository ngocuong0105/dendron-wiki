---
id: 62fr2x24gm8h0m2x4c3r862
title: Misc
desc: ''
updated: 1665491734192
created: 1664382870554
---
# Sequences

## Binary Search
- template for finding smallest element $i$ in array such that `func(i)` is `True`

<details>
<summary> <b>CODE</b> </summary>

```Python
def bs(i,j,func):
    while i < j:
        mid = i+j >> 1
        if func(mid):
            j = mid
        else:
            i = mid + 1
    return i
```

</details>

- 2D problems often treat columns/rows as elements. E.g each column is element and we do binary search on columns $O(m*logn)$
    - [black pixels](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/)
    - [peak element](https://leetcode.com/problems/find-a-peak-element-ii/)

- built in python library

<details>
<summary> <b>CODE</b> </summary>

```Python
import bisect
bisect.bisect_left(arr,num,key) # uses >=
bisect.bisect_right(arr,num,key) # uses >

# can binary search tuples too
bisect.bisect_left(arr, (x,y), key = lambda x: (x[0],x[1]))
```
- binary search + insert
```python
import bisect
bisect.insort_left(arr,num,key) # runs binary search and inserts O(n)
```


</details>


## RMQ task (Range Minimum Query - the smallest element in an interval)
## Longest increasing subsequence
## Maximum/minimum subarray sum
- [leetcode](https://leetcode.com/problems/maximum-subarray/)

**Solution 1.**
- goal find `nums[l:r+1]` with max sum
- use cumulative sums `nums[l:r+1] = cum[r]-cum[l-1]`
- redefined goal for each $r$ find $l$ which maximizes `sum(nums[l:r+1])`
- compute $cum[r]$ as we go, and maintain minimum possible value for $cum[l-1]$

<details>
<summary> <b>CODE</b> </summary>

```Python
def maxSubArray(nums: List[int]) -> int:
    res,min_sum,sm = -float('inf'),0,0
    for r in range(len(nums)):
        sm += nums[r]
        res = max(res,sm-min_sum)
        min_sum = min(min_sum,sm)
    return res
```
</details>

**Solution 2.**
- Kadane algo
- compute partial/cumulative sum `sm` as we go. If negative rest to 0
- our maximum subarray must start at a critical point when $sm < 0$

<details>
<summary> <b>CODE</b> </summary>

```Python
def maxSubArray(nums: List[int]) -> int:
    res,curr = -float('inf'),0
    for num in nums:
        curr += num
        res = max(res,curr)
        curr = max(curr,0)
    return res
```
</details>

#QED


## K-th order statistic in O(N)
# Game Theory
## Games on arbitrary graphs
## Sprague-Grundy theorem. Nim

**Concept 1 (Impartial Game)**: Given a particular arrangement of the game
board, if either player have exactly the same set of moves should he
move first, and both players have exactly the same winning condition,
then this game is called impartial game. For example, chess is not
impartial because the players can control only their own pieces, and
the [flip game II](https://leetcode.com/problems/flip-game-ii/) , on the other hand, is impartial.


**Concept 2 (Normal Play vs Misere Play)**: If the winning condition of
the game is that the opponent has no valid moves, then this game is
said to follow the normal play convention; if, alternatively, the
winning condition is that the player himself has no valid moves, then
the game is a Misere game. Our +- [flip game II](https://leetcode.com/problems/flip-game-ii/) has apprently normal play.

We consider impartial normal games.

Such games can be completely described by a directed acyclic graph: the vertices are game states and the edges are transitions (moves). 
A vertex without outgoing edges is a losing vertex (a player who must make a move from this vertex loses).


**Goal:** A state is winning if there is at least one transition to a losing state and is losing if there isn't at least one transition to a losing state. Our task is to classify the states of a given game.

**Nim**
There are several piles, each with several stones. In a move a player can take any positive number of stones from any one pile and throw them away. A player loses if they can't make a move, which happens when all the piles are empty.

**Charles L. Bouton Theorem.** The current player has a winning strategy if and only if the xor-sum of the pile sizes is non-zero.

Proof by induction. Induction step proves that if the current state is 0 then all other neighbour states are non zero. If the current state is non-zero you can always reach a zero state, consider the pile with the largest number of stones and consider is largest bit. (do xor tricks).

**Colloraly.** Nim games are equivalent as long as the xor value is the same.

Game of Nim can be reduced to game of one pile.

**Sprague-Grundy theorem** 
This theorem proves the equivalence of impartial games and Nim. It reduces every impartial normal game to Nim.

Let's consider a state $v$ of a two-player impartial game and let $\{v_{i},i = 1 \dots n\}$ be the states reachable from it. To this state $v$, we can assign a fully equivalent game of Nim with one pile of size $x$. The number is called the Grundy value or **nim-value** of state $v$. (this is the Game to Nim mapping)

Find this number $x$ recursively:

$x = mex(x_1, x_2, .... x_n)$

where $mex$ is the minimum excluding function, e.g $mex([0,1,2,4,5]) = 3$

Recursion base case is the end states where there are no possible moves and whoever turn it is they loose (nim-value equal to 0).


**Recipe**
To calculate the Grundy value of a given state you need to:
1. Get all possible transitions from this state
2. Each transition can lead to a sum of independent games (one game in the degenerate case). Calculate the Grundy value for each independent game and xor-sum them. Of course xor does nothing if there is just one game.
3. After we calculated Grundy values for each transition we find the state's value as the $mex$ of these numbers.
4. If the value is zero, then the current state is losing, otherwise it is winning.


**Problems**

- [flip game II](https://leetcode.com/problems/flip-game-ii/)

<details>
<summary> <b>CODE</b> </summary>

```Python
# O(C_n) where C_n is n-th Catalan number
class Solution:
    def canWin(self, s: str) -> bool:
        def adj(s):
            neigh = []
            for i in range(len(s)-1):
                if s[i:i+2] == '++': neigh.append(s[:i]+'--'+s[i+2:])
            return neigh
        @cache
        def dfs(s):
            for u in adj(s):
                if not dfs(u): return True
            return False
        return dfs(s)

# O(n^2) Sprague-Grundy theorem
class Solution:
    def canWin(self, s: str) -> bool:
        @cache
        def dp(s):
            if len(s) < 2: return 0
            st = set()
            for i in range(len(s)-1):
                if s[i:i+2] == '++':
                    st.add(dp(s[:i]) ^ dp(s[i+2:]))
            # mex
            i = 0 
            while i in st:
                i += 1
            return i
        return dp(s) != 0

```

</details>


**Note** the second solution is not $O(N^2)$ truly as it has lots of subproblems. Need to preprocess the input so that the subproblems depend on single numbers. e.g. get lenghts of plus groups: '++++--++-' preprocess to `[4,2]`. See your leetcode solution.


- [game of nim](https://leetcode.com/problems/game-of-nim/)
- [chalkboard](https://leetcode.com/problems/chalkboard-xor-game/)

#QED

# Schedules
## Scheduling jobs on one machine
## Scheduling jobs on two machines
## Optimal schedule of jobs given their deadlines and durations
# Miscellaneous
## Josephus problem
## 15 Puzzle Game: Existence Of The Solution
## The Stern-Brocot Tree and Farey Sequences

## Rotate image

- rotate image, [p1](https://leetcode.com/problems/rotate-image/)
- 90 degree rotation = flip + transpose

<details>
<summary> <b>CODE</b> </summary>

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
</details>

## Longest valid parenthesis
- [leetcode](https://leetcode.com/problems/longest-valid-parentheses/)

<details>
<summary> <b>CODE</b> </summary>

```Python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def compute(ch,s):
            bal,res,curr = 0,0,0
            for p in s:
                bal += (p == ch)
                bal -= (p != ch)
                curr += 2*(p == ch)
                if bal == 0: 
                    res = max(res,curr)
                elif bal<0:
                    curr,bal = 0,0
            return res
        return max(compute('(',s),compute(')',s[::-1]))
```
</details>



## LRU cache
- [LRU](https://leetcode.com/problems/lru-cache)

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