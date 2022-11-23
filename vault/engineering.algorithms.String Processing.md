---
id: tmyxaki17gpq6jb9xav1x3v
title: String Processing
desc: ''
updated: 1669232735937
created: 1664382813257
---
# Fundamentals
## String Hashing
## Rabin-Karp for String Matching
- [longest duplicate string](https://leetcode.com/problems/longest-duplicate-substring/)
## Prefix function - Knuth-Morris-Pratt

**Definition** You are given a string  $s$  of length  $n$ . The prefix function for this string is defined as an array  $\pi$  of length  $n$ , where  $\pi[i]$  is the length of the longest proper prefix of the substring  $s[0 \dots i]$  which is also a suffix of this substring.

$\pi[i] = \max_ {k = 0 \dots i} \{k : s[0:k] = s[i-k+1:i+1] \}$

For example, prefix function of string "abcabcd" is  $[0, 0, 0, 1, 2, 3, 0]$ , and prefix function of string "aabaaab" is  $[0, 1, 0, 1, 2, 2, 3]$ 


Brute force algo to compute $\pi$ is $O(n^3)$
```python
def compute_prefix(s):
    pi = [0]*len(s)
    for i in range(len(s)):
        for k in range(i):
            if s[:k] == s[i-k+1:i+1]:
                pi[i] = k
    return pi
```

**First optimization**

Observe $\pi(i+1)$ is at most 1 larger than $\pi(i)$. Thus when moving to the next position, the value of the prefix function can either **increase by one, stay the same, or decrease by some amount**. 

Algo: In total the function can grow at most  $n$  steps, and therefore also only can decrease a total of  $n$  steps. This means we only have to perform  $O(n)$  string comparisons, and reach the complexity  $O(n^2)$ .


**Second optimization**

*no string comparisons*

Let us compute $\pi[i]$. Notice that $\pi[i] = \pi[i-1] + 1$ iff $s[i] == s[\pi[i-1]]$

$\underbrace{\overbrace{s_0 ~ s_1 ~ s_2}^{\pi[i]} ~ \overbrace{s_3}^{s_3 = s_{i+1}}}_{\pi[i+1] = \pi[i] + 1} ~ \dots ~ \underbrace{\overbrace{s_{i-2} ~ s_{i-1} ~ s_{i}}^{\pi[i]} ~ \overbrace{s_{i+1}}^{s_3 = s_{i + 1}}}_{\pi[i+1] = \pi[i] + 1}$

goal is to find largest $j \leq \pi[i-1]$ such that $s[i] = s[j]$

$\overbrace{\underbrace{s_0 ~ s_1}_j ~ s_2 ~ s_3}^{\pi[i]} ~ \dots ~ \overbrace{s_{i-3} ~ s_{i-2} ~ \underbrace{s_{i-1} ~ s_{i}}_j}^{\pi[i]} ~ s_{i+1}$

```python
def KMP(s):
    pi = [0]*len(s)
    for i in range(1,len(s)):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi
```
$O(n)$ complexity as we increase $pi[i]$ at most $n$ times and decrease it at most $n$ times. No string comparisons.

$pi$ is called prefix function = longest preffix suffix (LPS)

**Problems**

[Search for a substring in a string](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

<details>
<summary> <b>Idea</b> </summary>
Search substring t in string s:

Apply KMP(t+'#'+s) # use the hashtag for cases such as s = 'aaa', t = 'aa'
</details>

**Counting the number of occurrences of each prefix**

Given a string  $s$  of length  $n$ . In the first variation of the problem we want to count the number of appearances of each prefix  $s[0 \dots i]$  in the same string. 

```python
def solve(s):
    pi = KMP(s)
    res = [0]*(len(s)+1)
    for i in range(len(s)):
        res[pi[i]] += 1
    for i in range(len(s)-1,0,-1):
        res[pi[i-1]] += res[i]
    for i in range(len(s)+1):
        res[i] += 1
    return res[1:]
```

[The number of different substring in a string](https://cp-algorithms.com/string/prefix-function.html#counting-the-number-of-occurrences-of-each-prefix)


<details>
<summary> <b>Idea</b> </summary>
We will solve this problem iteratively. Namely we will learn, knowing the current number of different substrings, how to recompute this count by adding a character to the end.

We take the string  $t = s + c$  and reverse it. Now the task is transformed into computing how many prefixes there are that don't appear anywhere else.

Therefore the number of new substrings appearing when we add a new character  $c$  is  $|s| + 1 - \pi_{\text{max}}$ .
</details>

## Z-function
## Suffix Array
## Aho-Corasick algorithm
## Suffix Tree
## Suffix Automaton
## Lyndon factorization
# Tasks
## Expression parsing
## Manacher's Algorithm - Finding all sub-palindromes in O(N)

- Manacher, [p1](https://leetcode.com/problems/longest-palindromic-substring/), [p2](https://leetcode.com/problems/shortest-palindrome/)
- [maximum product of two palins](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/)
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
            if R > i: # P[i] = (R>i) and min(R-i,P[2*C-i]) slows down
                P[i] = min(R-i,P[2*C-i])
            while T[i+P[i]+1] == T[i-P[i]-1]:
                P[i] += 1
            if R < i+P[i]:
                C,R = i,i+P[i]
        l = max(P)
        i = P.index(l)
        # P[2:-2:2] returns the sizes of largest palindrom for each i being the center (only odd length palindromes!)
        #P[2:-2] returns sized of largest palindromes (odd and even)
        return s[(i-l)//2:(i+l)//2]

```
</details>


- using Manacher to query if substring is palindome in `O(1)` per query

```Python
def Manacher(s):
    T = '$#'+'#'.join(s)+'#&'
    P = [0]*len(T)
    C,R = 0,0
    for i in range(len(T)-1):
        if R > i: 
            P[i] = min(R-i,P[2*C-i])
        while T[i+P[i]+1] == T[i-P[i]-1]:
            P[i] += 1
        if R < i+P[i]:
            C,R = i,i+P[i]
    return P[2:-2]

def palin(i,j):
    if j > len(s): return False
    l = j-i
    c = 2*((i+j)//2)-(l%2==0)
    return P[c] >= l
P = Manacher(s)
palin(i,j) # returns if s[i:j] is a palindrome
```

## Finding repetitions