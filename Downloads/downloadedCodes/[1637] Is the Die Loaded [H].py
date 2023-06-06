"""
####  Is the Die Loaded  ####

The Chi-Squared (χ²) goodness of fit test estimates if an empirical (observed) distribution fits a theoretical (expected) distribution within reasonable margins. For example, to figure out if a die is loaded you could roll it many times and note the results. Because of randomness, you can't expect to get the same frequency for all faces, but if one or more faces turn up much more frequently than some others, it is reasonable to assume the die is loaded.
The formula to calculate the Chi-Square parameter is:

Below is an example of a die rolled 600 times:

In this example, the Chi-Square parameter has a value of:
___
χ² = ((1)^2 + (16)^2 + (-11)^2 + (8)^2 + (-3)^2 + (-11)^2) / 100 = 5.72
_____

This parameter is then compared to a critical value, calculated taking into account the number of categories and the confidence level. Here, the critical value is 11.0705. Since 5.72 < 11.0705, it is safe to assume the die is unloaded.
Given a list with the six observed frequencies, write a function that returns True if a die is unloaded, or False if it is loaded. Take 11.0705 as the critical value for all cases.


[Examples]

___
fair_die([44, 52, 33, 40, 41, 30]) ➞ True
(χ² = 7.75) < 11.0705

fair_die([34, 27, 23, 20, 32, 28]) ➞ True
(χ² = 1.6) < 11.0705

fair_die([10, 20, 11, 5, 19, 16]) ➞ False
(χ² = 12.556) > 11.0705
_____



[Notes]

You can't import any modules.


[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Chi-Square Goodness of Fit Test
https://stattrek.com/chi-square-test/goodness-of-fit.aspx
This lesson explains how to conduct a chi-square goodness of fit test. The test is applied when you have one categorical variable from a single population. It is used t …
_________
_________
Find Average of a List
https://www.geeksforgeeks.org/find-average-list-python/
Given a list of numbers, the task is to find average of that list. Average is the sum of elements divided by the number of elements. In Python we can find the average o …
_________

"""
#Your code should go here:

