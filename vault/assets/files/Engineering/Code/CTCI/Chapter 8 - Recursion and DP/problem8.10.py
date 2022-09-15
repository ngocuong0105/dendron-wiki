# classic dfs
# careful for cycles
def floodFill(
    image: list[list[int]], sr: int, sc: int, newColor: int
) -> list[list[int]]:
    color = image[sr][sc]
    m, n = len(image), len(image[0])
    visited = set()

    def dfs(row, col):
        if row < 0 or row >= m or col < 0 or col >= n or image[row][col] != color:
            return
        if (row, col) not in visited:
            image[row][col] = newColor
            visited.add((row, col))
            for k in [-1, 1]:
                dfs(row + k, col)
                dfs(row, col + k)

    dfs(sr, sc)
    return image
