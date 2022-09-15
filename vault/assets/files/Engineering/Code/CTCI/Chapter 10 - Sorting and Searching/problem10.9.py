# Search in Sorted matrix in linear time
# O(m+n)
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
        else:
            return True
    return False


# Trivial bs
# O(mlgn)
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    for i in range(len(matrix)):
        if bs(matrix[i], target):
            return True
    return False


def bs(arr, t):
    l, r = 0, len(arr) - 1
    m = (l + r) // 2
    while l < r:
        if arr[m] >= t:
            r = m
            m = (l + r) // 2
        elif arr[m] < t:
            l = m + 1
            m = (l + r) // 2
    return arr[l] == t
