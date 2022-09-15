# https://leetcode.com/problems/number-of-islands/submissions/
# disjoint set implementation with array
# overcomes overhead of a hashmap
class DSU:
    def __init__(self, m, n):
        self.parent = [i for i in range(m * n)]
        self.rank = [0 for i in range(m * n)]
        self.components = m * n
        self.n = n

    def find(self, idx: int) -> int:
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]

    def union(self, x: int, y: int) -> None:
        u, v = self.find(x), self.find(y)
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u] += 1
        self.components -= 1


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dsu = DSU(m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    idx = i * n + j
                    for u, v in self.adj(i, j, grid):
                        idx1 = u * n + v
                        if dsu.find(idx) != dsu.find(idx1):
                            dsu.union(idx, idx1)
                else:
                    dsu.components -= 1
        return dsu.components

    def adj(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        res = []
        for k in [-1, 1]:
            if i + k >= 0 and i + k < m and grid[i + k][j] == "1":
                res.append((i + k, j))
            if j + k >= 0 and j + k < n and grid[i][j + k] == "1":
                res.append((i, j + k))
        return res
