# https://leetcode.com/problems/range-sum-query-2d-mutable/ z tre6ww  lution/
from typing import List


class NumMatrix:
    def __init__(self, mat: List[List[int]]):
        # build O(n*m*logn*logm)
        # self.mat = [[0]*len(mat[0]) for _ in range(len(mat))]
        # self.bit = [[0]*(len(mat[0])+1) for _ in range(len(mat)+1)]
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         self.update(i,j,mat[i][j])

        # build O(n*m)
        self.mat = mat
        self.bit = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        for i in range(1, len(self.bit)):
            for j in range(1, len(self.bit[0])):
                self.bit[i][j] += mat[i - 1][j - 1]

        for i in range(1, len(self.bit)):
            for j in range(1, len(self.bit[0])):
                if self.next(i) < len(self.bit):
                    self.bit[self.next(i)][j] += self.bit[i][j]

        for i in range(1, len(self.bit)):
            for j in range(1, len(self.bit[0])):
                if self.next(j) < len(self.bit[0]):
                    self.bit[i][self.next(j)] += self.bit[i][j]

    def next(self, i):
        return i + (i & -i)

    def parent(self, i):
        return i - (i & -i)

    def update(self, i: int, j: int, val: int) -> None:
        diff = val - self.mat[i][j]
        self.mat[i][j] = val
        i += 1
        j += 1
        while i < len(self.bit):
            jj = j
            while jj < len(self.bit[0]):
                self.bit[i][jj] += diff
                jj = self.next(jj)
            i = self.next(i)

    # self.query(0,0) -> mat[0][0]
    def query(self, i, j) -> int:
        i += 1
        j += 1
        res = 0
        while i:
            jj = j
            while jj:
                res += self.bit[i][jj]
                jj = self.parent(jj)
            i = self.parent(i)
        return res

    def sumRegion(self, i: int, j: int, x: int, y: int) -> int:
        return (
            self.query(x, y)
            - self.query(x, j - 1)
            - self.query(i - 1, y)
            + self.query(i - 1, j - 1)
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
