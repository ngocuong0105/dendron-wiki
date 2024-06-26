---
id: yh0ww8ogawf7n4n2q2lnsus
title: Graphs
desc: ''
updated: 1704972450286
created: 1664382861926
---

# Graph traversal
## Breadth First Search

- [visit all](https://leetcode.com/problems/shortest-path-visiting-all-nodes/?envType=study-plan&id=dynamic-programming-iv)
## Depth First Search

----

# Connected components, bridges, articulations points

## Finding Connected Components

## Finding Bridges in O(N+M)

- find bridges in graph in linear time
- [leetcode](https://leetcode.com/problems/critical-connections-in-a-network/)
- [explanation](https://cp-algorithms.com/graph/bridge-searching.html#implementation)
- key: track entry times in array `tin`, and compute array `low`
`low[s]` is minimum of:
    - entry time in s
    - entry time in all descendants u of s which are back edges
    - `low[u]` for all u where $(s,u)$ is tree edge


<details>
<summary> <b>CODE</b> </summary>

```Python
def bridges(n, adj_mat) -> List[List[int]]:
    def dfs(s,p):
        nonlocal t
        visited.add(s)
        t += 1
        low[s] = tin[s] = t
        for u in adj_mat[s]:
            if u not in visited:
                dfs(u,s)
                low[s] = min(low[s],low[u])
                if low[u] > tin[s]:
                    res.append([s,u])
            elif u != p:
                low[s] = min(low[s],tin[u])
    res,visited = [],set()
    t,low,tin = 0,[float('inf')]*n,[float('inf')]*n
    for s in range(n):
        if s not in visited:
            dfs(s,-1)
    return res
```
</details>

## Finding Bridges Online

## Finding Articulation Points in $O(N+M)$
- [leetcode](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/)
- [explanation](https://cp-algorithms.com/graph/cutpoints.html)


<details>
<summary> <b>CODE</b> </summary>

```Python 
def articulation_point(adj):
    def dfs(s,p):
        nonlocal t
        visited.add(s)
        t += 1
        tin[s] = low[s] = t
        children = 0
        for u in adj[s]:
            if u not in visited:
                dfs(u,s)
                low[s] = min(low[s],low[u]) 
                if low[u] >= tin[s] and p!=-1: # \geq !
                    art.append(s)
                children += 1
            elif u != p:
                low[s] = min(low[s],tin[u])  
        if children != 1 and p==-1:
            art.append(s)
    t,visited = 0, set()
    tin,low,art = {},{},[]
    for s in adj:
        if s not in visited: dfs(s-1)
    return art != []
            
```
</details>

- [malware spread](https://leetcode.com/problems/minimize-malware-spread-ii/); can be solved using simple dfs/bfs for each node in $O(N^3)$, use articulation points $O(N^2)$, DSU $O(N^2)$

## Strongly Connected Components and Condensation Graph

## Strong Orientation


----

# Single-source shortest paths

## Dijkstra - finding shortest paths from given vertex
- [Cheapest flights within k stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/?envType=study-plan&id=level-3)

- [Modify edges, SMART Dijkstra application](https://leetcode.com/problems/modify-graph-edge-weights/)

```python
def dijkstra(s):
    h = [(0,s)]
    dist,parent = {s:0},{}
    while h:
        d,s = heappop(h)
        for u,du in adj[s]:
            if dist.get(u,inf) > du+d:
                dist[u] = du+d
                parent[u] = s
                heappush(h,(dist[u],u))
    return dist,parent
```

**First loop on k, otherwise it will error. k is the phase count.**

## Dijkstra on sparse graphs
## Bellman-Ford - finding shortest paths with negative weights
## 0-1 BFS
## D´Esopo-Pape algorithm


# All-pairs shortest paths
## Floyd-Warshall - finding all shortest paths

**NB: Order of the loops is important. MUST START WITH K that is the phase.**

Given a directed or an undirected weighted graph $G$ with $n$ vertices.
The task is to find the length of the shortest path $d_{ij}$ between each pair of vertices $i$ and $j$.

The graph may have negative weight edges, but no negative weight cycles.


The key idea of the algorithm is to partition the process of finding the shortest path between any two vertices to **several incremental phases**.

Let us number the vertices starting from 1 to $n$.
The matrix of distances is $d[ ][ ]$.

Before $k$-th phase ($k = 1 \dots n$), $d[i][j]$ for any vertices $i$ and $j$ stores the length of the shortest path between the vertex $i$ and vertex $j$, which contains only the vertices $\{1, 2, ..., k-1\}$ as internal vertices in the path.

In other words, before $k$-th phase the value of $d[i][j]$ is equal to the length of the shortest path from vertex $i$ to the vertex $j$, if this path is allowed to enter **only the vertex with numbers smaller than $k$** (the beginning and end of the path are not restricted by this property).

It is easy to make sure that this property holds for the first phase. For $k = 0$, we can fill matrix with $d[i][j] = w_{i j}$ if there exists an edge between $i$ and $j$ with weight $w_{i j}$ and $d[i][j] = \infty$ if there doesn't exist an edge.


Suppose now that we are in the $k$-th phase, and we want to compute the matrix $d[ ][ ]$ so that it meets the requirements for the $(k + 1)$-th phase.
We have to fix the distances for some vertices pairs $(i, j)$.
There are two fundamentally different cases:

*   The shortest way from the vertex $i$ to the vertex $j$ with internal vertices from the set $\{1, 2, \dots, k\}$ coincides with the shortest path with internal vertices from the set $\{1, 2, \dots, k-1\}$.

    In this case, $d[i][j]$ will not change during the transition.

*   The shortest path with internal vertices from $\{1, 2, \dots, k\}$ is shorter.

    This means that the new, shorter path passes through the vertex $k$.
    This means that we can split the shortest path between $i$ and $j$ into two paths:
    the path between $i$ and $k$, and the path between $k$ and $j$.
    It is clear that both this paths only use internal vertices of $\{1, 2, \dots, k-1\}$ and are the shortest such paths in that respect.
    Therefore we already have computed the lengths of those paths before, and we can compute the length of the shortest path between $i$ and $j$ as $d[i][k] + d[k][j]$.


```cpp
for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            d[i][j] = min(d[i][j], d[i][k] + d[k][j]); 
        }
    }
}
```

## Number of paths of fixed length / Shortest paths of fixed length


# Spanning trees
    Minimum Spanning Tree - Prim's Algorithm
    Minimum Spanning Tree - Kruskal
    Minimum Spanning Tree - Kruskal with Disjoint Set Union
    Second best Minimum Spanning Tree - Using Kruskal and Lowest Common Ancestor
    Kirchhoff Theorem
    Prüfer code
# Cycles
## Checking a graph for acyclicity and finding a cycle in O(M)

- nonlocal variables cycle and visited
- keep path variable tracing the dfs
- CLRS and CP algo use coloring, white, gray, black and nonlocal cycle variable (i think we cannot avoid nonlocal stuff)
- **NB!!!** below is for cycle in directed graph, for **undirected** need to keep parent pointers and make sure you when you go back to parent you don't consider it as cycle

<details>
<summary> <b>CODE</b> </summary>

```Python
def dfs(s,path):
    nonlocal cycle
    visited.add(s)
    for u in adj[s]:
        if u not in visited:
            dfs(u,path|{u})
        elif u in path:
            cycle = True
            return
cycle,visited = False,set()
for s in range(n):
    if s not in visited:
        dfs(s,set([s]))
print(cycle)
```
</details>

- To get the nodes in the cycle you might keep a `parent` dictionary and do a while loop instead of marking cycle = True
- Alternatively there is this trick to get the cycle nodes:

<details>
<summary> <b>CODE</b> </summary>

```python
# step 1: backtracking DFS to find the cycle
circle = []
vis = set()

def find_circle(node, par):
    if node in vis:
        return (True, node)
    for nei in g[node]:
        if nei == par: continue
        vis.add(node)
        circle.append(node)
        status, res = find_circle(nei, node)
        if status: return status, res
        circle.pop()
        vis.remove(node)

    return False, None


_, node = find_circle(0, None)
# get the circle from start "node"
circle = circle[circle.index(node):] 
```
</details>



#QED

## Finding a Negative Cycle in the Graph


## Eulerian Path

Euler path

Eulerian Path is a path in a graph that visits every edge exactly once. 

- [leetcode](https://leetcode.com/problems/valid-arrangement-of-pairs/)
```Python
def hierholzer_recursive(graph):
    def visit(vertex, circuit):
        while graph[vertex]:
            next_vertex = graph[vertex].pop()
            visit(next_vertex, circuit)
        circuit.append(vertex)

    circuit = []
    start_vertex = list(graph.keys())[0]
    visit(start_vertex, circuit)
    circuit.reverse()
    return circuit

```
To properly initialize the start vertex in the recursive version of Hierholzer's algorithm, you can modify the code to select a vertex with an odd degree (if one exists) as the starting point. This ensures that the algorithm will find an Eulerian circuit if one exists in the graph.



# Lowest common ancestor
## Lowest Common Ancestor
Given a tree $G$ find the lowest common ancestor of two nodes $(u,v)$. If you have to do just once it is easy, see [lca](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

<details>
<summary> <b>CODE</b> </summary>

```Python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    l,r = lca(root.left),lca(root.right)
    if l and r: return root
    return l if l else r
```
</details>

More interesting is when you have **queries** $(u_i,v_i)$. Note lca lies on shortest path.


## Hamiltonian path

A Hamiltonian path or traceable path is a path that visits each vertex of the graph exactly once. A graph that contains a Hamiltonian path is called a traceable graph.

Whether Hamiltonian path exists in a graph or not is NP-complete problem.

## Binary Lifting

![](assets/images/o(logn).png)

With Binary tree lifting you can answer questions such as given a tree and a node inn the tree, what is its k-th ancestor.

Brute force is to repeat $k$ times `v = parent[v]` -> complexity $O(Q * N)$ if we have $Q$ queries and the tree is very deep.

Binary tree lifting is also known as jump pointers. [Errihto](https://www.youtube.com/watch?v=oib-XsjFa-M&t=579s&ab_channel=Errichto).

**There are $log(n)$ powers of 2.**


**Preprocessing**

**Define** $u[v][j]$ is the $2^j$-th ancestor of v.

$u[v][j]$ is the $2^j$-th ancestor of v.
$u[v][0] = parent[v]$ - that is my first parent
$u[v][1] = u[u[v][0]][0]$ - what is my second parent? first parent of my first parent
$u[v][2] = u[u[v][1]][1]$ - what is my fourth parent? second parent of my second parent

`u` is a map that tells me for each node what is the 1st, 2nd, 4th, 8th ... ancestor.


```Python
# parent[i] if the parent of node i
log = len(bin(n))
parent[0] = 0 # root
for i in range(len(parent)):
    up[i][0] = parent[i]
for j in range(1,log):
    for i in range(n):
        up[i][j] = up[up[i][j-1]][j-1]
        
def getKthAncestor(node: int, k: int) -> int:
    # if depth[node] < k: return -1
    for j in range(log):
        if k & (1<<j):
            node = up[node][j]
    return node
```

careful with for loops, you might need $parent[i] < i$ to do preprocessing (computing) matrix $u$ (depending on your loop order).  

- [Kth ancestor](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) 

**Complexity:** $O(nlog(n))$ on preprocessing and $O(log(n))$ per query.

## Lowest Common Ancestor - Binary Lifting




**Lowest common ancestor**
For queries with nodes $(u,v)$ we want to get the lowest common ancestor of $u$ and $v$.

Idea: Run dfs, record for each nodes `timein` and `timeout`. This helps to answer if $u$ is ancestor ov $v$ or vice versa.

Start from the top $up[u][L]$ = the highest ancestor of $u$. Decrement $L$ checking if $up[u][i]$ is ancestor of $v$. Goal is to find highest ancestor of u which is not ancestor of $v$, return $up[u][0]$.

<details>
<summary> <b>CODE</b> </summary>

```Python
def is_ancestor(p,q):
    return timein[p] <= timein[q] and timeout[p] >= timeout[q]

def lca(p,q):
    if is_ancestor(p,q): return p
    if is_ancestor(q,p): return q
    for i in range(l-1,-1,-1):
        if not is_ancestor(up[p][i],q):
            p = up[p][i]
    return up[p][0]

def dfs(root,p):
    nonlocal time
    if not root: return
    timein[root] = time
    time += 1
    up[root] = [None]*l
    up[root][0] = p
    for i in range(1,l):
        up[root][i] = up[up[root][i-1]][i-1]
    dfs(root.left, root)
    dfs(root.right, root)
    timeout[root] = time
    
time,l = 0,20 # supports 2**19 nodes
up,timein,timeout = {},{},{}
dfs(root,root)
    
print(lca(p,q)) # lowest common ancestor in O(log(n))
```
</details>

Problem where you need to use optimised LCA:
- [queries in tree](https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/)


- [longest good segement](https://www.codechef.com/problems/LGSEG)


- semi brute force, for each index i (starting index), find largest good segment
- $O(n^2)$

<details>
<summary> <b>CODE</b> </summary>

```Python
def solve(nums,N,K,S):
    def compute(i):
        seg,curr,j = 1,nums[i],i+1
        while seg <= K and j<N:
            if curr + nums[j] > S:
                curr = 0
                seg += 1
            curr += nums[j]
            j += 1
        return j-i-(seg>K)
    return max(compute(i) for i in range(N))
```
</details>

- binary lifting = jumps

<details>
<summary> <b>CODE</b> </summary>

```Python

def build(N,start_index):
    up = [[None]*N for _ in range(20)]
    up[0] = start_index
    for i in range(1,20):
        for j in range(N):
            p = up[i-1][j]
            if p == -1:
                up[i][j] = -1
            else:
                up[i][j] = up[i-1][p]
    return up

def call(up, node, K):
    last,jump = node,1
    for i in range(19):
        if node == -1: break
        if K & jump:
            node = up[i][node]
        jump <<= 1
    return last-node

def solve2(nums,N,K,S):
    start_index,j,curr = [],0,0
    for i in range(N):
        curr += nums[i]
        while curr > S:
            curr -= nums[j]
            j += 1
        start_index.append(j-1)
    
    up = build(N,start_index)
    res = 0
    for i in range(N-1,-1,-1):
        res = max(res, call(up,i,K))
    return res

```
</details>

#QED

## Lowest Common Ancestor - Farach-Colton and Bender algorithm
## Solve RMQ by finding LCA

## Lowest Common Ancestor - Tarjan's off-line algorithm

-----------------------------------------
# Flows and related problems
    Maximum flow - Ford-Fulkerson and Edmonds-Karp
    Maximum flow - Push-relabel algorithm
    Maximum flow - Push-relabel algorithm improved
    Maximum flow - Dinic's algorithm
    Maximum flow - MPM algorithm
    Flows with demands
    Minimum-cost flow
    Assignment problem
    - [min XOR sum](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/)
    - hungarian algo?
Matchings and related problems
    Bipartite Graph Check
    Kuhn's Algorithm - Maximum Bipartite Matching
# Miscellaneous
## Topological Sorting
For DAGs only. Topo sort exists only if there are no cycles in the DAG.
- use dfs
- after you have exosted vertex `s`, append it as all its descendants have been visited.
- think of exit/finish times
- need to reverse answer in the end
- below version we also track if there is a cycle

<details>
<summary> <b>CODE</b> </summary>

```Python
def dfs(s,path):
    nonlocal cycle
    visited.add(s)
    for u in adj[s]:
        if u not in visited:
            dfs(u,path|{s})
        elif u in path:
            cycle = True
            return
    res.append(s) # all topo sort needs, the rest are for cycle tracking
cycle,res,visited = False,[],set()
for s in range(n):
    if s not in visited:
        dfs(s,set([s]))
if cycle: print([])
print(res[::-1])
```
</details>

#QED

## Edge connectivity / Vertex connectivity
## Tree painting
## 2-SAT
## Heavy-light decomposition