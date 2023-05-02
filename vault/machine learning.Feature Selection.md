---
id: pc1mkj2gp1dfypmvprtqeo5
title: Feature Selection
desc: ''
updated: 1682870719098
created: 1679935795985
---

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

To highlight which features contribute the most to the generalization power of the inspected model permutation importance should be computed on validation set.


Sklearn permutation_importance takes as input a fitted model. Thus based on the selected features/weights during training it computes the importance of the features. These features importance show how good are these features for this particular model. 

**Another take on feature importance is: to do permutation importance before model training.** This should be done manually (I don't know about a library)
Advatange is that is more acurate, disadvantage is that you loose a lot of time in training.


**NB**
When two features are correlated and one of the features is permuted, the model will still have access to the feature through its correlated feature. This will result in a lower importance value for both features, where they might actually be important.

One way to handle this is to cluster features that are correlated and only keep one feature from each cluster.


## Model Class Reliance
[Paper](https://arxiv.org/pdf/1801.01489.pdf)
