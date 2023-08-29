# What is CUPED?

CUPED is a well-established variance reduction technique for experiments (paper).

Unlike methods like outlier removal or winsorization, it doesn’t sacrifice any data integrity.

It can be used together with winsorization, which enhances its effectiveness.

It requires pre-experimentation data - which we generally have in Bunsen.

For a rather unpredictable event like ad clicks, we get ~5% reduction in standard deviation (which is ~10% reduction in variance, and experiment run time). For something like sessions, that 5% can increase to something like 30%.



# Predicted uncertainty is not uncertainty. 

So the variance in your experiment metric should only take into account the unpredictable part of your measurement. If you predict that:
- guv A will have 5 sessions during the experiment, and 
- guv B will have 20 sessions,

And when you actually measure the sessions, you get:
- guv A has 4 sessions (-1 from prediction)
- guv B has 21 sessions (+1 from prediction),

Then the variance, or the uncertainty, in your measurement can be calculated on the residuals of your predictions, rather than on the measurements themselves. This gives var([-1, +1]), rather than var([4, 21]), which is a great reduction.
