---
id: q7gonhx2ncjvh8vr9qpwlaq
title: Statistics
desc: ''
updated: 1667063508229
created: 1664832112863
---
# Buzzwords

# Introduction. Random samples. Summary Statistics, MLE

Probability: in probability we start with a probability model $P$, and we deduce properties of $P$.

E.g. Imagine flipping a coin 5 times. Assuming that flips are fair and independent, what is the probability of getting 2 heads?

Statistics: in statistics we have data, which we regard as having been generated from some unknown probability model $P$. We want to be able to say some useful things about $P$.


**Definition.** A random sample of size $n$ is a set of random variables $X_1 , . . . , X_n$ which are independent and identically distributed (i.i.d.).

often you will compute the joint pmf of $X_1,...,X_n$. This joint pmf gives you the probability you observe the sample data $x_1,...,x_n$,

In probability we assume that parameters $λ$ and $µ$ in our two examples are known. In statistics we wish to estimate $λ$ and $µ$ from data.
- What is the best way to estimate them? And what does “best” mean?
- For a given method, how precise is the estimation?

**Sample mean** and **Sample variance**, **sample standard deviation**

Denominator in sample variance is $n-1$, so that the sample variance will be what is called an **unbiased** estimator of the population variance. If we divide by $n$ our sample variance would be underestimating the TRUE variance on average.
_
Given observations $x_1,...,x_n$ we can compute the observed values $x$ and $s^2$ .

We use sample mean, variance, standard deviation to estimate the TRUE unknown mean, variance, standard deviation.

![summary_stats.png](assets/images/summary_stats.png)

**MLE = Maximum Likelihood Estimation**
Maximum likelihood estimation is a general method for estimating unknown parameters from data.


**Definition.** Let $X_1,...,X_n$ have joint p.d.f./p.m.$f(x; θ)$. Given observed values $x_1,...,x_n$ of the **likelihood** of $θ$ is the function:
$L(θ) = f (x; θ)$

$L(\theta)$ is the joint pmf, pdf of the observed data and is regarded as a function of $\theta$ for fixed **$x$**.

Definition. The maximum likelihood estimate (MLE) is the value $\hat{\theta}$ that maximizes the likelihood $L(\theta)$ (or log-likelihood).


The idea of maximum likelihood is to estimate the parameter $\theta$ that gives the greates likelihood to the obsrvations $x_1,...,x_n$.



Estimator:
- A rule for constructing an estimate.
- A function of the random variables $X$ involved in the random sample.
- Itself a random variable.
Estimate:
- The numerical value of the estimator for the particular data set.
- The value of the function evaluated at the data $x_1,...,x_n$.

# Parameter estimation


**Definition.** A **statistic** is any function $T(X)$ of $X_1,...,X_n$ that does not depend on $\theta$.

**Definition.** An **estimator** of $θ$ is any statistic $T(X)$ that we might use to estimate $θ$.

**Definition.** $T(x)$ is the **estimate** of $θ$ obtained via $T$ from observed values $x$.


We can choose between estimators by studying their properties. A good estimator should take values close to the TRUE parameter $θ$.

**Definition.** An estimator $T=T(X)$ is **unbiased** for $\theta$ if $E(T) = \theta$. This means that “on average” $T$ is correct.


**Definition.** The mean squared error (MSE) of an estimator $T$ is defined by $MSE(T) = E[(T − θ)^2].$

**Definition.** The bias $b(T)$ of $T$ is defined by $b(T) = E(T) − θ$.

MSE is a measure of the **“distance”** between $T$ and the true parameter $θ$

However $MSE(T)$ and $b(T)$ may depend on $\theta$.

Note $MSE(T) = var(T) + b(T)^2$ (bias variance trade-off)

So an estimator with small MSE needs to have small variance and small bias.


MLEs are usually asymptotically unbiased, and have MSE decreasing like $1/n$ for large $n$.

**USE MSE(T)** to compare different estimators for $\theta$.

# Accuracy of estimation: Confidence Intervals

A crucial aspect of statistics is not just to estimate a quantity of interest, but to assess how accurate or precise that estimate is. One approach is to find an interval, called a confidence interval (CI) within which we think the true parameter falls.


**Definition.** If $a(X)$ and $b(X)$ are two statistics, and $0 < α < 1$, the interval $(a(X), b(X))$ is called a confidence interval for $θ$ with confidence level $1 − α$ if, for all $θ$:

$P(a(X) < θ < b(X)) = 1 − α$

The interval $(a(x), b(x))$ is called an interval estimate and the random interval $(a(X), b(X))$ is called an interval estimator.

Note: $a(X)$ and $b(X)$ do **not** depend on $θ$.

We want small intervals and $P(a(X) < \theta < b(X))$ to be large.


By the same argument as before, if $X_1 , . . . , X_n ∼ N(µ, σ_{0}^{2})$ with $σ_{0}^{2}$ known, then a level $1 − α$ confidence interval for $µ$ is

$(\bar{X}-\dfrac{z_{\alpha/2} \sigma_{0}}{\sqrt{n}}, \bar{X}+\dfrac{z_{\alpha/2} \sigma_{0}}{\sqrt{n}})$

The more data I have the smaller interval I get!

if variance is unknown use **SAMPLE VARIANCE** (division by $n-1$).

**Interpretation of a Confidence Interval**

- The parameter $\theta$ is fixed but unknown.
- If we imagine repeating our experiment then we’d get new data, **$x'$**
say, and hence we’d get a new confidence interval $a(x'), b(x')$. If we did this repeatedly we would “catch” the true parameter value about $95\%$ of the time, for a $95\%$ confidence interval: i.e. about 95% of our intervals would contain $θ$.
- The confidence level is a coverage probability, the probability that the random confidence interval $a(X), b(X)$ covers the true θ. (It’s a random interval because the endpoints $a(X), b(X)$ are random variables.)

You always get confidence interval estimates. You cannot say $(523,3313)$ is 95\% confidence interval. It either does or does not contain the TRUE parameter $\theta$. You cant say which as $\theta$ is unknown.


**Confidence Intervals using the CLT**


(estimate ± 2 estimated std errors)is an approximate 95% CI
(estimate ± 3 estimated std errors)is an approximate 99.8% CI.