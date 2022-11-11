---
id: pn4b2d4br8xn0y2dh1sgor4
title: Trustworthy Online Controlled Experiments
desc: ''
updated: 1668151389578
created: 1667338869712
---

# 1. Intro and motivation

*One accurate measurement is worth more than a thousand expert opinions*

Simplest controlled experiments: Control(existing system) vs Treatment(existing system with feature X) (A/B test)

**OEC = Overall Evaluation Criterion** is a quantitative measure of the experiment's objective.

Examples:
- active days per user
- sessions per user
- successful sessions
- time to success
- ads revenue

**OEC should be measurable in short periods and drive long-term strategic objectives.**

Example: Profit is not good OEC metric.  Customer lifetime value is a strategically powerfull OEC.

Metrics should meet key characteristics of strategy and not be gameable.

OEC is the perfect mechanism to make the strategy explicit and to align what features ship with the strategy.

It is about matching top-down-directed perspectives with bottom-up tasks.

Glossary of terms:

**Parameter** in an experiment is a controllable variable (e.g font size). Parameter are assigned *values* also known as *levels*.

In online world common use **univariate** (one parameter) designs with multiple values (A/B/C/D tests).

**Variant** are the populations being tested - A is Control population, B is Treatment population

**Randomization Unit** is a process to map units (users) to their variants. Need:
- **persistency** same user should experience consistenly the same variant
- **independence** assigning users to one variant should not affect the assignment probabilities of oher users 

No factor should be allowed to influence variant assighment.

**Correlation foes not imply causality!**

Example: Microsoft Office 365 observes lower churn rate by users who see more error messages. Does not mean Microsoft should show more errors.

The reason for this corelation is simply **usage**. Users who use MSOffice more see more messages and have lower churn rate.

Controlled experiments give scientific framework to:
- establish causality with high probability
- detect small changes
- detect unexpected changes


**Ingredients for Controlled Experiments:**

1. Enough experimental units (users) divided into variants randomly
2. Key metrics, OEC.
3. Cahnges are easy made (e.g software changes in algorithms vs aviation engineering system change)

Agile + Controlled experiments + MVP is good combination

Useful concept to have in mind EVI (expected value of information). Running a failed MVP has value.

Experiments evauluate ideas (people could be very poor at this)

Experiments usually make small many improvements over time. 10% improvemnt for 5% of users is 0.5% overall improvement

Winning is done inch by inch.

Always have a protfolio of ideas:
- most should optimize near the current location (maximize your current hill)
- but a few should be radical (whether we can move to a bigger hill)

Big jumps to other hills (big site redesigns) usually fail. It is a high risk high reward endevour.

Two things to consider when making big jumps:

- The duration of the experiment. Need to overcome **primacy** effect (users are primed to the old design). Run longer the experiment.
- The number of ideas tested. In big jumps you make lots of changes. Some ideas might be really bad and cancel the really good ideas (which you would not see that are good).



# 2. Running and analysing experiments

This chapter contains an example of setting up, running and analysing results of an experiment

Experiment **setup/design**: 

**Hypothesis**: Adding a coupon code field to the checkout page will degrade revenue.

**OEC**: Profit itself is bad metric as it depends on the number of users in each variant. Revenue-per-user is better.

What should be in the denominator?

- all users: valid but would be quite noise. Lots of users will never initiate checkout
- only users who complete purchase process. Wrong. The more users purchase the lower metric??
- only users who start the purchase process. That's the most accurate denominator. Includes all potentially affected users.

**Refined hypothesis:** Adding a coupon code field to the checkout page will degrade revenue-per-users who start the purchase process.

Decide what **statistical significance** p-value to use.

Statistical significance means whether the observed result is by chance or not.

However, in practice we need **practical significance** - does it make sense from business stand point to make the change?

practical significance is usually larger than statistical significance. If you are on start-up you would like to have larger practical significance say 10% where as big businesses like Google with billions of revenue  the 0.2% change is practically significant

**randomization unit** - usually these are users

**size** - how large in size should be the population. Larges smaple size needed to detect smaller changes. alternatively you can reduce the variance in the data, e.g. use *purchase indicator* (1 if user buys 0 if not) instead of revenue as OEC and that would have lower variance data, detect easier.

detecting larger changes requires less data

lower p-value rtequires larger data

size ~ variance, minimum detectable effect needed, p-value

**power** of the test

**time** - how long do we run thhe experiment

- more time = more users
- day-of-week effect (seasonality)
- primacy and novelty effects


**Results of experiment**

- do sanity checks for trustworthiness of your experiment

some metrics should be the same in all variants, e.g. latency

to catch errors looks at invariants between Treatment and Control datasets


**Launch/no-launch**

Desisions take into considerations the results of the experiment as well as broader context:

