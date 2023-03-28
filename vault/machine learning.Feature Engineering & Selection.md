---
id: pc1mkj2gp1dfypmvprtqeo5
title: Feature Engineering & Selection
desc: ''
updated: 1679936230357
created: 1679935795985
---

Quick [guide](https://github.com/Yimeng-Zhang/feature-engineering-and-feature-selection/blob/master/A%20Short%20Guide%20for%20Feature%20Engineering%20and%20Feature%20Selection.md#451-recursive-feature-elimination) for feature engineer and selection.

# Recursive Feature Elimination

1. Rank the features according to their importance
2. Remove one/or more features - the least important - and build a machine learning algorithm utilizing the remaining features.
3. Calculate a performance metric of your choice
4. If the metric decreases by more of an arbitrarily set threshold, then that feature is important and should be kept. Otherwise, we can remove that feature.
Repeat steps 2-4 until all features have been removed (and therefore evaluated) and the drop in performance assessed.