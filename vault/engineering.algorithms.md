---
id: 7m3gais9ll8mlmzqlw08s7g
title: Algorithms
desc: ''
updated: 1665755749863
created: 1658766702063
---


Resources:
- [cp algos](https://cp-algorithms.com/)
- [dbabichev](https://flykiller.github.io/)
- [pyrival](https://github.com/ngocuong0105/PyRival)
- [usaco](https://usaco.guide/CPH.pdf)

#TODOs 
- add from dbabichev link for [patterns](https://flykiller.github.io/coding%20ideas/).
- add from pyrival
- add from cp algos
# Buzz words
BIT, AVL trees, B-trees (used in databses?), Red Black Trees, Segment Trees, A* Search, Dijkstra, Kruskal, Prim algo, Trie. String algorithms KMP, State machines. Prime numbers algos, Sieve of Eratosthenes, union find, Morris Traversal [inorder](https://leetcode.com/problems/binary-tree-inorder-traversal/), Palindrome algo, Manacher, Combinations, Permutations smart ways to get (yield) + no duplicated calls, BFS, DFS, [Fractional Cascading](https://en.wikipedia.org/wiki/Fractional_cascading), huffman encoding (greedy)
[TSP](https://leetcode.com/problems/find-the-shortest-superstring/), Sprague-Grundy theorem, game theory, normal incomplete games

#TODO
these buzz words should be sorted as a content page - maybe use backlinks

# Algos


- guess the algo, [p1](https://leetcode.com/problems/shortest-path-with-alternating-colors/)

- BFS with smart states [p1](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)

- sliding window with augmented/additional data structure heap + queue, [p1](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)


- kth element in sorted matrix [p](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/), #TODO check
[paper](https://github.com/ngocuong0105/dendron-wiki/blob/main/vault/assets/files/Engineering/X%2BY.pdf)

- order statistic tree, Red Black tree implementation I think

<details>
<summary> <b>CODE</b> </summary>

```Python
from sortedcontainers import SortedList
sl.add(num)
sl.bisect_left(num) # get order statistic
sl.remove(num)
```
</details>