- different metrics tradeoffs, e.g. if CPU utilization usage increases, is the cost of running the new service worth? 
- cost of launching the change (sometimes all the cost is in the setup experiment, sometimes there are add ons)
- what is the downside of making the wrong decision/risks


The decisions are usually three way:

Launch, no-launch and continue testing.

- statistical, practical significance -> launch
- no statistical significance, no practical significance -> no launch
- statistical significance, no practical significance -> no launch/continue testing

# 3. Twyman's Law and Experimentation Trustworthiness

**Twyman's Law: "Any figure that looks interesting or different is usually wrong."**

Extreme resultss are more likely to be result of an error:
- in instrumentation (logging)
- loss/duplication of data
- computational error

Hypothesis testing depends on
- significance level/value ($\alpha = 0.05$, that's Type 1 error(false positives))
- power (high power = low Type 2 error (false negatives)), high power = catch Alternative hypothesis if it is true 
- minimum detectable effect
- sample size

**Mistakes:**

**A common mistake is to assme that low significance value = no Treatment effect.** It migh be just that our test is **underpowered**.

Need to ensure you have enough power to detect a change of that magnitude or smaller.


**p-value != probability of $H_{0}$ is true.** p-value is GIVEN $H_{0}$ how likely is we observe AS EXTREME VALUE AS the current test statistic value.

p-value computes on CONDITIONING

**[Peeking at p-values](https://towardsdatascience.com/wish-tackles-peeking-with-always-valid-p-values-8a0782ac9654)**

Running online experiments and make conclusiong before reaching the sample size you need. Might lead to infalted false positive rates (underpowered tests).


Fix it using always valid p-values method

**Multiple Hypothesis testing**

Multiple hypothesis vs single Null

Bonferronni correction (conservative). Need it as high probability of false negatives (high probability of incorrectly rejecting the null)


Duality between confidence intervals and p-values. For Null hypothesis that the threatment has no effect, a 95% CI containing a zero is equavalent to having significat p value 0.05%

95% CI is referring to the fact that if you run the experiment many times and compute the CI, then 95% of the time you will catch the TRUE value.

**Threat to internal Validity** - is your experiment trustworthy?

Careful about:

**SUTVA** (Stable Unit Treatment Value Assumption):
- **spillover effect** (networks have this problem)
- two-sided markets (lowering prices in Treatment might affect the Contol buy side)
- shared resources (CPU, storage, cache)


**Survivor bias**


**SRM - Sample Ratio Mismatch**

The size of the variants must be close to the designed ratio! Good place to do sanity checks.

Small imbalances might change your result completely (reject null to not reject null)

In practice it is easy to have this wrong:

- browser redirects (e.g. links can be send by certain users to other users etc. better use **server side mechanism**)
- gathering data (the way you define stuff like clicks)
- bots (automatic filtering)
- residual or carryover effects from previous experiments
- time-of-day effect (if you send mail campaign for control in working hours and treatment in non-working hours)


**Threats to External Validity** - are your experiments generalizable

Generalizing across population is rarely applicable.

Threats:
- primacy effect (attached to the old)
- novelty effect (excited for the shiny)

Catch these effects by ploitting traffic over time.


Viewing metrics by segments!

- market or country
- device type
- time of dayweek
- user characteristcs


**Analysis by segments can be wrong** - thats when you add rates and averages.

For two segments the OEC can increase for both but decrease overall due to migration from one segment to another.

average 20 sessions-per-user use feature F, average 10 users-per-session not use feature F

If users who use F have 15 sessions and stop using it, then both OES metrics would increase, overall would decrese.

**Simpson's Paradox**

Run experiment for two phases and in each the OEC increase. But overall it deacreases
$\dfrac{a}{b} < \dfrac{A}[B], \dfrac{c}{d} < \dfrac{C}[D]$ but $\dfrac{a+c}{b+d}<\dfrac{A+C}{B+D}$


Good data scientists are sceptic! Invoke Twyman's Law.

# 4. Experimentation Platform and Culture

Phases of experimation maturity models:

- Crawl (1-10 experiments/year) - fundamental capabilities, instrumentation, data analytics/science
- Walk (50 experiments/year) - validating your experiments + defining metrics
- Run (250 experiments/year) - codifying your OEC, run experiments at scale
- Fly (1000+ experiments/year) - do not launch anything before running an experiment, automation ,institutional memory, learning form past experiments, automation

To add experimentation in an organization need learship buy-in espessially in Crawl and Wal phases to define OEC and set up fundamentals


Infrastructure:

- Experiment definition, setup, management via UI, or API, store configurations
- experiment deployment, both server and client side - variant assignment and parametrization
- experiment instrumentation (logging, triggers, alerting, automation)
- experiment analysis, aggregate, clean, statistical tests, p-values, power analysis, visualization

*Iterations* - progressively roll out new features to many users (not all at once).

Scaling experimentation:
- need multiple experiments and assign same user to many experiments (multi-layer method)
- need to do lots of monitoring
- deal with interactions between experiments


# 17. The stattistics behind Online Controlled Experiments

**Two-sample** t-tests look at the size of the difference between the means *relative* to the variance.

The significance of the difference is measured using p-value

The lower the p-value the strnger evidence that the Treatment is different from the Control.

$T-statistic = \dfrac{\delta}{\sqrt{var(\delta)}}$

$\delta = \bar{Y_t} - \bar{Y_c}$ 

t-statstic $T$ is normalized version of $\delta$

Intuitively, the larger t, the less likley the means are the same, the more likely we reject the Null hypothesis.

**p-value**

This is the probability we observe as extreme as the observed $\delta$ given $H_{0}$ is True

$P(H_{0}|\delta observed) = \dfrac{P(H_{0} is True)}{P(\delta observed)} \times P(\delta observed| H_{0} is True) = \dfrac{prior}{likelihood} \times p-value$

95% CI is equivalent to p-value of 0.05. If 0 is not in the 95% CI, we reject the null hypothesis (p-value is significant and is less than 0.05).


**Normality assumption** when doing t test is for the average $\bar{Y}$, not the sample $Y_{i}$.

This assumption holds for large $n$ by the CLT.

Rule-of-thumb is to use $355s^2$ data points where $s$ is the skewness coefficient.

To reduce skewness - transform the metrics or cap them.

To be more confident if normality assumption holds test in offline simulation.

Shuffle samples across Treatment and Control and test for normality using **Kolmogorov-Smirnov** and **Anderson-Darling**.


**Type I/II errors and Power**

- Type I error: false positives (reject Null incorrecly)
- Type II error: false negatives (do not reject Null incorrectly)

Tradeoff between the two errors:

higher p-value threshold -> higher Type I error but lower Type 2 error

You control Type I error by setting the significance level p-value $\leq 0.05$.

$Type II error = 1 - Power$

Power = probability detecting difference(reject null) when there is indeed difference.

Power is usually parametrized by $\delta$ = the minimum delta of practical interest

$Power_{\delta} = P(|T| \geq 1.96| true difference is \delta)$

**power analysis**

To achieve enough power (industry standard of 80%) you need approximately $n = \dfrac{16 \sigma^2}{\delta^{2}}$

We do not know the true difference $\delta$ so we use **practical difference**, known as the **minimum detectable effect**.

Want to spot big difference need less power.


**Bias = when the estimate and the true value of the mean are systematically different.**

**Multiple Testsing problem** When you have many alternative hypothesis, your probability of false discoveries increases (false positive).

Simple way to fix it is reducing the p-value threshold (Bonferroni correction).

Similar problem appears when you have many many metrics. "Why is this irrelevant metric significant?"

Here you can separete the metrics in groups and assign varying p-value thresholds.


**Fisher's Meta-analysis**

Combining results (p-values) from multiple experiments with the same hypothesis.

Fisher's method:

$\chi_{2k}^{2} = -2 \sum_{i=1}^{k}ln(p_{i})$

$p_i$ is p-value from $i-$th experiment.

Fisher's method increases the power and reduces the false-positives of your experiment.


do orthogonal replications of the experiment and apply Fisher's method.

# 18. Variance estimation and Improved sensitivity

**Variance estimation is the core of experiment analysis**

incorrect estimate of variance leads to incorrect p-value and confidence interval.

overestimated varaince leads to false negatives (reject when we should have) and underestmated variance leads to false positives


**Delta vs Delta %**

percent delta is the relative difference $\delta \% = \dfrac{\delta}{\bar{Y_{c}}}$

1% session increase more meaningful than 0.01 increase per user.

$var(\delta \%) = \dfrac{var(\bar{Y_{t}}-\bar{Y_{c}})}{\bar{Y_{c}}} = var(\dfrac{\bar{Y_{t}}}{\bar{Y_{c}}})$

estimate it using the delta method (taylor expansion etc.)


variance of Ratio metrics can be estimated using delta method or bootstrap method.

**Ratio metric. When analysis unit is didfferent from the experiment unit**

**NB ASSUMPTION** the varaince formula $var(Y) = \dfrac{1}{n-1}\sum(Y_{i}-\bar{Y})^2$ is true when $Y_i$ are iid.

If $Y_{i}$ is CTR per user, or other measurement by user, then this assumtion does not hold!

NB: Rmove outliers before computing variance.

Improving sensistivity = Higher power

Achieve this by reducing variance in the data.
- create an evaluation metric with smaller variance while capturing similar information (instead of purchase price, is_purchase)
- transform metric, cap ,log
- triggered analysis
- stratification, CUPED
- randomize on more gradular unit


Varaince of other statistics (such as quantiles, not only the mean.)

Use bootstrap. By estimating the density you can estimate the variance.