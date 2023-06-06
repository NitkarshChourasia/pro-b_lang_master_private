"""
####  Sample Points from a Curve  ####

Create a function that given a type of curve will generate a list containing a samples amount of numbers calculated from said curve.
It's easier to see with a visual representation:

If samples = 3 and curve = "pow", we would sample 3 points along the x axis [0, 0.5, 1] and figure out the value of y, in the case of the pow curve the values are [0, 0.25, 1].


[Examples]

___
samples_from_curve(3, "linear") ➞ [0, 0.5, 1]

samples_from_curve(3, "pow") ➞ [0, 0.25, 1]

samples_from_curve(3, "sqrt") ➞ [0, 0.71, 1]

samples_from_curve(5, "linear") ➞ [0, 0.25, 0.5, 0.75, 1]
_____



[Notes]

___
*) The available curves are linear, pow, sqrt as shown in the picture.
*) All values returned must have a maximum of 2 decimals to avoid floating point problems in the tests.
*) All values returned must be between 0 and 1 (inclusive).
*) The samples parameter will always be ≥ 2.
*) The samples are evenly distributed along the x axis.
___



[algebra] [arrays] [math] 



-------------------------------------------------------------------
[Resources]
_________
Dictionary
https://www.programiz.com/python-programming/dictionary
Learn everything about Python dictionaries; how they are created, accessing, adding, removing elements from them and various built-in methods.
_________

"""
#Your code should go here:

