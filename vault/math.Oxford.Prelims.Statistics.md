---
id: q7gonhx2ncjvh8vr9qpwlaq
title: Statistics
desc: ''
updated: 1667238410675
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

**Example.** Estimating the TRUE variance and stadard deviation of the sample population.

- Let $X_1,...,X_n ∼ N(\mu, \sigma^{2})$ be iid. Then $\hat{\mu} = \bar{X}$ and estimate of the variance is $var(\hat{mu}) = \dfrac{\sigma^{2}}{n}$ and standard deviation $SE(\hat{\mu}) = \dfrac{\sigma}{\sqrt(n)}$

The variance and SE of an estimator $\hat{\mu}$ might themself depend on anothe paramater. We need to plug in $\hat{\sigma}$ with the Maximum likelihood estimator (divides by $n$) or other estimate (sample variance divides by $n-1$ and is **unbiased**).


**Given a radnom normally distributerd sample, when constructing  a confidence interval you should use the sample variance. If you use the MLE to estimate the $\sigma$ you will underestimate the variance and your CI would be shrinked**

$\hat{\mu} \pm z_{\alpha/2}\dfrac{\hat{\sigma}}{\sqrt{n}}$


# Linear Regression

Suppose we measure two variables in the same population:
- $x$: the **explanatory variable, predictor, feature, input**
- $y$: the **response variable, output**


A linear regression model for the dependence of $y$ on $x$ is:

$y_{i} = \alpha + \beta x_{i} + \epsilon_{i}$


where:
- $x_1,...,x_n, y_1...,y_n$ are known constants (data points)
- $\epsilon_1,..., \epsilon_{n}$ are i.i.d. $N(0,\sigma^{2})$ "random errors"
- $α, β$ are unknown parameters.
The “random errors” represent random scatter of the points $(x_i, y_i)$ about the line $y = α + βx$, we do not expect these points to lie on a perfect straight line.


**Note: a linear relationship like this does not necessarily imply that $x$ causes $y$.**

**Goal: estimate $\alpha$ and $\beta$**

$Y_i ~ N(\alpha+\beta x_i,\sigma^{2})$

Maximize the likelihood $L(\alpha,\beta|x_i,y_i)$. Same as minimizing the square error $S(\alpha,\beta) = \sum_{i=1}^{n}(y_i-\alpha-\beta x_i)^2$!

Vectorized linear regression problem: Estimate $\beta$ for $\bf{y} = \bf{X}\beta + \epsilon$ (intercept is included as a col of ones)

Vectorized solution $\hat{\beta} = (X^{T}X)^{-1}X^{T}y$ it is an unbiased estimator!

95\% CI for the true parameter $\beta$ is $(\hat{\beta} \pm 1.96 SE(\beta))$

The standard deviation of the true parameter $SE(\beta)$ is usually unknown and we need to estimate it.

$var(\beta) = X^{T}X var(y) = X^{T}X \sigma^{2}$

You can use the The MLE: $\hat{\sigma}^{2} = \dfrac{1}{n}\sum(y_i-x_i\beta)$ to get 95\% CI: $(\hat{\beta} \pm z_{\alpha/2}\SE(\beta))$ 

A better approach is to estimate $\sigma^{2}$ using $\dfrac{1}{n-p}\sum(y_i-x_i\beta)$ because this is an unbiased estimator (on average you are correct) and to base the confidence interval on a t-distribution rather than a normal distribution

[example](https://stats.stackexchange.com/questions/29981/should-confidence-intervals-for-linear-regression-coefficients-be-based-on-the-n)

# Assessing model fit

Having fitted a model = estimated the parameters $\beta$.

Having fitted a model, we should consider how well it fits the data. A model is normally an approximation to reality: is the approximation sufficiently good that the model is useful?

**Definition.** The i-th fitted value is $\hat{y_i} = x_{i}\hat{\beta}$

The i-th residual is $e_{i} = y_{i}-\hat{y_{i}}$

The RSS (residual sum of squares) is $RSS = \sum e_{i}$

The RSE (residual standard error) is $RSE = \sqrt{\dfrac{RSS}{n-p}}$ (this is an estimate of the standard deviation $\sigma$).


**Potential problem: non-linearity**

A **residual plot** is a useful graphical tool for identifying non-linearity: for simple linear regression we can plot the residuals $e_i$ against the fitted values $\hat{y_{i}}$ . Ideally the plot will show no pattern. The existence of a pattern may indicate a problem with some aspect of
the linear model.


**Potential problem: non-constant variance of errors**

Non-constant variance is also called **heteroscedasticity**.
Can see funnel-type shape in the residual plot.

How might we deal with non-constant variance of the errors?
- One possibility is to transform the response Y using a transformation such as $log(Y)$ or $\sqrt{Y}$ (which shrinks larger responses more), leading to a reduction in heteroscedasticity.
- If you know how variances behave for $Y_i$ and think $var(Y_i)=var(\epsilon_i) = \sigma^{2}/w_{i}$ you can take the approach called weighted least squares minimizing $\sum_{i=1}^{n}w_i(y_i-x_i\beta)$

**Potential problem: outliers**

An outlier is a point for which $y_{i}$ is far from the value $\hat{y_i}$ predicted by the model.


If we believe an outlier is due to an error in data collection, then one solution is to simply remove the observation from the data and re-fit the model. However, an outlier may instead indicate a problem with the model, e.g. a nonlinear relationship between $Y$ and $x$, so care must be taken.

studentized residuals = standardized residuals greater than 3 is signal for outlier

**Potential problem: high leverage points**

(Trailstone group interview...)

Outliers are observations for which the response $y_i$ is unusual given the value of $x_i$. 

On the other hand, observations with high leverage have an unusual value of $x_i$ .

**Definition** the leverage of the ith observation is $h_{i}$ where

$h_{i} = \dfrac{1}{n} + \dfrac{(x_i - \bar{x})^{2}}{\sum (x_j-\bar{x})^{2}}


Take-away: Points with high residuals pull the regression line towards them more than points with lower residuals (the more $\hat{y_i}$ are wrong the more the line goes towards them)

Points with unusual value of $x_i$ far from the mean pull ht regression line a lot too. These are called high leverage points.


Why does this matter? We should be concerned if the regression line is heavily affected by just a couple of points, because any problems with these points might invalidate the entire fit. Hence it is important to identify high leverage observations.


# Data Analysis

Linear regression is an example of supervised learning $Y ~ X$.

In unsupervised learning you have only $X$. In this case you want to answer questions:

1. Can we find a way to visualize the data that is informative?
2. Can we compress the dataset without losing any relevant information?
3. Can we find separate subgroups (or clusters) of observations that de-
scribe the structure of the dataset?

Unsupervised learning can be more challenging than supervised learning,
since the goal is more subjective than prediction of a response variable.

Exploratory data analysis is unsupervised learning.

data matrix = design matrix

First step in modelling - EDA

Inter Quartile Range (IQR) - the difference between the 1st and 3rd quartiles. This is a measure of ‘spread’ within the dataset.

Box plot.

![box_plot.png](assets/images/box_plot.png)

Pair plots

3D interactive plots

**Simulation** is a technique for generating pseudo-random values that have a particular distribution.


# The Multivariate Normal Distribution


# PCA


# Clustering