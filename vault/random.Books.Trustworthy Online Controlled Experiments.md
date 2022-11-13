---
id: pn4b2d4br8xn0y2dh1sgor4
title: Trustworthy Online Controlled Experiments
desc: ''
updated: 1668369436218
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



# 5. Speed Matters

Measure impact of performance improvements by slowing down artifitially your feature and run A/B test.

Assume that the metrc(e.g revenue) has linear dependence on the performance. This assumption is reaistic locally (for small performance improvements like miliseconds.)

**Measuring Page Load time of search engine.**

1. The user makes a request at time $T_0$ by typing a query into the browser.
2. The request takes time to reach the server at time $T_{1}$, $T_{1}-T_{0}$ is super small and hard to measure.
3. On receiving the request the server typically sends the first chunk of HTML at time $T_{2}$. It is often independent of the request (e.f. query or URL). It returns the header. navigation elemtns etc. It tells the user his request was received. User receives this chunk at time $T_{3}$.
4. At time $T_{4}$ the server sends the rest of the page and the other chunks of HTML. At time $T_{5}$ user receives all chunks
5. At time $T_{6}$, the browser fires the Onload event, indicating the page is ready. It makes a log request from the server. At time $T_{7}$ the server receives the log request (user clicks, scorlls, hovers).

The Page load time is $T_{0}-T_{6}$ which we estimate with $T_{1}-T_{7}$ (stuff happening on server side).


**Slowdown experiment design**

Best is to slowdown the experiment when the server finishes computing Chunk2 which is the URL dependent HTML - as if it took longer to compute it.


Above is the real performance. User experience **perceived performance** - denoting the idea that users stat to interpret the page once enough of it is showing. E.g. can measure the time to first result instead of displaying all results.

# 6. Organizational Metrics

Objectives and Key Results (OKRs).

Objecties represent long-term goals and Key results short-term goals.

Types of metrics:

- **Goal metrics** reflect what the organization ultimately cares about. Need to articulate your goal in words. Goal metrics are proxies to what you really want to achieve. 

- **Driver metrics** tend to be short-term faster-moving and more sensitive metrics than goal metrics. HEART(HAppiness, Engagement, Adoption, Retention and Task Success). PIRATE framework (AARRR! Acquisition, Retention, Referral, Revenue)., user funnel.

- **Guardrail metrics** guard agains violated assumptions and come in two types: metrics that protect the busness and that assess the trustworthiness of experiments. These metrics make sure there is balance in all metrics.

The same metric may play different role in different teams. Some teams use latency and performance as guardrail metric. That is if you ship new feature and have revenue as driver metric you want to make sure you don't loose a lot on performance. Infrastructure teams might have these swapped.

**Asset vs engagement metrics:** asset metrics are static (number of users), engagement are dynamic and measure the valuea a user receive

**Business vs operational metrics:** business metrics are (daily average users (DAU), revenue per user) track busniess health. Operational are (queries per second) track operational concerns

You want your goal metrics to be **simple and stable**.

You want your driver metrics to be:
- alligned with the goal
- actionable and relevant
- sensitive
- resistant to gaming

**Always remember that metrics are proxies!**, e.g. simply driving high CTR might result in clickbaits.


example metrics: bounce rate(ratio of users went back - away from your content)

example gurdrail metrics(organizational):
- HTML responcse size per page
- Client crashes
- latency

these are metrics that usually most teams should NOT affect.





















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

# 19. The A/A Test

A/A test is a sanity check. Establishes trust in your experimentation platform.

Split users in two identical groups and do A/A test. If the system is operating correctly then in repeated trials about 5% of the time a given metric hould be statistically significant with p-value less than 5%.

When conducting t -tests to compute p-values, the distribution of the p-values from repeated trials should be *uniform distribution*.

A/A tests benefits:
- ensure Type I error are controlled (within 5%)
- assess metrics variability - larger variance in metric means you need to run longer the A/B test to detect the minimum detectable effect
- no bias between Control and Treatment (especially if you reuse populations from previous experiments - no carry-over effect)
- good first validation step
- distribution mismatch, platform anomalies
- catch wrong variance estimates (if you underestimate the variance you would have large t statistic hence reject Null too often)
- catch when independence assumption is violated (and wrong variance estimate)
- skewed distribution (normal assumption violated)

Run A/A test in parrallel and continously with other experiments.

You dont need new data to run many A/A tests. Just split the data again and again.

The p-values should follow iniform distribution.

Use **goodness-of-fit** such as Anderson-Darling or Kolmogorov-Smirnoff to check if it is uniform distribution

If there is a large p-value of around 0.32, then you might have an outlier. $T = \dfrac{\delta}{\sqrt{var(\delta)}}$ would be around 1 as the outlier would swamp all other values.

# 20 Triggering for Improved Sensiitivity

Sensitivity, Power, Variance are all related.

Users are triggered into the analysis of the experiment if there is (potentially) difference for this user when being in the varaint they are in or the counterfactual.

Example: Wnat to test a new checkout UI. We should trigger the experiment for only users who initiated checkout.

Example: Chage free shopping cart from 25$ to 35$. The triggered users shold be only those who have shopping cart between 25$ and 35$. Only they differ.

When analyzing only triggered users you might need smaller sample sized to reach the same power(high sensitivity) of the experiment.

Triggering only relevant users reduces the noise in the data.


**Trigerring Trustworthiness**

1. Check SRM (Sample ratio). If the overall experiment has no SRM, then the triggered data should not have SRM too.
2. Complement analysis. Run A/B test on the **non**- triggerred users. You should get A/A test results.

**Overall Treatment Effect**

When computing Treatment effect on the triggered population, you must *dilute* the effect to the overall user base.

Diluting depends on the triggering metric!

Example. Improving revenue metric with 3% on 10 % of users.

- If the triggered users were those who initiated checkout (and that's the only way to make money), then the overall revenue increased by 3%.
- If the trigerred users were those who spend 10% of the average user, then the improved revenue is 3%*10%*10% = 0.03%

**Open questions**

1. Should we take data prior tirggerring point? If you take it you oose a bit statistical power. If you do not take it you might have abnormal metrics. Clicks prior checkout to be 0.
2. Plotting a metric over time with increasing numbers of users usually leads to false trends. Best look at graphs over time where each day shows the user who visited that day. Same problem with triggered users. 100% of users who visited first day were triggered. Smaller portion on second day (as thoe visited first day would not trigger). Best compute triggered user ratio for each day - users who visited that day and were triggered that day. **Issue** is that you need overall Treatment for all days not day per day.

# 21. Sample Ratio Mismatch 

SRM is used as a **guardrail metric** making sure your experiment design holds (all assumptions are plausible).

SRM looks at the ratio of users between two variant (Treatment and Control) and checks if it is similar to the experimental design sample ratio.

Example: we expect 1:1 ratio and get:
- Contol: 821,588 users
- Treatment: 815,482 users

we need to run test to check if the p value is significant or not. If it is significant then we have SRM and probaly all other metrics outputed from the experiment would be wrong.

Causes of SRM:
- Buggy randomization of users
- data pipeline issues (bot's filtering)
- residual effect (say we ran expirement and it had a bug. We fix the bug, avoid re-randomization and run the experiment again)
- bad trigger condition

Other trust related guardrail metrics:
- cache hit rates
- click tracking (web beacons)
- cookie write rate

# 22. Leakage


SUTVA = Stable Unit Treatment Value Assumption states that the behaviour of each unit in the experiment is unaffected by variant assignment of other units.

between variants **interference** = violation of SUTVA = data leakage = spillover

units might have direct or indirect connection
- direct connection in networks (friends)
- indirect (shared resources, e.g ads budget, CPU) 

when there is interference between data in variants applying treatment might affect control group as well. So the delta estimation would be wrong.

Shared resources example: Say we apply new feature in Airbnb and Treamnet users book more. Revenue generated in Treatment increases, but the number of free rooms decreases which affects the revenue of the control. We would overestimate the treatment effect.


Tackle data leakage:
- Isolation (group by geography, time, clusters). When randomizing A/B test take one point per group (decreases the power of the test)
- Evaluate the effect of data leakage:
    - total messages send and responded to
    - total number of posts created and total number of likes/cmments these posts receive
these metrics can measure the downstream impact = measure spillover by measuring the first-order impact.

# 23. Measuring Long-Term Treatment Effects

Experiments running for one or two weeks measure short-term effects. Our goal is to design experiments and measure short-term effects which can generalize to long-term effects.

Poor generalization examples:
- showing poor search results, would initally make users search more, but long term they might abandon the search engine
- showing many low quality, might initially work and ahve higher CTR and revenue, but long term not

Reasons why the treatment effect may differ between short-term and long-term:
- user-learned effects. User adapt to change. If the search engine or the reccomendation system give bad results users may try it initially, but abandon in the long term. On the other hand if the new feature is useful but complex, they may need time to discover the usefulness.
- network effects. Treatment effect takes time to propagate through the whole network. Or initial propagationg may result in good results but once it finishes it is no good anymore. For example 'People you may know' feature in Linkdin. Changing the rec algo may improve simply because you reccommend new people.
- delayed experience and measurement. In Airbnb people can book in advance by several months.
- ecosystem changes:
    - other new features are launched
    - seasonality
    - competitive landscape

One way to measure long term effect is to run the experiment for longer time, and the last delta you get is what you consider as the long term delta.

Caveat: The longer you run the experiment the more likely you will have data leakage:
- users may start using the feature from multiple devices
- netwrok effect would propagate
- treatment effect dilution

The longer yourun the experiment the higher survivorship bias you might have.

**Alternative methods for Long-Running Experiments**

1. Cohort Analysis - divide data using stable ID (addressing survivorship bias and data leakage). You can track for each cohort the bias and leakage.

Need to combine results from different cohorts in the end

2. Post-Period Analysis.

You have Control and Treatment for time $T$. Then you turn off the new feature for all users.

For time $T$ to $T+1$ you check the *learning effect.* There are two types:
- user-learning effect (say you added more ads in treatment and they are used to clicking adds. Then after time T users from treatment might continue clicking lots of ads)
- system-learning effect. Your ML models have better parameters.

3.  Time-staggered Treatments

The experiments so far require to wait 'enough' time before taking the long-term measurement. How to decide what is enough?

Run the same treatment to two variants where one lagged, i.e. we have 2 starting times $t_{0} = t$, $t'_{0} = t+1$.

You have effectivle A/A test where the second A is has the treatment effect 1 period less.

When your test statistic are the same (running A/A test), i.e the p-valu is not significant, you can say that is enough.

Assumes over time the difference between the statistics converges to 0

4. Holdback and reverse experiment

Runng long time and experiment might cost a lot. Not releasing the feautre to the control group might lead to missed opportunities.

Thus you can consider *holdback* - i.e. leave 10% control group and 90% Treatment. You loose a bit of power of the test though.

*reverse experiment*. Release for all the treatment and after some time reverse 10% back to Control. Problem is control group might be confused.