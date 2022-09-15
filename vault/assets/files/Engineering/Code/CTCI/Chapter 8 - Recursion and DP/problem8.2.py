def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    def dp(i, j):
        if memo[i][j] != None:
            return memo[i][j]
        val = 0
        for x, y in adj(i, j, obstacleGrid):
            val += dp(x, y)
        memo[i][j] = val
        return memo[i][j]

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    memo = [[None] * n for _ in range(m)]
    memo[m - 1][n - 1] = 1
    if obstacleGrid[0][0] == 1:
        return 0
    return dp(0, 0)


def adj(i, j, obstacleGrid):
    res = []
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    k = 1
    if i + k < m and obstacleGrid[i + k][j] == 0:
        res.append((i + k, j))
    if j + k < n and obstacleGrid[i][j + k] == 0:
        res.append((i, j + k))
    return res
