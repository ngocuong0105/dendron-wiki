---
id: ltvbyf1oqc8qx7khy58pby2
title: Kaggle Learn
desc: ''
updated: 1681982126654
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