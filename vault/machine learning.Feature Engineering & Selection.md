---
id: pc1mkj2gp1dfypmvprtqeo5
title: Feature Engineering & Selection
desc: ''
updated: 1681982150605
created: 1679935795985
---

Quick [guide](https://github.com/Yimeng-Zhang/feature-engineering-and-feature-selection/blob/master/A%20Short%20Guide%20for%20Feature%20Engineering%20and%20Feature%20Selection.md#451-recursive-feature-elimination) for feature engineer and selection.



# Feature engineering

**TL;DR**

- transformation of current features (taking squares, log etc)
- apply interactions (multplication and ratio of two other features). When you make recipies it does make sense to add the ratio of the amounts of two ingredients
- group transforms (you get features that aggregate information across multiple rows grouped by some category, e.g. the average income of a person's state of residence)
- building-up and breaking-down features (ID 123-45-6789, addresses '8241 Kaggle Ln., Goose City, NV')
- K-means (use cluster as a categorical feature)
- cluster distane feature
- rescaling features (`preprocessing` module in scikit-learn )
- PCA
- target encoding for categorical features
- one-hot encoding (ok if you do not have many different values in a single category)

**Feature importance**

Rank features using a feature utility metric called "mutual information". The **mutual information (MI)** between two quantities is a measure of the extent to which knowledge of one quantity reduces uncertainty about the other. If you knew the value of a feature, how much more confident would you be about the target?

Mutual information = entropy (amount of information learned).


- MI can help you to understand the relative potential of a feature as a predictor of the target, considered by itself.
- It's possible for a feature to be very informative when interacting with other features, but not so informative all alone. MI can't detect interactions between features. It is a univariate metric.
- The actual usefulness of a feature depends on the model you use it with. 

```python
from sklearn.feature_selection import mutual_info_regression
```

**Interaction plots** using the hue parameter in seaborn. These plots shows you interactions between pairwise features.


**General tips:**
- Linear models learn sums and differences naturally, but can't learn anything more complex.
- Ratios seem to be difficult for most models to learn. Ratio combinations often lead to some easy performance gains.
- Linear models and neural nets generally do better with normalized features. Neural nets especially need features scaled to values not too far from 0. Tree-based models (like random forests and XGBoost) can sometimes benefit from normalization, but usually much less so.
- Tree models can learn to approximate almost any combination of features, but when a combination is especially important they can still benefit from having it explicitly created, especially when data is limited.
- Counts are especially helpful for tree models, since these models don't have a natural way of aggregating information across many features at once.

## K-means

The motivating idea for adding cluster labels is that the clusters will break up complicated relationships across features into simpler chunks. Our model can then just learn the simpler chunks one-by-one instead having to learn the complicated whole all at once. It's a "divide and conquer" strategy.


**K means is sensitive to scale**. Features with larger values will be weighted more heavily.


**Cluster distance feature!**
The k-means algorithm offers an alternative way of creating features. Instead of labelling each feature with the nearest cluster centroid, it can measure the distance from a point to all the centroids and return those distances as features.

## PCA

Clustering is a partitioning of the dataset based on proximity, you could think of PCA as a partitioning of the variation in the data.

PCA is typically applied to standardized data.

The whole idea of PCA: instead of describing the data with the original features, we describe it with its axes of variation. The axes of variation become the new features.

PCA makes this precise through each component's percent of explained variance.

PCA is a linear dimensionality reduction technique.

PCA use-cases:
- Dimensionality reduction: When your features are highly redundant (multicollinear, specifically), PCA will partition out the redundancy into one or more near-zero variance components, which you can then drop since they will contain little or no information.
- Anomaly detection: Unusual variation, not apparent from the original features, will often show up in the low-variance components. These components could be highly informative in an anomaly or outlier detection task.
- Noise reduction: A collection of sensor readings will often share some common background noise. PCA can sometimes collect the (informative) signal into a smaller number of features while leaving the noise alone, thus boosting the signal-to-noise ratio.
- Decorrelation: Some ML algorithms struggle with highly-correlated features. PCA transforms correlated features into uncorrelated components, which could be easier for your algorithm to work with.

**PCA tips:**
- PCA only works with numeric features, like continuous quantities or counts.
- PCA is sensitive to scale. It's good practice to standardize your data before applying PCA, unless you know you have good reason not to.
- Consider removing or constraining outliers, since they can have an undue influence on the results.


## Categorical features

We need to encode categorical features into numerical features.
- group aggregation strategy (use aggregate of the y values to encode the categorical features) e.g. mean encoding

This strategy is also known as **target encoding**. A target encoding derives numbers for the categories using the feature's most important property: its relationship with the target.

Problem with aggregate encoding:
1. missing categories in the test set need to be imputed somehow
2. rare categories would have uncertain calculated aggregated statistics

**Smoothing** in encoding idea.

The idea is to blend the in-category average with the overall average. Rare categories get less weight on their category average, while missing categories just get the overall average.
```
encoding = weight * in_category + (1 - weight) * overall
```

```
weight = n / (n + m)
```
Use **m-estimate** to calculate the weight.  The parameter $m$ determines the "smoothing factor". Larger values of $m$ put more weight on the overall estimate, the smoother it is.

```python
from category_encoders import MEstimateEncoder # scikit-learn-contrib package
```

**Use Cases for Target Encoding**
- High-cardinality features: A feature with a large number of categories can be troublesome to encode: a one-hot encoding would generate too many features and alternatives, like a label encoding, might not be appropriate for that feature. A target encoding derives numbers for the categories using the feature's most important property: its relationship with the target.
- Domain-motivated features: From prior experience, you might suspect that a categorical feature should be important even if it scored poorly with a feature metric. A target encoding can help reveal a feature's true informativeness.

**Tip**
When  using a target encoder it's very important to use separate data sets for training the encoder and training the model. Otherwise the results can be very disappointing!


# Feature Selection

Whatever feature selection you do **you should separete feature selection from model training.** This avoid data leakage. First fo model selection and then model training.

**Wrapper methods**: these are model dependent
- forward selection
- backward selection
- recursive feature elimination (greedy optimization)

**Filter methods**: these are model independent, and involve preprocessing
- Pearson correlation
- LDA - linear discriminant analysis
- ANOVA
- Chi-Square

These methods does not remove multicollinearity.

**Embedded methods**: regularization
- Ridge, Lasso

## Recursive Feature Elimination

1. Rank the features according to their importance
2. Remove one/or more features - the least important - and build a machine learning algorithm utilizing the remaining features.
3. Calculate a performance metric of your choice
4. If the metric decreases by more of an arbitrarily set threshold, then that feature is important and should be kept. Otherwise, we can remove that feature. 
Can run permutation importance on held out test set [scikit-learn](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)

Repeat steps 2-4 until all features have been removed (and therefore evaluated) and the drop in performance assessed.


## MDI

Tree-based models provide an alternative measure of feature importances based on the mean decrease in impurity (MDI). Impurity is quantified by the splitting criterion of the decision trees (Gini, Log Loss or Mean Squared Error). However, this method can give high importance to features that may not be predictive on unseen data when the model is overfitting Permutation-based feature importance, on the other hand, avoids this issue, since it can be computed on unseen data.

Furthermore, impurity-based feature importance for trees are strongly biased and favor high cardinality features (typically numerical features) over low cardinality features such as binary features or categorical variables with a small number of possible categories.

This problem stems from two limitations of impurity-based feature importances:
- impurity-based importances are biased towards high cardinality features;
- impurity-based importances are computed on training set statistics and therefore do not reflect the ability of feature to be useful to make predictions that generalize to the test set (when the model has enough capacity).

## Permutation importance

```python
from sklearn.inspection import permutation_importance
```
Permutation importance does not reflect to the intrinsic predictive value of a feature by itself but how important this feature is **for a particular model.**

We measure the importance of a feature by calculating the increase in the model’s prediction error after permuting the feature. A feature is “important” if shuffling its values increases the model **error**, because in this case the model relied on the feature for the prediction. A feature is “unimportant” if shuffling its values leaves the model error unchanged, because in this case the model ignored the feature for the prediction. 

**You should do permutation importance before model training.**

To highlight which features contribute the most to the generalization power of the inspected model permutation importance should be computed on validation set.


**NB**
When two features are correlated and one of the features is permuted, the model will still have access to the feature through its correlated feature. This will result in a lower importance value for both features, where they might actually be important.

One way to handle this is to cluster features that are correlated and only keep one feature from each cluster.


## Model Class Reliance
[Paper](https://arxiv.org/pdf/1801.01489.pdf)
