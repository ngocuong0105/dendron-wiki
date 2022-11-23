---
id: 575nhoxd9zglbmn3y4gmcnz
title: Algebra
desc: ''
updated: 1669103747579
created: 1664382729044
---
    Fundamentals
        Binary Exponentiation
        Factoring Exponentiation
        Euclidean algorithm for computing the greatest common divisor
        Extended Euclidean Algorithm
        Linear Diophantine Equations
        Fibonacci Numbers
    Prime numbers
        Sieve of Eratosthenes
        Linear Sieve
        Primality tests
        Integer factorization
# Number-theoretic functions
## Euler's totient function
## Number of divisors / sum of divisors
    
## Lagrange's four-square theorem
Any number can be represented by at most 4 squares. Check proof in wikipedia.
- [least squares sum](https://leetcode.com/problems/perfect-squares/)

    
    Modular arithmetic
        Modular Inverse
        Linear Congruence Equation
        Chinese Remainder Theorem
        Factorial modulo p
        Discrete Log
        Primitive Root
        Discrete Root
        Montgomery Multiplication
#Number systems
## Balanced Ternary
## Gray code
- [permute binary representation](https://leetcode.com/problems/circular-permutation-in-binary-representation/)

Note how graycode construction adds 0-s and 1-s(reverses these) in the previous solution
```python
class Solution:
    def circularPermutation(self, n: int, s: int) -> List[int]:
        graycode = [i ^ (i >> 1) for i in range(1<<n)]
        i = graycode.index(s)
        print(graycode)
        return graycode[i:]+graycode[:i]
    
class Solution:
    def circularPermutation(self, n: int, s: int) -> List[int]:
        return [s ^ i ^ (i >> 1) for i in range(1<<n)]
    
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # my construct of consecutive bits add 0 and 1 to previous solution
        # this is the same as gray code...
        def dp(i):
            if i == 1: return ['0','1']
            res,rev = [],[]
            for code in dp(i-1):
                res.append('0'+code)
                rev.append('1'+code)
            return res + rev[::-1]
        res = dp(n)
        res = [int(b,2) for b in res]
        i = res.index(start)
        return res[i:] + res[:i]
```

It's not obvious why $n ^ (n>>1)$ and $(n+1) ^ ((n+1)>>1)$ would differ by 1 bit.


# Miscellaneous
        Enumerating submasks of a bitmask
        Arbitrary-Precision Arithmetic
        Fast Fourier transform
        Operations on polynomials and series
        Continued fractions