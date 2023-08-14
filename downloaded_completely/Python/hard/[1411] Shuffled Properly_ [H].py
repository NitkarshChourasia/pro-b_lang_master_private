"""
####  Shuffled Properly?  ####

Given a list of 10 numbers, return whether or not the list is shuffled sufficiently enough. In this case, if 3 or more numbers appear consecutively (ascending or descending), return False.


[Examples]

___
is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) ➞ False
# 1, 2, 3 appear consecutively

is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) ➞ False
# 9, 8, 7, 6 appear consecutively

is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) ➞ True
# No consecutive numbers appear

is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) ➞ True
# No consecutive numbers appear
_____



[Notes]

___
*) Only steps of 1 in either direction count as consecutive (i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)).
*) You will get numbers from 1-10.
___



[arrays] [loops] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
You'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables in parallel and create dictionar …
_________
_________
Any All
https://www.geeksforgeeks.org/any-all-in-python/
Any Returns true if any of the items is True. It returns False if empty or all are false. Any can be thought of as a sequence of OR operations on the provided iterables …
_________

"""
#Your code should go here:

