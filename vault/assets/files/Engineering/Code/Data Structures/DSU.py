# Complexity:
# If we make N requestis to the union method it would take
# O(alpha(N)) amortised time per ops and alpha is the Inverse-Ackermann function. This is approximately constant
# To perform a sequence of m addition, union, or find operations on a disjoint-set forest with n nodes requires total time
# O(mα(n)), where α(n) is the extremely slow-growing inverse Ackermann function.
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    # path compression
    def find(self, idx: int) -> int:
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]

    # keep tree's rank small
    def union(self, x: int, y: int) -> None:
        u, v = self.find(x), self.find(y)
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u] += 1
