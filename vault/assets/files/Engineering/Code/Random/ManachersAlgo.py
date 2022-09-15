# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = "#".join("!" + s + "*")
        C, R = 0, 0
        P = [0] * len(T)
        for i in range(1, len(T) - 1):
            P[i] = (R > i) * min(P[2 * C - i], R - i)
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        length, idx = max((n, i) for i, n in enumerate(P))
        return s[(idx - length) // 2 : (idx + length) // 2]
