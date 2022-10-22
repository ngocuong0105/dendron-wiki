---
id: yh0ww8ogawf7n4n2q2lnsus
title: Graphs
desc: ''
updated: 1666353719541
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

    Dijkstra - finding shortest paths from given vertex
    Dijkstra on sparse graphs
    Bellman-Ford - finding shortest paths with negative weights
    0-1 BFS
    D´Esopo-Pape algorithm
All-pairs shortest paths
    Floyd-Warshall - finding all shortest paths
    Number of paths of fixed length / Shortest paths of fixed length
Spanning trees
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
- below is for cycle in directed graph, for **undirected** need to keep parent pointers and make sure you when you go back to parent you don't consider it as cycle

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

#QED

## Finding a Negative Cycle in the Graph


## Eulerian Path



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

Euler path


## Lowest Common Ancestor - Binary Lifting
Binary tree lifting is also known as jump pointers. Idea: Number of powers of two is logarithmic. [Errihto](https://www.youtube.com/watch?v=oib-XsjFa-M&t=579s&ab_channel=Errichto).

With Binary tree lifting you can answer questions such as given a tree, what is its k-th ancestor.

**Define** $u[v][j]$ is the $2^j$-th ancestor of v.

$u[v][j]$ is the $2^j$-th ancestor of v.
$u[v][0] = parent[v]$ - that is my first parent
$u[v][1] = u[u[v][0]][0]$ - what is my second parent? first parent of my first parent
$u[v][2] = u[u[v][1]][1]$ - what is my fourth parent? second parent of my second parent

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
    
print(lca(p,q)) # lowest common ancestor
```
</details>


#QED

## Lowest Common Ancestor - Farach-Colton and Bender algorithm
## Solve RMQ by finding LCA
##Lowest Common Ancestor - Tarjan's off-line algorithm
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