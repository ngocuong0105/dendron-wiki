---
id: h79jpatf2zw7a0qpq4asniw
title: Linear Rgression
desc: ''
updated: 1751964740835
created: 1751960242840
---
# On Multi-Collinear Features

Experiment:
- Run LR `y ~ x1`
- Run LR `y ~ x1+x2`, where these two are highly correlated

Results
```
Uncorrelated features correlation:

Uncorrelated case model summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.929
Model:                            OLS   Adj. R-squared:                  0.928
Method:                 Least Squares   F-statistic:                     1275.
Date:                Tue, 08 Jul 2025   Prob (F-statistic):           5.50e-58
Time:                        08:19:04   Log-Likelihood:                -78.314
No. Observations:                 100   AIC:                             160.6
Df Residuals:                      98   BIC:                             165.8
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          5.0443      0.054     93.689      0.000       4.937       5.151
X1             2.1139      0.059     35.712      0.000       1.996       2.231
==============================================================================
Omnibus:                        3.154   Durbin-Watson:                   2.216
Prob(Omnibus):                  0.207   Jarque-Bera (JB):                3.133
Skew:                           0.105   Prob(JB):                        0.209
Kurtosis:                       3.841   Cond. No.                         1.16
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Highly correlated features correlation:
          X1        X2
X1  1.000000  0.999931
X2  0.999931  1.000000

Highly correlated case model summary:
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.939
Model:                            OLS   Adj. R-squared:                  0.938
Method:                 Least Squares   F-statistic:                     751.5
Date:                Tue, 08 Jul 2025   Prob (F-statistic):           9.10e-60
Time:                        08:19:04   Log-Likelihood:                -63.278
No. Observations:                 100   AIC:                             132.6
Df Residuals:                      97   BIC:                             140.4
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          4.9343      0.047    105.551      0.000       4.842       5.027
X1             6.8089      4.486      1.518      0.132      -2.095      15.713
X2            -4.7588      4.475     -1.064      0.290     -13.639       4.122
==============================================================================
Omnibus:                        0.401   Durbin-Watson:                   2.118
Prob(Omnibus):                  0.818   Jarque-Bera (JB):                0.103
Skew:                          -0.034   Prob(JB):                        0.950
Kurtosis:                       3.141   Cond. No.                         174.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```

**Insights:**
- Forecasts of both model are good and in practice you don't need to drop the correlated features if you care about forecasts
- Remember that the forecast $\hat{y}$ is the orthogonal projection of the real value y on the subspace spanned by the design matrix $X$. If the deign matrix has correlated features there are multiple ways to express the same $\hat{y}$. Hence different values for the $\hat{beta}$ would give the same forecast.  
- When there are correlated features you will see large variance in the beta estimates, also mathematically $var(\hat{beta})=(XX^{T})^{-1}\sigma$ will just be very large when the inside matrix is not positive definite.
- large beta variance, means low t-statistic, which means high p-value
- hence with correlated features the model is not interpretable but the sum is good forecasts.


**The Geometry**
- When two variables are highly correlated, they both almost point in the same “direction” in the predictor space.
- The model tries to allocate credit (and adjust slope) between them for explaining changes in y.
- Many combinations of coefficients can fit the same plane equally well.
         
**Effect on Model Fit** 

- The overall plane/surface that regression fits (ŷ = intercept + b1*X1 + b2*X2) can still be the same, though b1 and b2 may be weird or unintuitive (like 378 and -377). Forecasts are still good.
- The regression is “sure” about the sum effect, but not about the individual effects.
     
**Unstaple coefficients**
- Opposite signs and very large in absolute values to offset each other.
- For forecasting, this generally does not hurt test-set predictive performance as long as your train/test data comes from the same distribution and the correlation patterns are stable. It can, however, make your model more sensitive to changes in the feature distribution ("unstable predictions" with changing data).

# High Leverage Points

- outliers in the design matrix $X$ can lead to the picture below:
- if a row $x_i$ deviates from the mean of $X$ it will have large leverage and pull the regression line
![high_leverage_point](./assets/images/high_leverage_point.png)


NOTE:  In regression, leverage is a property of observations (rows, i.e. data points), not of features (columns, variables). 
- You need to check rows that are with high leverage not features/columns!

```python
# Model Spec
# Generate 8 normal data points
X1 = np.random.normal(0, 1, 8)
X2 = np.random.normal(0, 1, 8)
y = 2*X1 + 3*X2 + np.random.normal(0, 0.5, 8)

# Add a high-leverage point (extreme X1)
X1_leverage = np.append(X1, 10)
X2_leverage = np.append(X2, 1)
y_leverage = np.append(y, 4)
```

**Results**

```
Model with leveraged point
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.526
Model:                            OLS   Adj. R-squared:                  0.368
Method:                 Least Squares   F-statistic:                     3.328
Date:                Tue, 08 Jul 2025   Prob (F-statistic):              0.107
Time:                        09:31:52   Log-Likelihood:                -18.040
No. Observations:                   9   AIC:                             42.08
Df Residuals:                       6   BIC:                             42.67
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.0550      1.093      0.965      0.372      -1.620       3.730
X1             0.0434      0.282      0.154      0.883      -0.647       0.734
X2             3.9627      1.857      2.134      0.077      -0.580       8.505
==============================================================================
Omnibus:                        0.114   Durbin-Watson:                   1.807
Prob(Omnibus):                  0.944   Jarque-Bera (JB):                0.321
Skew:                           0.113   Prob(JB):                        0.852
Kurtosis:                       2.103   Cond. No.                         9.95
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.


Model without leveraged point
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.972
Model:                            OLS   Adj. R-squared:                  0.961
Method:                 Least Squares   F-statistic:                     88.04
Date:                Tue, 08 Jul 2025   Prob (F-statistic):           0.000127
Time:                        09:31:52   Log-Likelihood:                -5.0804
No. Observations:                   8   AIC:                             16.16
Df Residuals:                       5   BIC:                             16.40
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.2898      0.299      0.968      0.377      -0.480       1.059
X1             2.0443      0.233      8.772      0.000       1.445       2.643
X2             2.1176      0.528      4.008      0.010       0.759       3.476
==============================================================================
Omnibus:                        3.584   Durbin-Watson:                   2.783
Prob(Omnibus):                  0.167   Jarque-Bera (JB):                1.223
Skew:                          -0.958   Prob(JB):                        0.543
Kurtosis:                       3.002   Cond. No.                         4.46
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```