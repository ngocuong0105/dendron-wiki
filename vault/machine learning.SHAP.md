---
id: p7q8tnzclqd4j6ri9o0dpwh
title: Explainable AI - SHAP
desc: ''
updated: 1698308392955
created: 1697562950645
---

# [A unified approach to interpreting model predictions](https://proceedings.neurips.cc/paper_files/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf)

[SHAP docs](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html)

- explainable AI
- accuracy vs interpretability
- SHAP (SHapley Additive exPlanations)
- new notion: **any explanation of a model’s prediction as a model itself, which we term the explanation model**
- related to partial dependency plots (way to compute 'importance' of a group of features)


**Definition.**  The best explanation of a simple model is the model itself; it perfectly represents itself and is easy to understand. For complex models, such as ensemble methods or deep networks, we cannot use the original model as its own best explanation because it is not easy to understand. Instead, we must use a simpler **explanation model**, which we define as any interpretable approximation of the original model.

**Definition 1:** Additive feature attribution methods have an explanation model that is a linear function of binary variables:
\[ g(z') = \phi_0 + \sum_{i=1}^{M} X_i \phi_i z_i', \quad \text{where} \quad z' \in \{0, 1\}^M, \, M \, \text{is the number of simplified input features, and} \, \phi_i \in \mathbb{R}. \]


**Definition 0:** Additive feature attribution methods have an explanation model that is a linear function of binary variables:  


Paper important things:
- Definition 1 Additive feature attribution methods
- Shapley regression values 
- Shapley sampling values 
- Theorem 1: There is a unique additive feature attribution method that satisfies the properties of local accuracy, missingness, and consistency.
- Section 3 provides the solution to that theorem
- main problem is to approximate SHAP values
- SHAP values can be very complicated to compute (they are NP-hard in general)


One of the fundamental properties of Shapley values is that they always sum up to the difference between the game outcome when all players are present and the game outcome when no players are present.