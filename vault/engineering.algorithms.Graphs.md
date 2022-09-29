---
id: yh0ww8ogawf7n4n2q2lnsus
title: Graphs
desc: ''
updated: 1664446403746
created: 1664382861926
---

# Graph traversal
    Breadth First Search
    Depth First Search
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

## Finding Bridges Online

## Finding Articulation Points in $O(N+M)$
- [leetcode](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/)
- [explanation](https://cp-algorithms.com/graph/cutpoints.html)

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
    Strongly Connected Components and Condensation Graph
    Strong Orientation

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
Cycles
    Checking a graph for acyclicity and finding a cycle in O(M)
    Finding a Negative Cycle in the Graph
    Eulerian Path
Lowest common ancestor
    Lowest Common Ancestor
    Lowest Common Ancestor - Binary Lifting
    Lowest Common Ancestor - Farach-Colton and Bender algorithm
    Solve RMQ by finding LCA
    Lowest Common Ancestor - Tarjan's off-line algorithm
Flows and related problems
    Maximum flow - Ford-Fulkerson and Edmonds-Karp
    Maximum flow - Push-relabel algorithm
    Maximum flow - Push-relabel algorithm improved
    Maximum flow - Dinic's algorithm
    Maximum flow - MPM algorithm
    Flows with demands
    Minimum-cost flow
    Assignment problem
Matchings and related problems
    Bipartite Graph Check
    Kuhn's Algorithm - Maximum Bipartite Matching
Miscellaneous
    Topological Sorting
    Edge connectivity / Vertex connectivity
    Tree painting
    2-SAT
    Heavy-light decomposition