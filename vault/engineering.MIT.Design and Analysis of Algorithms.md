---
id: g81jrasfq5f0bqj0mxq1ybr
title: Design and Analysis of Algorithms
desc: ''
updated: 1661978188784
created: 1660838818693
---
# MIT 6.046J - Design and Analysis of Algorithms

Lecture [notes](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/)

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