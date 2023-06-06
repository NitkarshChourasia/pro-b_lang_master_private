"""
####  Shift and Multiple Validators  ####

For this task, you will write two validators.

A few examples to illustrate these respective functions:


[Examples]

___
is_shifted([1, 2, 3], [2, 3, 4]) ➞ True
# Each element is shifted +1

is_shifted([1, 2, 3], [-9, -8, -7]) ➞ True
# Each element is shifted -10

is_multiplied([1, 2, 3], [10, 20, 30]) ➞ True
# Each element is multiplied by 10

is_multiplied([1, 2, 3], [-0.5, -1, -1.5]) ➞ True
# Each element is multiplied by -1/2

is_multiplied([1, 2, 3], [0, 0, 0]) ➞ True
# Each element is multiplied by 0
_____



[Notes]

___
*) The given lists are the same length.
*) Keep in mind one special case: if the second list is a list of only zeroes, then the first list can be anything (the multiplier will be 0).
___



[higher_order_functions] [validation] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it. In this tutorial, we will learn about Python zip() in detail with the help of examples.
_________
_________
len() Function
https://www.programiz.com/python-programming/methods/built-in/len
In this tutorial, we will learn about the Python len() function with the help of examples.
_________
_________
set() Function
https://www.programiz.com/python-programming/methods/built-in/set
The set() builtin creates a Python set from the given iterable. In this tutorial, we will learn about set() in detail with the help of examples.
_________

"""
#Your code should go here:

