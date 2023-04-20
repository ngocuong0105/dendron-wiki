---
id: tfv2mbp7pm72fjssn0eijec
title: Imbalanced dataset
desc: ''
updated: 1680686642070
created: 1680683206762
---

Common pitfalls

- Never test on the oversampled or undersampled dataset.
- If we want to implement cross validation, remember to oversample or undersample your training data during cross-validation, not before!
- Don't use **accuracy score** as a metric with imbalanced datasets (will be usually high and misleading), instead use f1-score, precision/recall score or confusion matrix

Imbalanced dataset techniques:

- random under-sampling = get small subsample of the overrepresented class. Main risk is of great infromation loss.
- SMOTE (synthetic minority over-sampling technique)
- cost-sensitive loss function

# What is the imbalanced dataset problem?

Without loss of generality, we assume that the minority or rare class is the positive class, and the majority class is the negative class. If we apply most traditional (cost-insensitive) classifiers on the dataset, they will likely to predict everything as negative (the majority class). This was often regarded as a problem in learning from highly imbalanced datasets.

Creating a traditional-cost-insensitive classifier has two assumptions:
- goal is to maximize accuracy/minimize loss
- train and test datasets have the same distributions

**Under these assumtions, predicting everything negative is the correct thing to do.**

Thus, the imbalanced class problem becomes meaningful only if one or both of the two assumptions above are not true:
- the cost of different types of error is not the same/missclasification cost is not equal
- the train and test data are different

## When changing the cost-function works
In the case when the misclassification cost is not equal, it is usually more expensive to misclassify a minority (positive) example into the majority (negative) class, than a majority example into the minority class (otherwise it is more plausible to predict everything as negative). That is, FN > FP. In this case you should have a loss function which penalizes FN more than FP.


## When over/undersampling works
In case the class distributions of training and test datasets are different (for example, if the training data is highly imbalanced but the test data is more balanced), an obvious approach is to sample the training data such that its class distribution is the same as the test data (by oversampling the minority class and/or undersampling the majority class).