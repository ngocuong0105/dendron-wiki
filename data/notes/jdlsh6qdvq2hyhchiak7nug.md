
# Diff-in-Diff (Difference-in-Differences)

Why?

Diff-in-diff is used to estimate the causal effect of a treatment when the treatment is not implemented as a randomized control trial (e.g. A/B testing).

Within Ad Market Dynamics we primarily use Diff-in-Diff to measure the impact of geo experiments.

When to use Diff-in-Diff
Treatment is not randomly assigned (e.g. Geo experiment ✅  A/B testing ❌)
Other things were happening while treatment was in effect
You can't control for all the potential confounders
Assumptions for Diff-in-Diff
Trend in control group approximates what would have happened in the treatment group in the absence of the treatment
i.e. if the treatment was not implemented, then the two groups would have experienced the same changes. 
How to calculate Diff-in-Diff




An Example:

Diff-in-Diff for the treatment is calculated as follows: result is 15. 

Reference
- Amazing Youtube video on Diff-in-Diff
- Blog post with examples and case studies using Diff-in-Diff





