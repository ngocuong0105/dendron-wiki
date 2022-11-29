---
id: 0qjr95oigreiv0ihjlwgtcz
title: Run Experiements
desc: ''
updated: 1669657804648
created: 1669630575598
---
# Experiment Design

Write a PEP (Product Enhancement Proposal) document.

1. The title should state the what, not the how. For example: Improve search results CTR vs Show restaurants with most reviews first. 
2. User/Business problem + opportunity size
3. hypothesis (should have a measurable goal), if we do this then we expect this to happen
4. description
5. measure success/metrics
6. experiment timing (e.g. depends on power = probability of detecting difference between cohorts if there is a true difference)
    - power analysis
7. Cohort allocation (how much users each cohort gets and how it gets it, i.e user X is exposed to treatement y iff the user does someting/is of certain type etc.)
    - general rule for $k$ treatments - $x\%$  to the control (status quo group) and $\dfrac{1-x}{k}\%$ for each treatment, where $x = \dfrac{\sqrt{k}-1}{k-1}$ (the pooled standard deviation of a t-test is minimized )


Question. An experimenter is creating an AB experiment on Beaker and they want to implement several runs with a treatment allocation first at 1%, then 5%, then 10%, then 50%, because the engineers are worried about the new feature tested breaking things. What should you do?

Recommend that they only do 1 “smoke test” for a few days, and then do the normal experiment run with a 50%-50% allocation (control group - treatment).

# Metrics

You should list all decision and secondary metrics that will be computed. When it comes to experiments, we should favor metrics that have a low standard deviation (thus resulting in more statistical power), and that are directly related to/close to the change being tested.

We want metrics which have clear **directional** meaning. The average number of searches is not a great metric because a change is hard to interpret. Users might not find what they want on our app and might need to do many searches to get a result they like (in which case an increase in searches is a negative signal), or conversely they really love our app and use it more, resulting in more searches (a positive signal).

# Power analysis

Power analysis determines how many samples must be observed to run the hypothesis test, which subsequently informs the experiment run time.

The Power of an experiment is defined as:

‘the probability of detecting a change of MDE%, given that it truly exists’, 

where MDE% = the Minimum Detectable Effect of the experiment.

Higher power = lower false negative (large p-value = not significant)

false negative is when you say incorrectly that the p-value is large and do not detect the difference

power eqaul to 80% = for 1 in 5 experiments where a change of MDE% did occur, we would not detect it as a significant change and would experience a False Negative result. 

[power analysis formulas](http://powerandsamplesize.com/Calculators/Test-1-Mean/1-Sample-Equality)

number of observations (required data size) depends on variance, z-quantiles, mean difference between hypothesises

Power calculations are based on the type of metric (average, proportion) you will measure in your experiment. Power here is calculated assuming a t-test in a frequentist approach for averages, chi-squared test for proportions. A Bayesian approach takes much longer to calculate and returns equivalent values for the types of experiments we run.

```python
from statsmodels.stats.power import tt_ind_solve_power
```

Run the solver

Run the following cell to return the parameter that was set to `None`, for example the nobs1. This would return the number of samples needed in the largest cohort.
```python
result = tt_ind_solve_power(
    effect_size=effect_size,
    alpha=alpha,
    alternative=alternative,
    nobs1=nobs1,
    power=power,
    ratio=ratio
)
round(result, 0)
```

If the MDE is increased, what is the impact on the experiment run time will decrese.

Decreasing the significance level from 95% to 80% would result in:
- a shorter experiment run time
- a higher false positive rate
- narrower confidence interval

What does the relationship between metric variance and sample size required look like? **linear**


# Multiple Comparisons

When we make multiple comparisons, such as when there is more than one treatment cohort or more than one metric we are testing, we increase alpha, meaning we increase the chance of false positive results. These increases can add up quite rapidly, meaning that looking at 5 metrics in 2 treatments, the chance is already high that you might get a false positive result. 

To control for this issue, we correct for the increased false positive (Bonferroni) or false discovery (Benjamini-Hochberg) rate in these multiple comparisons. 


We recommend waiting a few days after an experiment starts before investigating which test violation(s)?
- SRM (Sample Ratio Mismatch)
- Low Sample Size
- Guardrail metrics

# Help, my estimated run time is too long!
- Increase the MDE
- Decrease the confidence (1-alpha) level (might increase false positive rate)
- Decrease the Power (1 - beta) level (might increase false negative rate)
- Increase the cohort rate by adding more users if the experiment isn’t running at full traffic ()useful only if new users are stil a population of interest
- Increase the cohort rate by driving more traffic to the treatment
- Use a proxy metric with lower variance or higher baseline
- Decrease the metric variance by using winsorization 
- Reduce the number of secondary metrics used
- Even out the cohort allocation