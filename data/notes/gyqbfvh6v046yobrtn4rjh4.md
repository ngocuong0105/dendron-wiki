
# Huber Loss
[Wikipedia](https://en.wikipedia.org/wiki/Huber_loss#:~:text=absolute%20value%20function).-,Pseudo%2DHuber%20loss%20function,less%20steep%20for%20extreme%20values.)

Huber loss is a combination of L1 and L2 loss functions. It is less sensitive to outliers in data than the squared error loss.

pseudo huber loss allows you to control the smoothness and therefore you can specifically decide how much you penalise outliers by, whereas huber loss is either MSE or MAE

## How to choose the hyper parameter delta?
Huber loss will clip gradients to delta for residual (abs) values larger than delta. You want that when some part of your data points poorly fit the model and you would like to limit their influence. Also, clipping the grads is a common way to make optimization stable (not necessarily with huber).
[StackExchange](https://stats.stackexchange.com/questions/465937/how-to-choose-delta-parameter-in-huber-loss-function)


# L1 vs L2 regularization


The best advice in data science is always try both and see what produces better CV and LB.

I think L1 shines when we approach "the curse of dimensionality" (i.e. when the number of train rows is small compared with number of train columns). I think a rule of thumb is when number of features (i.e. columns) is anywhere near 1/10th (or larger) the number of training samples (i.e. rows) we approach the "the curse of dimensionality".

