---
id: pn4b2d4br8xn0y2dh1sgor4
title: Trustworthy Online Controlled Experiments
desc: ''
updated: 1667498220800
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

Experiments usually make small many improvements over time. 10\% improvemnt for 5\% of users is 0.5\% overall improvement

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

practical significance is usually larger than statistical significance. If you are on start-up you would like to have larger practical significance say 10\% where as big businesses like Google with billions of revenue  the 0.2\% change is practically significant

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

