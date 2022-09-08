---
id: g81jrasfq5f0bqj0mxq1ybr
title: Design and Analysis of Algorithms
desc: ''
updated: 1662585052939
created: 1660838818693
---
# MIT 6.046J - Design and Analysis of Algorithms

Lecture [notes](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/). All notes + your marks in one place [here](https://github.com/ngocuong0105/dendron-wiki/blob/main/vault/assets/files/Engineering/Design%20and%20Analysis%20of%20Algorithms%20MIT.pdf)

Lecture [videos](https://www.youtube.com/watch?v=2P-yW7LQr08&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)


**Overview of course:**
- Divide and Conquer (Merge Sort classic example, Fast Fourier transform, algorithm for convex hull, van Emde Boas trees)
- Amortized analysis, random algos, quick select,quick sort skip lists, perfect and universal hashing
- Optimization (greedy (Dijkstra), dynamic programming, shortest paths)
- Network Flow (network, capacities, max flow - min cut problem)
- Linear Programming
- Intractability (polynomial vs exponential time problems, approximation problems)
- Synchronous, Asynchronous algos, Cryptography, Cache

# Lecture 1. Interval Scheduling

*Very similar problems can have very different complexity*. Wiki problem [definition](https://en.wikipedia.org/wiki/Interval_scheduling#Group_Interval_Scheduling_Decision).

Polynomial: Shortest path between two vertices. O(V**2)

NP: Determine if a graph has Hamiltonian cycle: Given a directed graph find a simple cycle that contain each vertex V.

NP-complete are the hardest problems in NP. Solve a NP-complete in polynomial time, then you can solve all NP problems.

---

Given an array of intervals `[(s1,f1), (s2,f2) ... ]` - left closed, right opened. Select the maximum number of non-overlapping intervals.

**Claim** We can solve this problem using a greedy algorithm.

**Definition** A greedy algorithm is a myopic algorithm that processes the input one piece at a time with no apparent look ahead.

Non-working greedy heuristics:
- pick shortest intervals
- pick intervals with least amount of overlaps. Counter example:

```
---- ---- ---- ----
  ----- ---- ----
  -----      ----
  -----      ----
  -----      ----
```
Working greedy heuristic:
- pick earliest finish time

*"Proof by intimidation, proof because the lecturer said so"*

**Proof by induction**

Claim: Given a list of intervals `L`, greedy algorithm with earliest finish time produces `k*` intervals, where `k*` is maximum

Induction on `k*`! Induction on the number of optimal intervals.

1. Base case `k* = 1`. Any interval can be picked up.
2. Suppose claim holds for `k*` and we are given a list of intervals whose optimal schedule has `k*+1` intervals $(s_1,f_1), ... (s_{k*+1},f_{k*+1})$

Run our greedy algo and get intervals $(a_1,b_1), ... (a_{k},b_{k})$. $k$ and $k*$ are not comparable, yet. By construction $b_1 <= f_1$. Thus $S = (a_1,b_1), ... (s_{k*+1},f_{k*+1})$ is another optimal solution of size $k*+1$. Let $L'$ be the set of intervals where $s_i > b_2$. $S$ is optimal for $L$ then $S' =  (s_2,f_2)... (s_{k*+1},f_{k*+1})$ is optimal solution of $L'$ and has size $k$. By initial hypothesis we run greedy on $L'$ and produce
$(a_2,b_2), ... (a_{k},b_{k})$ of size $k-1$. Then $k-1 = k*$ and proves the when we run greedy and get $(a_1,b_1), ... (a_{k},b_{k})$ is also optimal solution.


---

Problem. Weighted interval scheduling. Each interval has a weight $w_i$. Find a schedule with maximum total weight.

*Greedy does not work here, need to use DP*

$O(n^2), O(nlogn)$

![dp_weighted_intervals.png](assets/images/dp_weighted_intervals.png)

![dp_weighted_intervals_2.png](assets/images/dp_weighted_intervals_2.png)

---

NP-complete problem. Generalization of the problem considers $k > 1$ machines/resources.Here the goal is to find $k$ compatible subsets whose union is the largest. First example had k = 1.

In an upgraded version of the problem, the intervals are partitioned into groups. A subset of intervals is compatible if no two intervals overlap.

# Lecture 2. Divide & Conquer: Convex Hull, Median Finding

Divide and Conquer Paradigm: Given a problem of size $n$:
1. Divide it into $a$ subproblems of size $n/b$ where $b > 1$ so that your subproblems have smaller size.
2. Solve each subproblem recursively
3. Combine solutions of subproblems into overall solution (this is where the smarts of the algo is).

Run-time: $T(n) = aT(n/b) + MergeWork$. Often to compute $T(n)$ you can use **Master Theorem**.

![master_theorem.png](assets/images/master_theorem.png)

---

**Convex Hull Problem**

Given $n$ points in a plane $S = \{ (x_i,y_i) | i = 1, 2, ..., n\}$ assume no two have the same $x$ coordinate and no two have the same $y$ coordinate and no three line on the same line. The convex hull is the smallest polygon which contains all points in $S$.

![convex_hull.png](assets/images/convex_hull.png)

Simple algorithm:
- For each pair of points draw a line.
- This line separates the plane in two half-planes.
- Check if all points lie in one side on the half-plane. If yes, this line is part of the convex hull (we call it a segment of the convex hull), otherwise it is not a segment.

Run-time: $O(n^2)$ pairs of points, $O(n)$ to test $= O(n^3)$ runtime.

Divide and Conquer algo:

1. Sort the points by x coordinates.
2. For input set $S$, divide into left half $A$ and right half $B$ by $x$ coordinates.
3. Compute convex hull for $A$ and for $B$.
4. Combine solutions.

**Obvious algorithm** looks at all $a_i, b_j$ pairs and takes $T(n) = 2T(n/2) + O(n^2) = O(n^2)$ runtime


![merge_convex_hulls.png](assets/images/merge_convex_hulls.png)

Find upper, and lower tangent using two finger and a string algorithm. Compute intercept of the vertical line and all $(a,b)$ points. Algo [demo](https://youtu.be/EzeYI7p9MjU?list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&t=2161).

*Merge step:*
After you find the tangents $(a_i,b_j)$ and $(a_k,b_m)$ you link $a_i$ to $b_j$ go down all $b-s$ till you see $b_m$, then link to $a_k$ then go up through all $a-s$ till you see $a_i$.

**Run time**

$T(n) = 2*T(n/2) + O(n) = O(nlogn)$

Other Convex Hull solutions:

- [dbabichev](https://flykiller.github.io/patterns/geometry) chain multiplication?


---

**Median Finding Algorithm**

It is just quick-select algo. Randomized pivot point has $O(n)$ expected run time and $O(n^2)$ worse case. Smart pivot point is a deterministic algo (groups of 5 elements, median of medians)  has $O(n)$ worse case time. See CLRS for detailed algo (deterministic) $O(n)$ time to find median.

# Lecture 3. Divide & Conquer: Fast Fourier Transform

Polynomial of order $n-1$ $A(x) = a_0 + a_1x + a_2x^2 + ... + a_{n-1}x^{n-1}$

Operations on polynomial:
- evaluation $A(x_0) = ?$. Use **Horner's rule** to do it in $O(n)$. $A(x) = a_o + x(a_1 + x(a_2 + ... (xa_{n-1})))$ - $n$ multiplications and additions
- addition $O(n)$
- multiplication $A(x)*B(x) = C(x)$, The coefficients of $C$ are $c_k = \sum_{j = 0}^{k} a_jb_{k-j}$ and that takes $O(k)$ time, so in total brute force multiplication of polynomials takes $O(n^2)$ run time.

Polynomial multiplication is the same as doing **convolution** between vectors.
```
u = [1 1 1];
v =  [1 1 0 0 0 1 1];
1  1  1 -> 1
   1  1 1 -> 2
      1 1 1 -> 2
conv(u,v) =  [1     2     2     1     0     1     2     2     1]
```
$u$ moves as a filter through $v$. Think convolutional neural networks! In polynomial multiplication $a = u, b = v$

**Polynomial representation**
- coefficient vector = $(a_0,a_1 ... a_{n-1})$
- roots $r_0, r_1, ..., r_n$ (allowing multiplicity). $A(x) = c(x-r_0)(x-r_1)..(x-r_{n-1})$
- samples/points (x_k,y_k) for $k = 0, 1 .. ,n-1$ for $A(x_k) = y_k$ has unique solution by the Fundamental Theorem in Algebra

By FTA $n-roots$ allowing multiplicity define uniquely the polynomial.

root representation is not good. Hard to go from polynomial to root representation. Addition is also very hard. Multiplication is easy.


![poly_ops.png](assets/images/poly_ops.png)

No representation is perfect! Our aim is to convert from coefficient to sample representation in $O(nlogn)$ time using Fourier transform.

*Coefficient repr -> Samples repr* can be done in $O(n^2)$ trivially

![matrix_view.png](assets/images/matrix_view.png)

- $V * A$ gets you the sample representation on $O(n^2)$
- Samples to coefficients ($V$ and $y$ are known how would you find $a$):
  - [Gaussian elimination](https://en.wikipedia.org/wiki/Gaussian_elimination) $O(n^3)$
  - Multiply by inverse $V^{-1} * y$ - $O(n^2)$ computing inverse once and use for free.

**Divide & Conquer Algorithm**

We have coefficient representation and want to get samples in $O(nlogn)$ time.

$A(x) = (a_0,a_1,a_2...a_{n-1})$

1. Divide into even and odd coefficients.

$A_{even} = \sum_{k=0}^{n/2} a_{2k}x^{k} = (a_0,a_2...)$

$A_{odd} = \sum_{k=0}^{n/2} a_{2k+1}x^{k} = (a_1,a_3...)$

2. Conquer: Recursively compute $A_{even}(z)$ and $A_{odd}(z)$ for $z \in \{x^2: x\in X\}$

3. Combine: $A(x) = A_{even}(x^2) + xA_{odd}(x^2)$

*Run time*

$T(n,|X|) = 2*T(n/2,|X|) + O(n+|X|))$


![dc_FFT.png](assets/images/dc_FFT.png)

To get **collapsing** set $X$:

![roots_of_unity.png](assets/images/roots_of_unity.png)

[dbabichev](https://flykiller.github.io/patterns/number%20theory) FFT implementation.

`np.convolve` is much slower as it does not use FFT. `scipy` has convolve function and uses FFT.

# Lecture 4. Divide & Conquer: van Emde Boas Trees

Emde Boas Tree.

**Goal**: Maintain $n$ elements among $\{ 0, 1, ... u-1\}$ subject to insert, delete, successor (given a value I want to know the next greater value in the set). We know how to do all these in $O(logn)$ time using balance BST-s (AVL, Red-Black). Emde Boas Trees can doo these in $O(loglog[u] )$ which is an exponential improvement.

**Intuition:** Binary search on the levels of the tree where the number of levels is $log(u)$

Can we do better than $O(log(n)))$ and does not depend on the universe of numbers $\{ 0, 1, ... u-1\}$? **No.**

In each of previous tree data structures, where we do stuff dynamically, at least one important operation took $O(log(n)))$ time, either worst case or amortized. In fact, because each of these data structures bases its decisions on comparing keys, the $O(nlog(n)))$ lower bound for sorting tells us that at least one operation will have to take $O(log(n)))$ time. Why? If we could perform both the INSERT and EXTRACT-MIN
operations in o.lg n/ time, then we could sort $n$ keys in $o(nlog(n)))$ time by first performing $n$ INSERT operations, followed by $n$ EXTRACT-MIN operations.


First attempt to store an array of size $n$ with elements among the set $\{ 0, 1, ... u-1\}$:

![bit_vec.png](assets/images/bit_vec.png)

Insert and Delete are constant, Successor is linear.

Second attempt:

![tree_emde.png](assets/images/tree_emde.png)


![clusters.png](assets/images/clusters.png)

Think each cluster as a binary tree built bottom up using the OR operation. All roots of the different clusters will be a 'summary' vector. As this vector will tell you if there is a one in each of the clusters.

Insert is constant - need to change the value in the clusters and mark in the summary vector.

Successor is:

![successor.png](assets/images/successor.png)


We have not yet improved the runtime complexity. Van Emde Boas is to create clusters which are recursive and depend on other clusters.

![emde_recurse.png](assets/images/emde_recurse.png)


Code implementation details look at the lecture and your notes [here](https://github.com/ngocuong0105/dendron-wiki/blob/main/vault/assets/files/lecture4_emde_boas.pdf).

# Lecture 5: Amortization

So far learning fancy cool data structures. This lecture is on fancy cool techniques of computing complexity of data structures.

Amortized analysis is used to compute complexity of **data structures**. It computes the total run time of a data structure given $n$ executed operations. Amortized analysis is not used in computing run time of algorithms.

**Table doubling**

That's how dynamic arrays work in Python.

Assume a table of size $m$. We will double the size of the table whenever it is full. For $n$ insertions the total running time is:

$O(2^0 + 2^1  + ... 2^{log(n)}) = O(n)$. Thus amortized (i.e.) per insertion it is $O(n)/n = O(1)$.

**Techniques of amortized analysis:**

- aggregate method
- accounting method
- potential method

All these method give upper bounds to the actual cost of all operations = amortized cost.

**Aggregate method**

This is what we did in table doubling. Added total cost of $n$ operations then divided by $n$.
NB: Often when you have a data structure with total of $n$ insert and delete operations you can just think of $n$ insert operations because each element can be deleted at most the number of times it has been inserted.

**Accounting method**

Store credit bank account which should always be **non-negative**. When you do an operation you pay for the operation and can deposit money in you account.

Example. Table Doubling.

- If insertion does not trigger table doubling: I would pay 1 coin for the insertion plus c coin deposit.
- If insertion trigger table doubling: I can pay from the bank account to cover the table doubling.

- amortized cost for table doubling when the table becomes of size $2*n$ is $O(n) - c * n/2 = O(1)$ for chosen large enough $c$. When table doubles from $n$ to $2n$, only last $n/2$ places have coins.

- amortized runtime per insertion $1+c = O(1)$


Aside. Table expansion and contraction have insert and delete operations in $O(1)$ amortized if:
- table doubling when table is full
- table contraction by a halve when there are $m/4$ elements in the table of size $m$

To prove this is indeed $O(1)$ amortized you need the Potential method.

**Potential method**

Define a *potential (energy) function* $\Phi$ which maps each data structure $D_i$ to a nonnegative integer. Check CLRS for more details and proof of Table doubling and halving is $O(1)$.

# Lecture 6: Randomized Algorithms

Randomized algorithm is one that generates a random number $r$ and makes decisions on $r$'s value.

On same input and on different execution randomized algos may:
- run a different number of steps
- produce different output

Two types of random algos:
- Monte Carlo - runs in polynomial time always output is correct with **high probability**
- Las Vegas - runs in **expected** polynomial time output is always correct

**Monte Carlo = probably correct**
**Las Vegas = probably fast**

Monte Carlo is for estimation stuff to get almost correct values.

Las Vegas example is quick sort - $O(nlog(n))$ expected time. 'Almost sorted' does not make sense.


**Problem. Matrix Product Checker**

Given $nx$n$ matrices $A, B, C$ the goal is to check if $A$ x $B=C$. We use randomized algo so that we do not checkout the full multiplication.

**Freivalds' algorithm**

Procedure:

1. Generate an $n × 1$ random $0/1$ vector $r$ .
2. Compute $P = A × (Br) - Cr$
3. Output "Yes" if $P = ( 0 , 0 , … , 0 )$; "No," otherwise.


If $A × B = C$ , then the algorithm always returns "Yes". If $A × B \neq C$ then the probability that the algorithm returns "Yes" is less than or equal to one half.

By iterating the algorithm $k$ times and returning "Yes" only if all iterations yield "Yes", a runtime of $O(k n^2)$ and error probability of $<= 1/2^k$ is achieved.

*Proof that $P($false negatives$) \leq 1/2$*. Idea is for every bad $r$ which does not catch that $AB - C \neq 0$ we create a good $r$ and have 1-1 mapping. See your [notes](https://github.com/ngocuong0105/dendron-wiki/blob/main/vault/assets/files/Engineering/Design%20and%20Analysis%20of%20Algorithms%20MIT.pdf).


**Paranoid Quick Sort**

![paranoid_quick_sort.png](assets/images/paranoid_quick_sort.png)

![paranoid_qs_analysis.png](assets/images/paranoid_qs_analysis.png)

Paranoid Quick sort is probably fast with expected running time $O(nlog(n))$.

# Lecture 7 Randomization: Skip Lists

 A skip list a **probabilistic** data structure that allows $O(log(n))$ search, insert, delete within a set of $n$ elements. It maintains a linked list hierarchy of subsequences with each successive subsequence skipping over fewer elements than the previous one. In the example below we insert 80.

Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists is just simple linked lists.

 ![skip_list.png](assets/images/skip_list.gif)

Design a skip list, [leetcode](https://leetcode.com/problems/design-skiplist/).

**Motivation for skip lists.**

Step 1. Linked list - search is $O(n)$

Step 2. Sorted Linked list - search is still $O(n)$

Step 3. Two sorted Linked list, where the second one is a subsequence (express line) and skips elements.

Step 4. Add $log(n)$ layers of linked lists

![skip_list_motivation.png](assets/images/skip_list_motivation.png)


- Insert is randomized using a fair coin
- Search and Delete are deterministic


**Why skip lists are good?**

**Warm-up Lemma,** The number of levels in $n-$element skip list is $O(log(n))$ with high probability, that is as $n$ grows we the probability converges to 1. This is stronger than having expected running times stuff where you have no guarantees of how likely the worst case is.

With this lemma we can say thing like:
- number of levels in the skip list is at most $2log(n)$ with $90\%$ probability
- at most $4log(n)$ with $99.9\%$ probability etc

**Proof.**
$P(>= clog(n) levels) = P($some element got $>=clog(n)$ promotions $) = (1/2)^{clog(n)} \leq \dfrac{n}{n^c} = \dfrac{1}{n^{c-1}}$


**Search**

Theorem.  Any search in $n$-element skip list costs $O(log(n))$

Steps:
1. We track the search moves **backwards**
2. Backwards search makes up and left moves each with probability 1/2
3. Number of ups is less than number of levels  $\leq c(log(n))$ with high probability
4. The BUM: Total number of moves = number of coin flips until you get $c(log(n))$ heads (up moves)

Claim: Number of coin flips until we see $c(log(n))$ heads is $O(log(n))$ with high probability.

We need to proof that for to see $clog(n)$ heads, there exist a constant $d$ such that if $Y$ is a random vairable counting the number of heads after $dlog(n)$ coin flips then $P(Y < clog(n)) = \dfrac{1}{n^{\alpha}}$. Idea is to use [Chernoff bound](https://en.wikipedia.org/wiki/Chernoff_boundhttps://en.wikipedia.org/wiki/Chernoff_bound).

# Lecture 8: Randomization: Universal & Perfect Hashing

**Buzz words:** Hashing with chaining, open addressing, load factor $n/m$, Simple Uniform Hashing assumption, Hash functions, linear probing, quadratic probing, universal hashing, perfect hashing

**Dictionary problem.** Abstract Data Type (Math definition, interface):
- maintain a dynamic set of items
- each item has a key, item is a key value pair
- insert(item)
- delete(item)
- search(key)

Goal is to run all 3 operations in $O(1)$ expected time (amortized).

In MIT 6.001- [[engineering.MIT.Introduction to algorithms]] you saw hashing with chaining and open addressing. you proved that the insert, delete and search take $O(1+\dfrac{n}{m})$, where n is the number of elements you have in the table and m is the number of slots (table size, number of buckets). So as long as you chose $m = O(n)$ (you can keep that dynamically using  table doubling and shrinking) you would have $O(1)$ operations.

However, you **assumed** that you have **simple uniform hashing**. That is your keys are mapped at each slot of the table with probability $O(\dfrac{1}{m})$ So you had to choose a smart hashing function that would map your keys uniformly. However you want, a hashing function that work work well no matter what the keys are. That is in the worst case scenario for the keys you still want $O(1)$ operations. Our analysis in MIT 6.001 considered average case scenario, where for random keys we would have simple uniform hashing.

Want to avoid the assumption that the keys are random.

**Universal Hashing**

Works for dynamic sets - allows insert and delete
- choose $h$ randomly from a hash family $H$.
- assume $H$ ti be universal hash family:
  - for all keys $k,k'$: $P(h(k)=h(k')) \leq \dfrac{1}{m}$, probability over choosing $h$.

You can prove using indicator variables that $E($number of keys hashing to the same place as $k_i) \leq 1+n/m$

*Dot product hash family*
- assume $m$ m is prime
- assume $u = m^r$ for integer $r$
- view key $k$ in base $m$, $k = (k_0,k_1, .. k_{r-1})$
- for a key $a = (a_0, .. a_{r-1})$ define $h_a(k) = (a \times k) \mod m$ (dot product)

$H = \{h_a| a \in 0...u-1\}$. To choose random $h_a$ choose a random $a$.

Another universal hashing family:


![universal_hashing.png](assets/images/universal_hashing.png)

We achieved $O(1)$ expected time for all operations.

**Perfect Hashing**

This works for static keys and support search only. It is perfect hashing because it achieves $O(1)$ search worst case, that is keys are stored perfectly with no collisions.

- polynomial build time with high probability
- worst case $O(1)$ run time
- worst case memory $O(n)$

Idea: Use 2-level hashing.

![2-level-hashing.png](assets/images/2-level-hashing.png)


# Lecture 9: Augmentation. Range Trees


**Easy Tree Augmentation.**

The goal here is to store $x.f$ at each node $x$, which is a function of the node, namely $f($subtree rooted at $x)$. If $x.f$ is computable **locally** from its children then updates take $O(h)$ runtime where h is the height of the tree. To update $x.f$, we need to walk up the tree to the root.

**Order-statistic trees.**

ADT (interface of the data structure):
- insert(x), delete(x), successor(x)
- rank(x)
- select(i): find me the element of rank i

Want all of these in $O(log(n))$


We can implement the above ADT using easy tree augmentation on AVL trees (or 2-3 trees or any balance BST) to store subtree size: $f($subtree$)$ = $#$ of nodes in it.

![rank_select.png](assets/images/rank_select.png)

NB: Need to choose augmentation functions which can be maintained easier such as subtree size. Above we could thing to store the rank of each node (rank and select would be very easy). However if you insert elements it would be $O(n)$, e.g. if you insert a minimum element you need to update all node ranks.


#TODO Finger Search Trees (this is tree augmentation on 2-3 threes)


**Range Trees**

Solves the problem orthogonal range search.

Suppose we have $n$ points in a $d$-dimension space. We would like a data structure that supports range query on these points: ﬁnd all the points in a give axis-aligned box. An axis-aligned box is simply an interval in 1D, a rectangle in 2D, and a cube in 3D.

Goal is to run in $O(log^d(n) + ($ output size $))$.

NB: Our data structure would be static and support only search points in box query.

**1D case**

We have array `[a_1,a_2...a_n]` and for a query `search(x,y)` we want to output all numbers in the array which are in the interval `[x,y)`. Simple solution is to use sorted array and then do binary searches in $O(log(n))$.

Sorted arrays are inefficient for insertion and deletion. For a dynamic data structure that supports range queries such as AVL, Red-Black trees.

However, neither of the above approaches generalizes to high dimensions.

**1D range trees**

![range_tree.png](assets/images/range_tree.png)

That is like doing rightful rank for node $a$ and left rank for node $b$.

**Analysis.** $O(lg n)$ to implicitly represent the answer (showing just the roots). $O(lg n + k)$ to output all k answers. $O(lg n)$ to report k via subtree size augmentation.

![range_tree_pic.png](assets/images/range_tree_pic.png)

**2D range trees**

Create a 1D range tree on the x coordinates. Do a search to find $O(lg(n))$ nodes which satisfy the interval provided by the $x$ coordinate. **Data Augmentation**: for each of these trees we store another range tree on the y coordinate. So we have dictionary with keys being the nodes of the first range tree, and values is range tree by the y coordinate. There is lots of data duplication. Then you do a little search on the $y-coordinate range tree$. Run time $O(log^2(n))$

Space complexity is $O(n lg n)$. The primary subtree is $O(n)$. Each point is dupli­cated up to $O(lg n)$ times in secondary subtrees, one per ancestor.

*Aside*

Range trees are used in database searches. For example if you have 4 columns in a database and you do searches like col1 should be inside one interval col2 in another interval, etc. range trees would allow fast queries. This is called indexing in database columns.


