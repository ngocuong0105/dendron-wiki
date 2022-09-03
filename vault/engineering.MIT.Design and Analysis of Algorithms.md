---
id: g81jrasfq5f0bqj0mxq1ybr
title: Design and Analysis of Algorithms
desc: ''
updated: 1662225275068
created: 1660838818693
---
# MIT 6.046J - Design and Analysis of Algorithms

Lecture [notes](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/). All notes + your marks in one place [here](https://github.com/ngocuong0105/dendron-wiki/blob/main/vault/assets/files/Design%20and%20Analysis%20of%20Algorithms%20MIT.pdf)

Lecture [videos](https://www.youtube.com/watch?v=2P-yW7LQr08&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)


**Overview of course:**
- Divide and Conquer (Merge Sort classic example, Fast Fourier transform, algorithm for convex hull)
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

## Lecture 5: Amortization

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

## Lecture 6: