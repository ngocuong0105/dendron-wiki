# https://leetcode.com/problems/coin-change-2/submissions/
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        def dp(amount, i):
            if i == 0:
                return 0
            if amount == 0:
                return 1
            elif amount < 0:
                return 0
            if memo[amount][i] != None:
                return memo[amount][i]
            memo[amount][i] = dp(amount, i - 1) + dp(amount - coins[i - 1], i)
            return memo[amount][i]

        memo = [[None] * (len(coins) + 1) for a in range(amount + 1)]
        return dp(amount, len(coins))
