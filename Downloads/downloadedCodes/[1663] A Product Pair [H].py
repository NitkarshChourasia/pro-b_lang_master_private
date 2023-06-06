"""
####  A Product Pair  ####

Mubashir needs your help in a simple task of multiplication of elements in a given list.
Create a function which takes a list of integers lst and a positive integer k and returns the minimum and maximum possible product of k elements taken from the list. If enough elements are not available in the list, return None.


[Examples]

___
product_pair([1, -2, -3, 4, 6, 7], 1) ➞ (-3, 7)

product_pair([1, -2, -3, 4, 6, 7], 2) ➞ (-21, 42)
# -3*7, 6*7

product_pair([1, -2, -3, 4, 6, 7], 3) ➞ (-126, 168)
# -3*6*7, 4*6*7

product_pair([1, -2, -3, 4, 6, 7], 7) ➞ None
# There are only 6 elements in the list
_____



[Notes]

N/A


[algorithms] [arrays] [logic] [loops] 



-------------------------------------------------------------------
[Resources]
_________
itertools.combinations()
https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/
Given an array of size n, generate and print all possible combinations of r elements in array.
_________
_________
reduce() Method
https://www.geeksforgeeks.org/reduce-in-python/
Used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” mo …
_________

"""
#Your code should go here:

