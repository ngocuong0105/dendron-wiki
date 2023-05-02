---
id: ltvbyf1oqc8qx7khy58pby2
title: Kaggle Learn
desc: ''
updated: 1682953623796
created: 1677947097369
---
[Hands-on course in Kaggle](https://www.kaggle.com/learn)


# Intro to ML

Steps:
1. EDA
2. Feature engineering
3. Build ML model
4. Model validation


**[random_state parameter](https://scikit-learn.org/stable/glossary.html#term-random_state:~:text=random_state-,%C2%B6,-%C2%B6)**

Many machine learning models allow some randomness in model training. Specifying a number for random_state ensures you get the same results in each run. You use any number, and model quality won't depend meaningfully on exactly what value you choose.

**Underfitting vs overfitting**

Control the balance between these two using max leaves and max tree depth parameters in decision trees.

# Data Vsualization


categorical scatter plot

```python
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])
```

# Videos

## [Beyond Feature Selection](https://www.youtube.com/watch?v=gdyuCqmLMUg&t=944)

**Is more features better? should I just get more and more features?**

More features is generally better. As long as your features bring novel information it is good.


Decision trees have built in Feature Selection. for each split you choose the best split - it is a feature selection algorithm.

So do we really need FS when training Decision Trees (LGBM, XGBOOST). The answer is yes. You still need. It does happen your model on the sample data might pick up noisy feature. So you still need FS.

Feature selection can reduce the number of features and you can get your AUC/Score up by a few points.

`scikit-learn`

- Univariate analysis: 
    - variance threshold
    - F-test (ANOVA)
- RFE (recursive feature elimination) the KAggle says it works well


There is some biase in the feature selection. If you do FS for Xgboost, then the features you et woud be good for the xgboost but might not be for Neaural NEts

`Beyond scikit-learn`

- Boruta
    - Wrapper
    - Loss based
    - Subset
- ReliefF
    - Filter method
    - Distance based
    - Ranking

**Characteristics of Feature Selection Algorithms**
- Feature space
    - Univariate F-Score
    - Multivariate (RFE, L1-based, Tree-based)
- Direction
    - Forward
    - Backward
    - Ranking: F-score, L1-based

**Most of the time in Kaggle competitons I spent 90% of the time on FS, FE, prepping the data.**


Feature engineering is usually better that Feature Selection


[CPMP talk](https://www.youtube.com/watch?v=VC8Jc9_lNoY&t=408s)


Target Engineering - transform the target and make predictions on it to match the competition metric.

SMAPE for example is assymetric metric. If you transfor the target with log, you get a metric which is almost like MAE.

Understand the problem that is being solved. Understand the metric. Understand the data.

How good a feature is depends on the competition metric!!! Feature importance, correlations, etc. are not that important.

Setup good Cross validation local setup. You CV score should correlate with the public LB.

**Track the Train-Test error GAP** Large gap indicates overfit. When your CV score is increasing and the gap is not incrasing a lot, then you are not overfitting.

For xgboost/LGBM no need to worry about one hot encoding, or nan values. They handle it well.

[Feature engineering deck](https://www.slideshare.net/HJvanVeen/feature-engineering-72376750)



[Winning gold is easy](https://www.youtube.com/watch?v=XBJ2f68LuO4&t=38s)

A LOT OF TIPS AND TRICKS in this video.

If something does not work, does not stick to it.

to get a gold model you need to try crazy ideas. Most would not work, but if you get one good one you can get the gold.

Trick for feature engineering:
- add 1 noisy features
- compute feature importance for all features
- features which have higher rank than the noisy feature should generally be good features
- if your noisy feature is too high in rank, your model is overfitting on noisy features and gives them high rank
- you need to go through the top ranked features and see which of them your model is overfitting 


**Feature importance**

Detect overfitting features
- remove the feature and if CV is not hurt your are good
- if removing the feature hurts CV, then use transoframtion on the feature


Feature engineering is a bit of an art. Feature X and Feature Y might be good only if you use both (as they have interation).

Powerful feature:

`
featureX - groupby(FeatureY)[FeatureX].mean()
`


If your model has many features (e.g xgboost) try using small colsubsample. Usually you would use 80-90%. But when having MANY features, this way your trees would be almost independent and not correlated.

Working with NN or linear models, when a feature you have NAN, add additional boolean column.

NN are making feature engineering implicitly.

----
