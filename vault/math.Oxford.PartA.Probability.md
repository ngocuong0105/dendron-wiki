---
id: 3ecgdrzmxv653whgpx6jb5g
title: Probability
desc: ''
updated: 1666882967185
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


generating functions are used to compute moments and pmfs. Take kth derivative and evaluate at 0 or 1.

Pgf-s used for discrete random variables $E(z^{X})$.

Mgf-s used for continuous random variables $E(e^{tX})$.

Mgfs and Pgfs define uniquely the distribution of random variables.

For $M_{X_1},M_{X_2} ... M_{X_n}$ if $M_{X_n} \rightarrow M_{X}$ then $X_{n} \rightarrow X$ in distribution as $n \rightarrow \infty$.


Proof WLLN CLT using mgfs and above fact

Chebyshev’s inequality, which is the application of Markov’s inequality to the random variable $(X − \mu)^2$.

Markovs inequality is about bouding the tails of non-negative distributions.
$P(X>a) \leq \dfrac{E(X)}{a}$


Fact: For standard normal random variable $P(X > 3) \approx 10^{-3}$

Markov chain is a sequence of variables satisfying the Markov property

$P(X_{n+1} = i_{n+1} | X_n = i_n ,..., X_0 = i_0) = P(X_{n+1} = i_{n+1} | X_n = i_n)$.


To describe a time homogeneous Markov chain you need the initial distribution of $X_0$ and a **transition matrix** $P = (p_{ij})_{i,j \in I}$

The matrix $P$ is indexed by the state space $I$. $P$ has non-negative entries and each row sums to 1.

Markov chains are memoryless.

Chapman-Kolmogorov equations

irreducible chains, communicating classes, closed class, periodicity of classes

recurrence, transience, mean return time, null recurrence, positive recurrence

null recurrent = mean return time is infinite but probability of goiing back infinitely many times is 1.

in a class all states are either positive recurrent or null recurrent, or transient

Random walk on $\Z^{d}$ is a irreducible chain with period 2.



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

# Chapter 3. Generating functions

The generating function of random variable $X$ is $G(z) = E(z^{X})$

Using generating dunctions you can compute moments and the pmf of $X$. Take kth derivative and evaluate at 0 or 1.

**Theorem 3.2** (Uniqueness theorem for probability generating functions). If X and Y have the same generating function, then they have the same distribution.


Generating functions for independen rvs: $G_{X+Y}(z) = G_{X}(z)G_{Y}(z)$

Generating functions used for random sums: $G_{S}(z) = G_{N}(G_{X}(z))$

**Probability genrating functions** are used for discrete random variables!


**Moment generating function** of a random variable is $M_X{t} = E(e^{tX})$

Mgf is Pgf with  $z = e^t$

We use $e^{t}$ because we can expand around $t=0$. If we expand around $z=0$ we would no longer have power series in the general case for cts variables.

Assuming the mgf exists (the expecation is finite), Taylor expansion:

$M_{X}(t) = \sum_{k=0}^{\infty} \dfrac{t^{k}E(X^k)}{k!}$

$M_{X}^{(k)}(0) = E(X^{k})$


Mgfs and Pgfs define uniquely the distribution of random variables.

For $M_{X_1},M_{X_2} ... M_{X_n}$ if $M_{X_n} \rightarrow M_{X}$ then $X_{n} \rightarrow X$ in distribution as $n \rightarrow \infty$.


Fact For standard normal random variable $P(X > 3) \approx 10^{-3}$.

**Characteristic functions**

Replace in mgf $t$ with $it$

$\phi_{X}(t) = E(e^{itX}) = E(cos(tx)) + iE(sin(tX))$.

Results for mgf hold for cgf too.

**Mgf vs Cgf**

Cgf does not require exponentially decaying tails (it is all on complex plain). Mgf to proove CLT uses exponential decay (finite expectation).

Mgf could be used to show bounds of tails (using Markov inequality, see section 3.3). CGf just does not makes sense as we use complex numbers and cannot compare them.

# Chapter 4. Joint distributions of continuous random variables



