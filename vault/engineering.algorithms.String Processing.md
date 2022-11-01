---
id: tmyxaki17gpq6jb9xav1x3v
title: String Processing
desc: ''
updated: 1667292849150
created: 1664382813257
---
# Fundamentals
## String Hashing
## Rabin-Karp for String Matching
- [longest duplicate string](https://leetcode.com/problems/longest-duplicate-substring/)
        Prefix function - Knuth-Morris-Pratt
        Z-function
        Suffix Array
        Aho-Corasick algorithm
    Advanced
        Suffix Tree
        Suffix Automaton
        Lyndon factorization
# Tasks
## Expression parsing
## Manacher's Algorithm - Finding all sub-palindromes in O(N)

- Manacher, [p1](https://leetcode.com/problems/longest-palindromic-substring/), [p2](https://leetcode.com/problems/shortest-palindrome/)

<details>
<summary> <b>CODE</b> </summary>

```Python
# O(n**2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palin(i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        res = ''
        for i in range(len(s)):
            odd = palin(i,i)
            even = palin(i,i+1)
            if len(res)<len(odd): res = odd
            if len(res)<len(even): res = even
        return res

# Manacher Algorithm. Find Longest Palindrome in O(n) time.
class Solution:
    def longestPalindrome(self, s: str) -> str:  
        T = '$#'+'#'.join(s)+'#&'
        P = [0]*len(T)
        C,R = 0,0
        for i in range(len(T)-1):
            P[i] = (R>i) and min(R-i,P[2*C-i])
            while T[i+P[i]+1] == T[i-P[i]-1]:
                P[i] += 1
            if R < i+P[i]:
                C,R = i,i+P[i]
        l = max(P)
        i = P.index(l)
        return s[(i-l)//2:(i+l)//2]

```
</details>

## Finding repetitions