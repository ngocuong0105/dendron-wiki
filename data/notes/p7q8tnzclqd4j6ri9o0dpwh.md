
# [A unified approach to interpreting model predictions](https://drive.google.com/file/d/16EB_r2xMpIwWTbmqSCzr_ajXOIg26oTb/view?usp=drive_link)

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
- The paper describes two model-agnostic approcimate methods to compute SHAP:
    - Spaley sampling values (already known)
    - Kernel SHAP (novel)


One of the fundamental properties of Shapley values is that they always sum up to the difference between the game outcome when all players are present and the game outcome when no players are present.



**SHAP Values:**

SHAP (SHapley Additive exPlanations) values are a unified measure of feature importance in machine learning models. The key idea behind SHAP values is to distribute the prediction value among features, considering all possible feature combinations. Specifically, for a prediction $f(x)$ in a model, SHAP values allocate the contribution of each feature $i$ to the prediction by averaging over all possible feature combinations, taking into account their interactions. Mathematically, SHAP values are defined as:


$$
\phi_i(f) = \sum_{S \subseteq N \setminus \{i\}} \frac{{|S|!(|N|-|S|-1)!}}{{|N|!}} [f(S \cup \{i\}) - f(S)]
$$

where $\phi_i(f)$ represents the SHAP value of feature $i$ for the prediction function $f$, $N$ is the set of all features, and $S$ is a subset of features excluding feature $i$. The sum is taken over all possible subsets $S$.


SHAP values provide a consistent, locally accurate, and globally fair attribution method, enabling interpretable analysis of complex machine learning models.


# SHAP Values