# Chapter 5. Markov chains

Let $X = (X_0 , X_1 , X2 , ...)$ be a sequence of random variables taking values in some state space $I$. The process $X$ is called a Markov chain if for any $n \geq 0$ and any $i_0 , i_1 , . . . , i_{n+1} \in I$,

$P(X_{n+1} = i_{n+1} | X_n = i_n ,..., X_0 = i_0) = P(X_{n+1} = i_{n+1} | X_n = i_n)$.

The Markov chain is called **(time) homogeneous** if in addition $P(X_{n+1} = j| X_{n} = i)$ does not depend on $n$. Then $p_{ij} = P(X_{n+1} = j| X_{n} = i)$ and these are called **transition** probabilities of the chain.

To describe a time homogeneous Markov chain you need the initial distribution of $X_0$ and a **transition matrix** $P = (p_{ij})_{i,j \in I}$

The matrix $P$ is indexed by the state space $I$. $P$ has non-negative entries and each row sums to 1.

Markov chains are memoryless.

We can say that “the future is independent of the past, given the present”.

**Theorem 5.2. (Chapman-Kolmogorov equations)**

- To reach from $i$ to $k$ in $m+n$ steps try middle: $p_{ik}^{m+n} = p_{ij}^{m} p_{jk}^{n}$
- To reach from $i$ to $j$ in $n$ steps: $p_{ij}^{n} = (P^n)_{i,j}$ 

**Theorem 5.3** If $\lambda$ is the initial distribution, then the distribution of $X_n$ is $\lambda P^{n}$.


**Class structure** of state space of Markov chains.

We say state $i$ communicates with state $j$ if we can reach from $i \rightarrow j$, that is $p_{ij}^{n}$ is positive for some $n$ (after certain number of steps we can reach from $i$ to $j$) and vice verca.

A class of states $C$ is **closed** if the probability to go out of the class is 0.

If the class $\{i\}$ is closed then we call it an **absorbing state**.

A state $I$ is **irreducible** if all states communicate (can reach from elsewhere to everywhere).

**Period** of a state $i$ is the least number of steps after which you will be back and back and back ... in $i$, that is the gcd of the set $\{ n \geq 1: p_{ii}^{n}\}$, if it does not exist (never go back, p_{ii}^{n} = 0)then the period is not defined.

$i$ is called **aperiodic** if this g.c.d. is 1. Example: go back in 1, 3, 7 steps

**Fact. All states in a communicating class have the same period.**
In particular, if a chain is irreducible, then all states have the same period.

**Hitting probabilities**

Define $h_{i}^{A} = P_{i}(X_{n} \in A \texttt{for some} n \geq 0)$, the hitting
probability of $A$ starting from state $i$. If $A$ is a closed class we call that the **absorbtion probability**.

**Recurrence and transience**

$P_{i}(X_{n} = i \texttt{for some } n \geq 1) = p \leq 1$ equivalently
$P_{i}(\texttt{git } i \texttt{ infinitely often}) = 0$. The state $i$ is called transient.

$P_{i}(X_{n} = i \texttt{for some } n \geq 1) = 1$ equivalently
$P_{i}(\texttt{git } i \texttt{ infinitely often}) = 1$. The state $i$ is called recurrent.

**Theorem 5.9** In a recurrent class: either all states are recurrent or all are transient.

Every recurrent class is closed. Every finite closed class is recurrent.


The theorem tells us that recurrence and transience are quite boring for finite chains: state $i$ is recurrent if and only if its communicating class is closed. But infinite chains are more interesting! An infinite closed class may be either transient or recurrent.

**Therem** State $i$ is recurrent iff $\sum_{n=0}^{\infty}p_{ii}^{(n)} = \infty$

**Random walk in $\Z^{d}$**

Consider a simple symmetric random walk on the $d$-dimensional integer lattice. This is a Markov chain with state space $\Z^{d}$ and transition probabilities $p_xy = 1/(2d)$ if $|x − y| = 1$, and $p_xy = 0$ otherwise. The chain is irreducible, with period 2.

