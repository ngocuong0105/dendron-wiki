---
id: 7z1pagvjmrp0151ogbehtpi
title: MIT - Introduction to Deep Learning
desc: ''
updated: 1744664275789
created: 1744659193293
---
# 6.S191 | MIT Introduction to Deep Learning

- [Official Website](https://introtodeeplearning.com/)
- [GitHub Repo](https://github.com/MITDeepLearning/introtodeeplearning/tree/master)

# Lecture 1: Introduction

Deep Fake vide of Obama. MIT created 2 minutes deep video of OObama saying Welcome to MIT class. In 2020 ot costed 15K $

Intelligence - the ability process information in order to inform some future decision or action

Artificial Intelligence - make computers be able to learn to apply this process.

Machine Learning is a subset of Artificial Intelligence.

Make computers learn and execute tasks from the given data.


## Why Deep Learning

Classical ML works by defining features. For example in image detection we would start defining lines, edges, curves ,eyes, noses, face. We need to define the features from low level to high level. We can't detect faces directly. We built composite features. **Feature Engineering**.

DL automates the process of **feature engineering**. DL has been around for a long time (decades). Why it became popular now?
- More data
- Compute power
- Libraries like tensorflow, pytorch

## The perceptron: Forward propagation

- single neuron
- input vector $x$
- Linear sum using weights and a bias term
- non-linear activation function: sigmoid (good for probabilities), ReLu (piecewise linear, non linear at 0), hyperbolic function

The point of the activation function is to introduce a non-linearity because real data in real world is heavily non-linear.

$\hat{y} = g(w_{0} + x^{T}w)$ 


![alt text](./assets/images/perceptron_simplified.png)

**dot product, add bias, apply non-linearity**


## Layer

![alt text](./assets/images/one_hidden_layer.png)


## Deep network

Has many hidden layers

## Loss

Empirical Loss

Loss function = Cost function = Objective function


Cross entropy loss, difference between probabilities. For Binary predictions.

Mean Squared Errors, difference between us functions. For real number predictions.


Our goal is to find a network that minimizes the loss on the given dataset.

Goal is to find all weights.


## Loss optimization

![alt text](./assets/images/loss_optimization.png)

## Gradient Descent

Randomly initialize our weights. Randomly pick a point in our landscape (loss function). Compute the gradient and take the opposite direction of the gradient. Note this is **local optimization**. We go with a small step opposite to the gradient direction. Choosing learning rate = step size.


![alt text](./assets/images/gradient_descent_2.png)

How do we compute the gradient? the process of computing the gradient is called **backpropagation**.

Derivatives, chain rule


Neural networks are extremely complex functions with complex loss landscapes.

## Learning rate

You don't want to set it too small, because you will be stuck in local minimum.

You don't want it to be too large as you will overshoot and diverge.


### Adaptive Learning Rates

Change the learning rate depending on the landscape
- how fast you are learning
- how steep


## Stochastic Gradient Descent


GD computes the gradient over the entire dataset which can be computationally expensive.


SGD chooses a subset of the data to estimate the gradient

Mini batch Gradient Descent (choose a batch of B data points) to calculate the gradient

Larger batches means you can trust your gradient more and you can use larger learning rate.


If you use 32 data points you can parallelize gradient computation over 32 processors.

## Overfitting


## Regularization

To avoid overfitting.

### Dropout

sets some activation neurons to 0. Forces the network to learn a different pathway. Very power technique as it makes the model that does not rely too much on a fixed set of weights.


Dropout nodes would not have any update, no gradient to compute.

### Early stopping

Stop the training model early.

Training loss always go down.


![alt text](./asstes/images/early_stopping.png)

**In practice you can start plotting this curve and decide when to early stop!**

Ideal Difference between train and test dataset is to be 0. Then you will not know when to stop. This usually happens in Large Language Models. The dataset is so big that the model itself finds it hard to memorize. So the difference between train and test will be almost always 0.

**Language models usually does not the classical overfitting problems.**


