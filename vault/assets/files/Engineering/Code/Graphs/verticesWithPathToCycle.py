# https://leetcode.com/problems/find-eventual-safe-states/
# DFS
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        def dfs(i, graph, color):
            if color[i] == "gray":
                return False
            if color[i] == "black":
                return True
            color[i] = "gray"
            for u in graph[i]:
                if not dfs(u, graph, color):
                    return False
            color[i] = "black"
            return True

        n = len(graph)
        color = ["white" for _ in range(n)]
        res = []
        for i in range(n):
            if dfs(i, graph, color):
                res.append(i)
        return res