For $d=1,2$ the chain is recurrent (probability of go back to 0 infinitely often is 1), and for $d \geq 3$ the cahin is transient.

**Mean Return Time to a state**

$m_{i} = E(\texttt{start from }i\textt{ and go back to }i) = 1 + \sum p_{ij}k_{j}^{i}$

where $k_{j}^{i}$ is the mean hitting time of $i$ starting from $j$

If $i$ is transient then $m_i = \infty$ (return time to itsleft is infinite with positive with probability).

If $i$ is recurrent and $m_i = \infty$, we say $i$ is **null recurrent**

If $i$ is recurrent and $m_i < \infty$, we say $i$ is **positive recurrent**

If the chain is irreducible, we can therefore call the whole chain either transient, or null recurrent, or positive recurrent.


# Chapter 6. Markov chains: stationary distributions and convergence to equilibrium

Let $\pi = (\pi_{i} , i \in I)$ be a distribution on the state space $I$.
We say that $\pi$ is a **stationary distribution**, or invariant distribution, or equilibrium distribution, for the transition matrix $P$ if $\pi P  = \pi$

$\pi$ is a **left** eigenvector of the matrix $P$ with eigenvalue 1.

That is for all $j$ $\pi_{j} = \sum_{i}\pi_{i} p_{ij}$
zzz
Stationary distributions are those for which after we move using transition matrix, the distribution does not change.


**Theorem 6.1 (Existence and uniqueness of stationary distributions)**. Let $P$ be an irreducible transition matrix.
- (a) $P$ has a stationary distribution if and only if $P$ is positive recurrent.
- (b) In that case, the stationary distribution π is unique, and is given by $\pi_{i} = 1/m_{i}$ for all $i$ (where $m_{i}$ is the mean return time to state $i$ defined at (5.12)).

**Theorem 6.2 (Convergence to equilibrium)**. Suppose $P$ is irreducible and aperiodic, with stationary distribution $\pi$. For a Markov chain with transition matrix $P$ and any initial distribution $P(X_n = j) \rightarrow \pi_{j}$ as $n \rightarrow \infty$ for all $j$.

**Theorem 6.3 (Ergodic theorem)**. Let $P$ be irreducible. Let $V_i(n)$ be the number of visits to state $i$ before time $n$.

Then $\dfrac{V_i(n)}{n} \rightarrow \dfrac{1}{m_i}$ almost surely as $n \rightarrow \infty$.

The ergodic theorem concerns the “long-run proportion of time” spent in a state.

In the positive recurrent case, the theorem says the long-run proportion of time   $\dfrac{V_i(n)}{n}$ spent in a state $i$ is the stationary probability of that state $\dfrac{1}{m_i} = \pi_{i}$.


In the null-recurrent or transient case, $1/m_{i} = 0$, so the ergodic theorem says that with probability 1 the long-run proportion of time spent in a state is 0.
zz
We can see the ergodic theorem as a generalisation of the strong law of large numbers.
The ergodic theorem can be seen as extending this to the case where Xn is not i.i.d. but is a Markov chain. IID is stronger asumption that Markov propery.


**Intuition** about the convergence theorems.


The idea will be that after a long time, a Markov chain should more or less “forget where it started”. There are essentially two reasons why this might not happen: 

- (a) periodicity; for example if a chain has period 2, then it alternates between, say, “odd” and “even” states; even an arbitrarily long time, the chain will still remember whether it started at an “odd” or “even” state. 

- (b) lack of irreducibility. A chain with more than one closed class can never
move from one to the other, and so again will retain some memory of where it started, forever

Thus for convergence to equillibrium (which does not depend on initial distribution) we require aperiodicity and irreducibility


# Poisson processes

A Poisson process is a natural model for a stream of events occuring one by one in continuous time, in an uncoordinated way.

