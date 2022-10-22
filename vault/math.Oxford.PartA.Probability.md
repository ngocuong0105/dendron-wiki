---
id: 3ecgdrzmxv653whgpx6jb5g
title: Probability
desc: ''
updated: 1666337128816
created: 1664832112863
---

Oxford notes for Part A probability.

# Buzzwords

Probability space $(\Theta, F, P)$ = modelling an experiment. $\Theta$ is the space of outcomes, $F$ is the space of events, $P$ gives a measure of probability.


Memoryless property of geometric and exponential distributions = kvot bilo bilo.

close connections between the Poisson distribution and the exponential distribution - think Poisson processes.

$X_n \rightarrow X$ almost surely (with probability 1) implies convergence in probability implies convergence in distribution.

WLLN

Weak law of large numbers is limit in probability. Proven using Chebyshev's inequality (requires finite variance)

This assumption of finite variance is not necessary (just makes proves easier). Large or infinite variance will make the convergence slower, but the LLN holds anyway.

Strong Law of Large Numbers (SLLN) is almost sure convergence.

CLT, converges in distribution. The fluctuations of the mean $X_n$ around $\mu$ is of order $1/\sqrt{n}$

risk pooling (used in CLT) $S_n = X_1 + ... X_n$, where $X_1 ... X_n$ are different portfolios (iid assumption!). 

Binomial with small probability and many events is poisson

Binomial = sum of Beornoulli. If fixed $p$, then by CLT Binomial converges to Normal distribution. Consider $W_n ~ Bin(n,p_n)$, where $p_n$ converges to 0. Assume the expected total number of successes stays approximately the same $np_n = \lambda$. Then Binomial converges to Poisson. 


# Chapter 1. Recap Prelims


- (i) $Ω$ is a set, which we call the sample space.
- (ii) $F$ is a collection of subsets of $Ω$. An element of $F$ is called an event.
- (iii) The probability measure $P$ is a function from $F$ to [0, 1]. It assigns a probability to each event in $F$.

A **random variable** is a function defined on $Ω$. Maps events to numbers.

cdf, pdf, discrete and cts random variables, variance, covariance

independence, $P(A \cup B \cup C) = P(A)P(B)P(C)$. pairwise indepence is weaker than independence.


If $X ∼ Gamma(rX , λ)$ and $Y ∼ Gamma(rY , λ)$ are independent, then we have $X + Y ∼ Gamma(rX + rY , λ)$. As a special case, if $X_1 , X_2 , . . . , X_n$ are i.i.d. with $Exp(λ)$ distribution,
then $X_1 + X_2 + · · · + X_n$ has $Gamma(n, λ)$ distribution.

Memoryless property of geometric and exponential distributions.


If $X ∼ Poisson(λ)$ and $Y ∼ Poisson(µ)$ are independent, then $X + Y ∼ Poisson(λ + µ).$



# Chapter 2. Convergence of random variables and limit theorems.

We need to formalise the notion that two random variables $X$ and $Y$ are close.

**Modes of convergence**

Let $X_1, ... X_n, X$ be random variables. We say:

$X_n$ converges to $X$ **almost surely (with probability 1)** if
$P(X_n \rightarrow X \text{ as } n \rightarrow \infty) = 1$

$X_n$ converges in **probability** to $X$ if for every $\epsilon > 0$: $P(|X_n - X| < \epsilon) \rightarrow 1 \text{ as } n \rightarrow \infty$.

$X_n$ converges to $X$ in **distribution**(weakly) if $F_n(x) \rightarrow F(x)$ as $n \rightarrow \infty$ for all $x$ where $F(x)$ is continuous.

These formulations are in decresing order of strength. The last one does not require distributions to be the same! This is really a definition about convergence of distributions, not about convergence of random variables.

**There are many situations in which a sequence of discrete random variables converges to a continuous limit.**

WLLN in convergence in probability.

$S_n  = X_1 + ... X_n$, where $X_1, ... X_n$ are iid with finite variance. Then:

$P(|\dfrac{S_n}{n}  - \mu| < \epsilon) \rightarrow 1$ as $n \rightarrow \infty$
proove it using Chebyshevs inequality.

CLT - convergence in distribution (standard normal). The fluctuations of $S_n = X_1 + ... + X_n$ around $n\mu$ is of order $\sqrt{n}$.

Binomial with small probability and many events is poisson

Binomial = sum of Beornoulli. If fixed $p$, then by CLT Binomial converges to Normal distribution. Consider $W_n ~ Bin(n,p_n)$, where $p_n$ converges to 0. Assume the expected total number of successes stays approximately the same $np_n = \lambda$. Then Binomial converges to Poisson. 