---
id: nkefr7ipopudoxe89h53oy4
title: Decision Trees
desc: ''
updated: 1674729446179
created: 1673945350311
---

To learn a decision tree model, we take a greedy approach:
1. Start with an empty decision tree (undivided
feature space)
2. Choose the ‘optimal’ predictor on which to split and
choose the ‘optimal’ threshold value for splitting by
applying a splitting criterion
3. Recurse on on each new node until stopping
condition is met
For classification, we label each region in the model
with the label of the class to which the plurality of the
points within the region belong.


![decision_trees.png](assets/images/decision_trees.png)


For regression you need:
- pure nodes (no two leaves with same value, e.g lemons)
- Output in $\R$ usually the average of the training points contained in the region



The learning algorithms for decision trees in regression tasks is:
1. Start with an empty decision tree (undivided feature space) 
2. Choose a predictor $j$ on which to split and choose a threshold value $t_j$ for splitting such that the weighted average MSE of the new regions as smallest possible:

$argmin_{j,t_j} (\dfrac{N_{1}}{N}) MSE(R_{1}) + \dfrac{N_2}{N}MSE(R_2)$

where $N_i$ is the number of training points in $R_i$ and $N$ is the number of points in $R$.
3. Recurse on on each new node until **stopping condition** is met

Stop conditions:
- max depth
- minimum number of points in each region
- compute purity gain and stop when the gain is less than some pre-defined threshold

$Gain(R) = MSE(R) - (\dfrac{N_{1}}{N}) MSE(R_{1}) - \dfrac{N_2}{N}MSE(R_2)$ 


## Expressiveness of DT

Classification trees approximate boundaries in the feature space that separate classes. Regression trees, on the other hand, define simple functions
or step functions, functions that are defined on partitions of
the feature space and are constant over each part.

![expr_dt.png](assets/images/expr_dt.png)


To capture a complex decision boundary (or to approximate a complex function), we
need to use a large tree (since each time we can only make axis aligned splits). Large trees have large variance and overfit.

## Bagging

Adjust for the high variance using **bagging**. Run multiple times DT and average out the results.

The same idea can be applied to high variance models:
1. (Bootstrap) we generate multiple samples of training
data, via bootstrapping. We train a full decision tree on
each sample of data.
2. (Aggregate) for a given input, we output the averaged
outputs of all the models for that input.

For classification - use voting.

Bagging = Boostrap + Aggregating

Note that bagging enjoys the benefits of
1. High expressiveness - by using full trees each model is able to approximate complex functions and decision boundaries.
2. Low variance - averaging the prediction of all the models reduces the variance in the final prediction, assuming that we choose a sufficiently large number of trees.

Drawback of bagging (and other ensemble methods) is that the averaged model is not interpretable.

# Out-of-bag error

The bootstrap step in Bagging has small out of bag sample (with replacement sampling) To compute OOB error:


1. Find all models (or trees, in the case of a random forest) that are not trained by the OOB instance.
2. Take the majority vote(average fore regressions) of these models' result for the OOB instance, compared to the true value of the OOB instance.
3. Compile the OOB error for all instances in the OOB dataset. Average out OOBs.

## Random forests

In practice, the ensembles of trees in Bagging tend to be highly correlated.

Suppose we have an extremely strong predictor, $x_j$ , in the training set amongst moderate predictors. Then the greedy learning algorithm ensures that most of the
models in the ensemble will choose to split on $x_j$ in early iterations.

That is, each tree in the ensemble is **identically distributed**, with the expected output of the averaged model the same as the expected output of any one of the trees.

**Bagging improvement**. The variance of the mean $B$ identical but not independent decision trees $X_1 ... X_B$ is $\dfrac{1}{B^2}(\sum var(X_i) + \sum_{i!=j} cov(X_i,X_j)) = \dfrac{1}{B}\sigma^2+\dfrac{B-1}{B}\rho\sigma^2 = \rho\sigma^2 + \dfrac{1-\rho}{B}\sigma^2$, where $\rho$ is pairwise correlation. 

The larger $B$ the lower variance. As $B → \infty$,bagging variance is bounded by correlation term.

**Random Forest** is a modified form of bagging that creates ensembles of independent decision trees.

To de-correlate the trees, we:
1. train each tree on a separate bootstrap sample of the full training set (same as in bagging)
2. for each tree, at each split, we randomly select a set of J predictors from the full set of predictors. From amongst the $J$ predictors, we select the optimal predictor and the optimal corresponding threshold for the split. [random subspace method](https://en.wikipedia.org/wiki/Random_subspace_method) reduces correlation between estimators.
3. ensemble all trees using average/majority function

Random forest models have multiple hyper-parameters to tune:
1. the number of predictors to randomly select at
each split
2. the total number of trees in the ensemble
3. the minimum leaf node size

Tuning random forests:

Using out-of-bag errors, training and cross validation can be done in a single sequence - we cease training once the out-of-bag error stabilizes.

**Weak spot of RF:**

When the number of predictors is large, but the number of relevant predictors is small, random forests can perform poorly.

In each split, the chances of selected a relevant predictor will be low and hence most trees in the ensemble will be weak models.

On number of trees in enseble algo

Increasing the number of trees in the ensemble generally does not increase the risk of overfitting. Again, by decomposing the generalization error in terms of bias and variance, we see that increasing the number of trees produces a model that is at least as robust as a single tree.

However, if the number of trees is too large, then the trees in the ensemble may become more correlated, increase the varianc

**Variable importance for RF**

Record the prediction accuracy on the oob samples for each tree.
- Randomly permute the data for column $j$ in the oob samples the record the accuracy again (make it unmeaningful).
- The decrease in accuracy as a result of this permuting is averaged over all trees, and is used as a measure of the importance of variable $j$ in the random forest. 

# Gradient Boosting

Random forests and boosted trees are really the same models; the difference arises from how we train them.

By increasing the number of trees $B$ and reducing the pairwise correlation $\rho$ we try to reduce the variance of the model. 

Rather than reducing variance, we can aim to reduce bias of simple trees and make them more **expressive**. Boosting is another ensemble method which achieves that.

Add weak models $T_{i}$ additively and iteratively to ensemble a linear combination $T = \sum \w_{i}T_{i}$  whis is expressive.


![gradient_boost.png](assets/images/gradient_boost.png)

Each simple model $T_i$ we add to our ensemble model $T$, models the errors of the previous version of $T$.

Note that gradient boosting has a tuning parameter, $\lambda$ - step size(learning rate). 

Goal is to minimize objective function, computationally you compute partial derivatives set them to 0 and compute the stationary point. If the objective function is convex, then the stationary point is the min.


Subtracting a $\lambda$ multiple of the gradient from $x$, moves $x$ in the opposite direction of the gradient (hence towards the **steepest decline**) by a step of size $\lambda$. 

![learning_rate.png](assets/images/learning_rate.png)

Choosing $\lambda$
- if $\lambda$ is a constant, then tune through cross validation
- variable learning rate $\lambda = g(|f'(x)|)$, function of the gradient of $f(x)$. Around the optimum, when the gradient is small, the learning rate should be small


# XGBoost

Our model is written in the form:

$\hat{y}_i = \sum_{k=1}^{K} f_{k}(x_{i}), f_k \in F$

where $K$ is the number of trees, $f_{k}$ is a function in the functional space $F$, and $F$ is the set of all possible CARTs.

The objective fundtion is given by:

$obj(\theta) = \sum l(y_i,\hat{y}_i) + \sum \omega(f_{k})$ where $\omega(f_k)$ is the complexity of the tree $f_k$ (regularization)


We add the trees $f_k$ additevely/iteratively. For example we learn $f_{t}$ by optimizing:

![xgboost_obj.png](assets/images/xgboost_obj.png)


One important advantage of this definition is that the value of the objective function only depends on $g_i$ and $h_i$. This is how XGBoost support custom loss functions. 


## Implementation resources

- [Scikit-Learn API](https://xgboost.readthedocs.io/en/stable/python/python_api.html)
- [XGBoost parameter](https://xgboost.readthedocs.io/en/stable/parameter.html)
- [Hyper parameter tuning (Bayesian)](https://www.kaggle.com/code/prashant111/a-guide-on-xgboost-hyperparameters-tuning/notebook)


**Limitation of additive tree learning.**

Since it is intractable to enumerate all possible tree structures, we add one split at a time. This approach works well most of the time, but there are some edge cases that fail due to this approach. For those edge cases, training results in a degenerate model because we consider only one feature dimension at a time. 


# Adaboost

Connect gradient boosting for regression to a boosting algorithm often used for classification.

Unfortunately error function is not differentiable!

$Error = \dfrac{1}{N} \sum I(y_n != \hat{y}_n)$

Replace the error function with a differentiable function that is a good indicator of classification error. Exponential loss:

$ExpLoss = \dfrac{1}{N} \sum exp(y_n \hat{y}_n)$



![adaboost.png](assets/images/adaboost.png)

![adaboost_lambda.png](assets/images/adaboost_lambda.png)

# Implemetations

There are few implementations on boosting:
- XGBoost: An efficient Gradient Boosting Decision 
- LGBM: Light Gradient Boosted Machines. It is a library for training GBMs developed by Microsoft, and it competes with XGBoost 
- CatBoost: A new library for Gradient Boosting Decision Trees, offering appropriate handling of categorical features