Example:
- the process of times of detections by a Geiger counter near a radioactive source (a very accurate model)
- the process of times of arrivals of
calls at a call centre (often a good model)
- the process of times of arrivals of buses at a bus
stop (probably an inaccurate model; different buses are not really uncoordinated, for various
reasons

**Definition** A *counting process* is a random process $N_t$ for $t \in [0,\infty]$, where time $t$ is continuous and $N_t$ is a random variable which takes values in $\{1,2,3...\}$ and $N_s < N_t$ for $s < t$.

**Arrival process**

If $N_t$ describes an arrival process, then $N_t = k$ means that there hae been $k$ arrivals in the time interval $[0,t]$.

In fact we can describe the process by the sequence of arrival times, which we might call “points” of the process. Let $T_k = inf\{t ≥ 0 : N_t ≥ k\}$ for $k ≥ 0$. inf = infimum!

$T_0 = 0$, $T_k$ is the *k-th arrival time*.

Also $Y_k = T_k - T_{k-1}$ $k \geq 1$ and $Y_k$ is the **interarrival** time between $k-1$ and $k$.


For $s < t$, we write $N(s, t]$ for $N_t − N_s$ and we call this the increment process $N$ on the interval $(s,t]$ = number of arravals between $s$ and $t$.


**Definition 7.1 (Definition of Poisson process via exponential interarrival times).** $(Nt , t ≥ 0)$ is a Poisson process of rate $\lambda$ if its interarrival times $Y_1 , Y_2 , Y_3,...$ are i.i.d. with $Exp(\lambda)$ distribution.

**Definition 7.2 (Definition of Poisson process via Poisson distribution of increments).** $(Nt , t ≥ 0)$ is a Poisson process of rate $\lambda$ if:
- N_0 = 0
- If $(s_1,t_1), ... (s_k,t_k)$ are disjoint intervals $\R_{+}$, then the increments $N(s_i,t_i]$ are independent. The number of points falling in disjoint intervals is independent.
- For any $s < t$, the increment $N(s,t]$ has Poisson distribution $\lambda(t-s)$

The two definitions are equivalent. The key idea is that the memoryless property for the exponential distribution and the independent increments property are telling us the same thing.


To get more intuition for the relation between Poisson increments and exponential interarrivals, one can also think about a related discrete-time process.

- (1) If $X_n ∼ Binomial(n, λ/n)$, then $X_n → Poisson(λ)$ as $n \rightarrow \infty$. (See Example 2.9.)
- (2) If $Y_n ∼ Geometric(λ/n)$, then $Y_n/n → Exp(λ)$ as $n \rightarrow \infty$. (See Example 2.3.)

So we can see this exponential/Poisson relationship in the Pois-
son process as a limit of the geometric/binomial relationship which is already familiar from sequences of independent trials


**Theorem 7.1 (Superposition of Poisson processes)**. Let $L_t and $M_t$ be independent Poisson processes of rate $λ$ and $µ$ respectively. Let $N_t = L_t + M_t$. Then Nt is a Poisson process of rate $λ + µ$.


**Theorem 7.2 (Thinning of a Poisson process).** Let $N_t$ be a Poisson process of rate $λ$. “Mark” each point of the process with probability $p$, independently for different points. Let $M_t$ be the counting process of the marked points. Then $M_t$ is a Poisson process of rate $pλ$.


# Problem sheets

Problem sheet 3.

Q1. closed classes: $\{3\},\{1,5\}$, $\{1,2,5\}$ (1-indexd)
closed classes are always communicating classes.

$(1/5,1/10,7/20,1/5,3/20)$, for second pard need chapman kolmogorv $9/16$
raise $P^2$

Q2. $p_{ii} = 1 - (\dfrac{N-i}{N})^2 - (\dfrac{i}{N})^2, p_{i,i-1} = (\dfrac{i}{N})^2, p_{i,i+1} = (\dfrac{N-i}{N})^2$

Q3. states  6 and not 6. need to get eigenvalue decomposition and raise the transition matrix to power n. Or condition of last state $p_n = p_{n-1} \dfrac{4}{5} \dfrac{1}{5}$

$P(\texttt{return} 1 \texttt{after n steps})$ = $\dfrac{1}{5}(1-P(\texttt{return to} 6)$


