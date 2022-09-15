# 8.12
# https://leetcode.com/problems/n-queens/submissions/
# Very educational problem about backtracking
import copy


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [None] * n

        def backtrack(curr):
            if curr == n:
                res.append(copy.deepcopy(board))
            for i in range(n):
                if not self.conflict(i, curr, board):
                    board[curr] = i
                    backtrack(curr + 1)
                    board[curr] = None

        def convert_sol(res):
            ans = [["."] * len(res) for i in range(len(res))]
            for i in range(len(res)):
                ans[res[i]][i] = "Q"
            for i in range(len(ans)):
                ans[i] = "".join(ans[i])
            return ans

        res = []
        backtrack(0)
        ret = []
        for ls in res:
            ret.append(convert_sol(ls))
        return ret

    def conflict(self, i, j, board):
        return (
            self.checkRow(i, j, board)
            or self.checkCol(i, j, board)
            or self.checkDiag(i, j, board)
        )

    def checkRow(self, i, j, board):
        for num in board:
            if num == i:
                return True
        return False

    def checkCol(self, i, j, board):
        return board[j] != None

    def checkDiag(self, i, j, board):
        for k in range(len(board)):
            if board[k] != None and abs(i - board[k]) == abs(j - k):
                return True
        return False
