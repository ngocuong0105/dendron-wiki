Проклятието на големите размери...

An increase in the dimensions can in theory, add more information to the data thereby improving the quality of data but practically increases the noise and redundancy during its analysis.

# Ballpark estimate for number of data points required

Say for the number of points required by ML model to learn any value of a feature is 10.

- 1 binary feature: $2^{1} * 10 = 10$ data points
- 2 binary features: $2^{2} * 10 = 40$ data points

...

- n binary features: $2^{n} * 10 =$ many data points


# Recognize COD
- Overfitting
- Sparse features
- Comptational complexity

# Techniques to avoid COD

- Strict forward-feature selection (add feature only when you see marginal improvement in CV)
- Feature selection using permutation importance
- Feature extraction: PCA/t-SNE
- Regularization
- Model selection, choosing models that are less prone to overfitting
- Sample more data - bootstrapping