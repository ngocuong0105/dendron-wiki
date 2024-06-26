---
id: q06yegd2gxq72jqf5aib8em
title: Outliers
desc: ''
updated: 1678293538585
created: 1675163687844
---
It is important to consider detecting and handling outliers in your data to prevent them from negatively impacting your model. Outliers can cause issues such as skewing the distribution of the data and leading to poor model performance.There are several techniques that can be used to detect and handle outliers, including IsolationForest, OneClassSVM, EllipticEnvelope, and LocalOutlierFactor. You can also consider removing or interpolating outlier data points as a way to address this issue. By addressing outliers in your data, you can help ensure that your model is better able to generalize to new, unseen data.

# PCA
Use PCA to detect outliers in the dataset. PCA in particular can show you anomalous variation which might not be apparent from the original features: neither small houses nor houses with large basements are unusual, but it is unusual for small houses to have large basements. That's the kind of thing a principal component can show you.

Box plot the y-values over pca components and look at the extreme points.

