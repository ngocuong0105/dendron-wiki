---
id: 4to49a2jwhv8s6kap9e4jps
title: Metrics
desc: ''
updated: 1679935856391
created: 1679901340004
---

# F1 score

Harmonic mean between precision and recall. Precision measures how precise is you pick up positive predictions (TP/FP).
Recall is how many of all true predictions you have predicted to be positive (TP/AP).

TP = true positive predictions

FP = forecastes as positive

AP = actual positive


You can pick one positive prediction and it to be corrrect. This will have high precision but low recall as you have not captured many true predictions.

F1 brings recall and precision in one number and we take the harmonic mean because precision and recall are rates.

Harmonic mean is used when you have multiple rates and you need to compute the **average rate**.


**NB**
- F1 score measures how good are your positive predictions
- F1 score is skewed towards classifiers which would overforecast positive predictions
- F1 score is 0.67 if you predict only ones and is 0 if you predict only zeroes.
- F1 equalized the importance of precision and recall. In practice these represent different mis-classifications.
- F1 ingnores True Negatives and is misleading for imbalannced classes
- F1 is not symmetric - if you change labels and forecasts from 1 to 0 and vice versa your F1 score changes

Example:

Actual: 0, 1

Prediction: 1, 1

F1 = 0.67, precision is 0.5, recall is 1

After swap:

Actual: 1, 0

Prediction: 0,0

F1 = 0

# SMAPE

[Symmetrics mean absolute percentage error](https://en.wikipedia.org/wiki/Symmetric_mean_absolute_percentage_error)

- Overforecasts are better than under forecasts (A: 100, F: 120 is better than A: 100, F: 80).
- SMAPE is a ratio metric. Hence if you adjust your forecast you better use a multiplication factor rather than additive factor (adding constant number (e.g 5) to a forecast of 100 and to a forecast of 10 is totatally different).
- small actual values and forecasts can have big impact on the metric (usually data is nosier with small values/quantitites) 
- one possible trick to optimize SMAPE is to predict the relative change rather than the actual values (relative change works with normilized data).

Example why you need target engineering/relative change fortecasts:
```
Let's take one example of two cities and two months.
First month:
City A = 5
City B = 100

Second month:
City A = 1 (-80% retrocession)
City B = 105 (+5% growth)

Now suppose your model is predicting the second month, and the predictions are:
Pred A = 6 (+20%)
Pred B = 110 (+10%)

From these predictions, you had a low MAE (missed both by 5), but a high SMAPE for A and very low for B.

SMAPE = SMAPE(city A) + SMAPE(city B) = 5/7 + 5/215

city A contributes to the error 30 times more than city B. Smaller city hase huge effect on the SMAPE.

Now suppose you use rate of change as Target
SMAPE = SMAPE(city A) + SMAPE(city B) = 1/1 + 0.05/0.15 = 1 + 1/3
```

**The example above shows that small cities can have huge impact on SMAPE and last value model should generrally be used for them**

