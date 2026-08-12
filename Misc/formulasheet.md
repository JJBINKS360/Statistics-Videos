# Welcome back!

### In this video, we'll go over everything that you can find on your formula sheet.

This video is based off of the 2020 Formulas and Tables Sheet provided by CollegeBoard for AP Statistics, although all the concepts will apply to Math 1040.

I will go through these in the order found on the sheet, so this will be a fairly long video. Please feel free to skip around.
***


# Descriptive Statistics

> These formulas relate to common values that describe a quantitative **sample** distribution.

## $\overline{x}$, the Sample mean

### $$\overline{x} = \frac{1}{n}\sum{x_i} = \frac{\sum{x_i}}{n} = \frac{x_1+x_2+x_3+\cdots+x_i}{n}$$
Where:
* $\overline{x}$ is your sample mean
* $n$ is the number of values in your sample
* $x_i$ is the $i^{th}$ value in your sample

> The sample mean, written as $\overline{x}$ (pronounced "ex-bar"), is the **calculated arithmetic mean**, or average, of a collected sample.

In plain English, the sample mean is the result of summing every collected data point, and dividing by the quantity of data points collected. ***This is not the same as the population mean***, which is the true mean for all possible data points. However, as your sample count ($n$) increases, the sample mean begins to more accurately represent the population mean:
$$\lim_{n\to\infty} \frac{\sum{x_i}}{n}=x$$

The "Vinculum", (also known as an "overline" or simply a "bar"), denotes that the value we are dealing with is a sample mean of some variable, which doesn't always have to be $x$. For instance, you can have $\overline{x}$, $\overline{y}$, and $\overline{z}$, which all show that you took a sample and are storing the **sample mean** in the respective variable. 

## $\hat{y}$, the Estimated Value

### $$\hat{y} = a+bx$$
Where:
* $\hat{y}$ is the Estimated Value of y
* $a$ is the mean value of the response variable when the explanatory is zero
* $b$ is the mean change in the response variable per one unit increase in the explanatory variable
* $x$ is the desired explanatory variable

> The estimated value, written as $\hat{y}$ (pronounced "Y-Hat"), is the estimated (or expected/predicted/projected) value of the response variable $y$ for a specific value of the explanatory variable $x$.

Because it is impossible to deterministically predict the output value, you need to make it clear when using linear regression that it is the *expected* value of $y$ for an input of $x$. Otherwise, the equation closely follows the standard $a+bx$ form for slope intercept, which can be a helpful reminder.

The "hat" symbol ($\ \hat{}\ $) that appears on the top of the variable $y$ tells us that the variable we are dealing with is estimated from existing data.

## $r$, the Spearman's Correlation Coefficient

### $$r = \frac{1}{n-1} \sum{(\frac{x_i-\overline{x}}{s_x}})(\frac{y_i-\overline{y}}{s_y})$$
Where:
* r is the Speraman's Correlation Coefficient
* n is the number of datapoints in your sample
* $x_i$ is the $i^{th}$ $x$ value in your sample
* $\overline{x}$ is the overall sample mean of the $x$ values in your sample
* $s_x$ is the sample standard deviation of $x$ for your sample
* $y_i$ is the $i^{th}$ $y$ value in your sample
* $\overline{y}$ is the overall sample mean of the $y$ values in your sample
* $s_y$ is the sample standard deviation of $y$ for your sample

> The Spearman's Correlation Coefficient is a value from $-1$ to $1$ that describes the correlation and spread of the data points collected across two different quantitative variables, with respect to the direction.

A value of $1$ would represent a perfect, positive, and linear correlation between the two variables. If the points were plotted on a scatter plot, there would be a perfectly straight line passing diagonally upwards through the points (positive slope).

A value of $-1$ would represent a perfect, negative, and linear correlation between the two variables. If the points were plotted on a scatter plot, there would be a perfectly straight line passing diagonally downwards through the points (negative slope).

A value of $0$ would represent there being no correlation at all between the points.

Any intermediate values describe varying strengths of correlation.

## $s_x$, the Sample Standard Deviation

### $$s_x = \sqrt{\frac{1}{n-1}\sum{(x_i - \overline{x})^2}} = \sqrt{\frac{(x_i - \overline{x})^2}{n-1}}$$
Where:
* $s_x$ is the sample standard deviation of x
* $n$ is the number of datapoints in your sample
* $x_i$ is the $i^{th}$ $x$ value in your sample
* $\overline{x}$ is the overall sample mean of the $x$ values in your sample

> The Sample Standard Deviation is defined as the estimated average difference from the mean across a sample

We use a different formula for the **sample** standard deviation than the population standard deviation, because when we calculate from a sample, we tend to under-represent the true variability in the population. To remedy this, we calculate using $\frac{1}{n-1}$ instead of $\frac{1}{n}$

## $\overline{y}$, the Expected Mean

### $$\overline{y}=a+b\overline{x}$$
Where:
* $\overline{y}$ is the Estimated Mean of y
* $a$ is the mean of the response variable when the mean of the explanatory variable is zero
* $b$ is the mean change in the response mean per one unit increase in the mean of the explanatory variable
* $\overline{x}$ is the desired explanatory mean

This is a lot of means, but it essentially functions in the same way when you're talking about predicting means using linear regression (Least-Squares regression line)
For instance, when you're comparing individually calculated means as your data points (i.e. comparing GP**A** in college to GP**A** in high school)

## $b$, the Slope

### $$b=r\frac{s_y}{s_x}$$
Where:
* $b$ is the slope of the least-squares regression line
* $r$ is the Pearson's correlation coefficient of the sampled data
* $s_x$ is the sample standard deviation of the $x$ values
* $s_y$ is the sample standard deviation of the $y$ values

> The slope of a Least-Squares Regression Line is the rate of change of a straight line through your collected data that would ensure the residuals are normally distributed.

Used best in significance tests for linear regression and for calculating estimated values for response variables.

