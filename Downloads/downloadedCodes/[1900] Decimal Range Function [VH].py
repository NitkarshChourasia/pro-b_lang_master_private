"""
####  Decimal Range Function  ####

Create a function that can take 1, 2, or 3 arguments (like the range function) and returns a tuple. This should be able to return float values (as opposed to the range function which can't take float values as a step).


[Examples]

___
drange(1.2, 5.9, 0.45) ➞ (1.2, 1.65, 2.1, 2.55, 3.0, 3.45, 3.9, 4.35, 4.8, 5.25, 5.7)

drange(10) ➞ (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

drange(1, 7, 1.2) ➞ (1, 2.2, 3.4, 4.6, 5.8)
# Here 7 is not included, like in the range function.
_____



[Notes]

Always round values to the number with the most decimal digits (e.g. in the first example, the answer should always be rounded to 2 digits. In the second, it should be rounded to 0 digits and the third, 1 digit).


[algebra] [data_structures] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
round() Function
https://www.programiz.com/python-programming/methods/built-in/round
Returns a floating-point number rounded to the specified number of decimals. In this tutorial, we will learn about Python round() in detail with the help of examples.
_________
_________
numpy.arange
https://numpy.org/doc/stable/reference/generated/numpy.arange.html
Return evenly spaced values within a given interval.
_________
_________
range() Function
https://www.w3schools.com/python/ref_func_range.asp
Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
_________

"""
#Your code should go here:

