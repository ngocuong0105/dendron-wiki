---
id: 575nhoxd9zglbmn3y4gmcnz
title: Algebra
desc: ''
updated: 1689162244719
created: 1664382729044
---
# Fundamentals
        Binary Exponentiation
        Factoring Exponentiation
        Euclidean algorithm for computing the greatest common divisor
        Extended Euclidean Algorithm
        Linear Diophantine Equations
## Fibonacci Numbers
- [express k as a minimum number of Fibonacci numbers](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)

**Math behind why greedy works**

Among all resolution with the minimum number of Fibonacci numbers, we are to find the lexicographically largest one.

Facts about shortest sequence:
- uses each Fibonacci number at most once `fibo[i] * 2 = fibo[i - 2] + fibo[i + 1]`
- never uses two consecutive Fibonacci numbers

Then: If no dup, no adjacent, we must take the biggest.

`fibo[0] + fibo[2] + fibo[4] + ... + fibo[2n] = fibo[2n + 1] - 1`

`fibo[1] + fibo[3] + fibo[5] + .... + fibo[2n-1] = fibo[2n] - 1`


# Prime numbers
## Sieve of Eratosthenes

- [leetcode problem](https://leetcode.com/problems/closest-prime-numbers-in-range/)
```python
sieve = [False,False]+[True]*(r-2)
for i in range(2,int(r**0.5)+2):
    for j in range(i*i,r+1):
        sieve[j] = False
primes = [i for i,p in enumerate(primes) if p]
```

- find all primes less or equal to n
```python
primes = []
for d in range(2,n+1):
    for p in primes:
        if d%p == 0: break
    else:
        primes.append(d)
```

        Linear Sieve
        Primality tests
        Integer factorization
# Number-theoretic functions
## Euler's totient function
## Number of divisors / sum of divisors
    
## Lagrange's four-square theorem
Any number can be represented by at most 4 squares. Check proof in wikipedia.
- [least squares sum](https://leetcode.com/problems/perfect-squares/)

    
# Modular arithmetic
## Modular Inverse

A [modular multiplicative inverse](http://en.wikipedia.org/wiki/Modular_multiplicative_inverse) of an integer $a$ is an integer $x$ such that $a \cdot x$ is congruent to $1$ modular some modulus $m$.
To write it in a formal way: we want to find an integer $x$ so that 

$$a \cdot x \equiv 1 \mod m.$$

We will also denote $x$ simply with $a^{-1}$.

It can be proven that the modular inverse exists if and only if $a$ and $m$ are relatively prime (i.e. $\gcd(a, m) = 1$).

**Finding the Modular Inverse using Binary Exponentiation**

```python
pow(a,m-2,m)  # m must be prime/Fermat's little theorem
```

* For an arbitrary (but coprime) modulus $m$: $a ^ {\phi (m) - 1} \equiv a ^{-1} \mod m$
* For a prime modulus $m$: $a ^ {m - 2} \equiv a ^ {-1} \mod m$

**Finding the Modular Inverse using Extended Euclidean algorithm**

Use the identity eqaution (linear diophantine equation in two variables)

$$a \cdot x + m \cdot y = 1$$

Take modulu m both sides and you get the result.

The function below solves $ax+by = 1$, for given $a$ and $b$.
```python
def extended_euclidean(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = extended_euclidean(b, a % b)
        return y, x - (a // b) * y, gcd
```
[why this works](https://math.stackexchange.com/questions/747342/extended-euclidean-algorithm-for-modular-inverse)



## Linear Congruence Equation
## Chinese Remainder Theorem
## Factorial modulo p
## Discrete Log
## Primitive Root
## Discrete Root
## Montgomery Multiplication
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

It's not super obvious why $n$ XOR $(n>>1)$ and $(n+1)$ XOR $((n+1)>>1)$ would differ by 1 bit.

XOR is commulative. we need to prove that $n$ XOR $(n>>1)$ XOR $(n+1)$ XOR $((n+1)>>1)$ is a power of two.

$n$ XOR $(n>>1)$ and $(n+1)$ XOR $((n+1)>>1)$ $=$ $n$ XOR $(n+1)$ and $(n>>1)$ XOR $((n+1)>>1)$ $=$ $2^{k} - 1$ XOR $2^{k-1} - 1$

## Finding inverse Gray code

Given Gray code $g$, restore the original number $n$, i.e. $g = n^(n>>1)$, given $g$ find $n$

We will move from the most significant bits to the least significant ones (the least significant bit has index 1 and the most significant bit has index $k$). The relation between the bits $n_i$ of number $n$ and the bits $g_i$ of number $g$:

$n = n_{k}n_{k-1}...n_{1}$ in binary presentation $n_{i} \in \{0,1\}$

Rewrite $n = g$ XOR $n>>1$ to get:

$$\begin{align}
  n_k &= g_k, \\
  n_{k-1} &= g_{k-1} \oplus n_k = g_k \oplus g_{k-1}, \\
  n_{k-2} &= g_{k-2} \oplus n_{k-1} = g_k \oplus g_{k-1} \oplus g_{k-2}, \\
  n_{k-3} &= g_{k-3} \oplus n_{k-2} = g_k \oplus g_{k-1} \oplus g_{k-2} \oplus g_{k-3},
  \vdots
\end{align}$$

```python
def gray_to_dec(g):
    res = 0
    while g:
        res ^= g
        g >>= 1
    return res
```
# Miscellaneous
        Enumerating submasks of a bitmask
        Arbitrary-Precision Arithmetic
        Fast Fourier transform
        Operations on polynomials and series
        Continued fractions