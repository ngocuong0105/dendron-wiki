---
id: yonznut0gv00jlkclk15lrn
title: All in one
desc: ''
updated: 1699453298578
created: 1696345069256
---
# Basics

Experiments are created by **randomly** splitting your traffic into separate cohorts, where each cohort gets a different variation of a treatment. Experiments can establish causality because the randomly assigned cohorts are effectively the same except for the applied treatment, so any differences seen in metric results are a result of the applied treatment. However, because the cohorts are sampled, they may not be reflective of the entire population, which introduces uncertainty (this is where statistics comes in!). 
To simplify the results of the statistics, we have created the Scorecard.


3 types of experiments:
- Simple AB allows you to compare multiple variants against the status quo. A Simple A/B does not run a formal A/A test.
- A/B allows you to compare multiple variants against the status quo.
- Rollout allows you to compare one single new variant - usually the new feature - against the status quo.
- SEO

**Beaker**

This is Yelp's platform to create experiments. You can create experiments in these two subplatforms:
- RequestBucketer (cohort-based)
- Bunsen (parameter-based)

Both allow you to run experiments, the difference is that you manage and instantiate them in a different way. Bunsen tracks performing metrics automatically. RequestBucketer requires your own or third-party solution.


## A/B test

A/B testing is a method of comparing multiple variants against each other to determine which one performs better.

A typical A/B experiment includes one A/A test and multiple A/B tests.
- A/A test: a test to determine the time needed to conduct the A/B test. The A/A test itself runs for 7 days.
- A/B test: a test to compare treatment with current status quo. It runs for the time determined by the A/A test.

## Rollout
A feature rollout is the process of introducing a new feature to a set of users and analyzing the impact. By rolling out in phases, it gives a company an opportunity to fully test the UI and user experience.

It includes one optional A/A test and multiple rollout runs.
- A/A test: a test to determine the time needed to conduct the A/B test. It is only needed if tracking a metric. The A/A test itself runs for 7 days.
- Rollout run: a process of splitting traffic into status quo and one variant. There is no requirement on how long a rollout run should take.


## Simple AB

Simple AB is the fastest option for most experiments that do not have specific needs for an A/A test. Power Analysis occurs during the A/B run, removing the week long A/A Run requirement.

It includes optional smoke tests and one A/B test.
- Smoke test: a short test to uncover implementation issues at an early stage of the experiment pipeline. It need not run for more than 1-2 days.
- A/B test: compares treatment cohorts against status quo. Automatically determines duration of the experiment run (at least 7 days).

Unsupported Use Cases:
- Experiments with diversion keys other than guv , user_id_encid and business_id_encid.
- Swimlanes.
- Manual A/A tests.

## SEO
SEO experiments are used to test features that impact web organic traffic levels coming into yelp. They use page_id as a diversion key instead of guv, therefore a new feature is introduced to a set of "pages" versus a set of "users". The SEO experiment tests impact on both msite and www pages for Yelp. An SEO Experiment tests features to identify what optimizes SEO and therefore should lead to an increase in organic traffic.


A typical SEO experiment includes two tests, an A/A test followed by an A/B test on the same set of users.
- The first A/A test is used to collect baseline value, define the required number of samples and randomly selects samples for the experiment.
- The second A/B test runs after the first A/A run has reached full power, and uses the baseline and selected samples to compare treatment cohorts with current status quo.

Specifics of SEO experiments:

These experiments run not on users but on website pages and number of pages in cohort is not stable - some pages can be a part of an experiment at some point of time (not necessarily during all period when it was active) BUT they can’t switch between cohorts. 
The main goal of SEO experiments is to test how certain changes on webpage can impact our traffic from Google, in other words: how Google react on changes (title tags, internal linking, content, etc.) we make on a page - will they rank us higher and send us more traffic or maybe we’ll start losing traffic. 

## What types of runs make up an SEO experiment?
Each SEO experiment is made of exactly one SEO A/A test followed by one SEO A/B test. Each individual test can be rerun if issues occur.

SEO A/A: A/A testing is used to test two identical versions of each other. A/A testing is done to:

- Collect the metric value of the status quo cohort in order to perform power analysis, calculating the number of samples needed for the experiment to conclude.
- Collect the required number of samples into the assignment log for A/B run to use. Any new samples that the A/B run collects but were not present during the A/A run will not be considered for analysis.

SEO A/B: A/B testing is a method of comparing multiple variants against each other.

- The A/B run measures how the samples collected during A/A run react to different treatments.
- Any new samples that appeared during AB run but were not present during A/A will not be included in analysis.


## Steps to run SEO



# Scorecard



## Guardrail alerts


Guardrails are important company wide metrics that we aim to protect against while experimenting.



# A/B Testing Intuition Busters

[Paper](https://drive.google.com/file/d/1O0HxZprNGDpzD27Aiqjm5XxAp2FQigca/view?usp=drive_link)

