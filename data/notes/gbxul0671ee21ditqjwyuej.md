# Chapter 1. Introduction to Casual Inference

- "Association is not causation", but sometimes association is causation..
- association is when two quantities or random variables move together, whereas causality is when change in one variable causes change in another.
- you want to know cause-and-effect relationships so taht you can **intervene** on the cause to bring upon a desired effect
- in forecasting association is enough tbh. 
- predictive models (e.f ARIMA, ML models, regression, neural networks) are effective even witouth establishing causal relationship. They are based on **observed patterns**.
- limitation of predictive mdoels is although they can provide accurate forecats they may not perform well if the underlying relationship change. They do not provide insights into how or why the change occur.
- **The fundamental problem of casual inference is that you can never observe the same unit with and without treatment**
- **spillover or network** effects in experiments. Vaccinating one person will make other people less likely to get illness. Control grou might be affected.
- this is the SUTVA assumption, stable unit of threatment value, threating one unit does not influece other units behaviour


## When Causality Matters

Usually when you need to intervene or control the behaviour of outcomes. For example in policy making, healthcare (you want the drug to work) or at tech companies when you add new features in the app. Causality matters in **decision making** and it the industry it becomes a **decision science**.

Causal models are more robust to changes in the environment since the focus on the underlying mechanisms rather than just on the observed patterns.

- casual inference is great for "what if" questions, ML is just awfult at those types of questions
- "the new wave of artificial intelligence does not actuallybring intelligence but instead a critical component of intelligence - **prediction**"
- ML requirement is to frame the problem as prediction one. e.g want to translate from english to portuguese, then build ML model that predicts Portuguese sentences when given English sentences.
- ML is very good under problems with rigid boundaries


## Causal Models

**Notation:**

$$
T \leftarrow f_{t}(u_{t}) \newline
Y \leftarrow f_{y}(T, u_{y})
$$


The treatment is a random variable that depends on exogeneous vairable $u_{t}$. The outcome $Y$ is a random variable that depends on the threatment $T$ and on endogeneous variable $u_{y}$.

Now with this framework, we can start interventions. What would happendi f we set the threatment to $t_{0}$

$$
T \leftarrow t_{0}\newline
Y \leftarrow f_{y}(T, u_{y})
$$

**Definition.** When we intervene we define the *do(.)* operator.

$$
E[Y|T=1] \neq E[Y|do(T=1)]
$$

LHS is an obervations, whereas the right hand side is the truth. In practice you apply threatment $T=1$ to only a subset of observations, whereas the RHS tells you what would happen if you apply to all observations.



### Individual threatment effect

This is the difference between counterfactual(not able to observe) vs factual (able to observe).

For an individual unit $i$, the **indivudual threatment effect is**:
$$
\rho_{i} = Y_{i}|do(T=1) -Y_{i}|(T=0) = Y_{1i} - Y_{0i}
$$

Due to the fundamental problem of causal inference, you can only observe one term of the preceding equation. So, even though you can express the term theoretically, it doesn't necessarily mean you can recover it from data. From data we will make an estimate!

### Casual Quantities of Interest

Average threatment effect:

$$
ATE = E[Y_{1i}-Y_{0i}]
$$ 

usually we can replace the expectation with sample average, estimation.

In practice you cannot do this since you cannot observe the two states of the same unit.

Average threatment effect on the treated:

$$
ATT = E[Y_{1i}-Y_{0i}|T=1]
$$

you want to estimate this value in cases you want to understand what is the threatment effect on the threated group. You run a marketing campaign and want to understand the actual profit rather then what would have happed withought the campaign for which you use ATE.


Conditional average threatment effect

$$
CATE = E[Y_{1i}-Y_{0i}|X=x]
$$

effect of a drug on customers older than 45 years old.


### What happens in practice when we estimate ATE, ATT and CATE


Assume that we have a random variable $Y$ (quantity of intersest in experiment, e.g number of clicks).

that is the amount of clicks $Y_1$ when treated, i.e $T=1$ and the amount of clicks $Y_0$ when not treated, i.e $T=0$. Note all quantities are random variables.

The **association** between the treatement and the outcome is measured by $E[Y|T=1] - E[Y|T=0]$ and is the value we can observe/estimate. **Causation** is measured by $E[Y|do(T=1)] - E[Y|do(T=0)]$

$$
E[Y|T=1] - E[Y|T=0] \newline 
= E[Y_{1}|T=1] - E[Y_{0}|T=1] \newline 
= E[Y_{1}-Y_{0}|T=1] + E[Y_{0}|T=1] - E[Y_{0}|T=0]\newline 
= ATT + BIAS
$$

So in practice intead of observing $ATT$ only we observe $ATT + BIAS$. Not that bias is the difference between the averages of the **untreated** samples  that we decide to treat $T=1$ and thos that we do not want to treat $T=0$.


**Definition:** Treated and control groups are *interchangable* if
- treatment and control group are comparable regardless of the treatement $E[Y_{0}|T=1] = E[Y_{0}]|T=0$, that is zero bias, and this means that association = causation
- treatment and control group respond similarly under treatement $E[Y_{1}|T=1] = E[Y_{1}]|T=0$. Then $$ATT = ATE$$, treatment effect on the treated is no different than all.

**Exchangable, interchangable, independent** control and treatment groups refer all to the same assumptions. $(Y_{0}, Y_{1}) \perp T$

This assumption means **treated and untreated** control and treatment groups are comparable and indistinguishable.

Identification is the process of making this assumption correct.


# Chapter 2. Randomized Experiments and Stats Review

Main assumption we need in casual inference is "“Treatment & control groups are comparable regardless of treatment”"

**Key idea:** assigning the treatment randomly “brute-forces” this.


RCT = Randomized Control Trials


**Randomized vs Systematic Error**

Systematic errors are consistent biases that affect all measurements in the same way, while random errors are unpredictable fluctuations in daa due to chance.



In the previous chapter we calculated $ATT$, $ATE$ estimates. How confident can we be in them? We need hypothesis testing, standdard error, CI, p-values caluations for this.


Causual Inference two steps:

1. Identation - going from unobservable causal quantities to observable statistical quantitites that you can estimate.
2. Estimation - hypothesis testing.