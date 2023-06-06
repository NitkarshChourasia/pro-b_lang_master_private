"""
####  Strictly Increasing or Decreasing  ####

Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.


[Examples]

___
check([1, 2, 3]) ➞ "increasing"

check([3, 2, 1]) ➞ "decreasing"

check([1, 2, 1]) ➞ "neither"

check([1, 1, 2]) ➞ "neither"
_____



[Notes]

___
*) The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater than the 0-indexed 1.
*) Input lists have a minimum length of 2.
___



[arrays] [conditions] [control_flow] [loops] 



-------------------------------------------------------------------
[Resources]
_________
How to check list monotonicity?
https://stackoverflow.com/questions/4983258/python-how-to-check-list-monotonicity
What would be an efficient and pythonic way to check list monotonicity? i.e. that it has monotonically increasing or decreasing values? Examples: [0, 1, 2, 3, 3, 4] …
_________
_________
Any & All in Python?
https://www.tutorialspoint.com/any-and-all-in-python
Python provides two built-ins functions for “AND” and “OR” operations are All and Any functions.Python any() functionThe any() function returns True if ...
_________
_________
Reverse a List
https://www.techbeamers.com/reverse-list-python/
This tutorial provides five ways to reverse a list in Python such as list.reverse(), reversed(), slice, for loop, and list comprehension.
_________
_________
sorted() Function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________
_________
enumerate() Method
https://www.w3schools.com/python/ref_func_enumerate.asp
Takes a collection (e.g. a tuple) and returns it as an enumerate object. The enumerate() function adds a counter as the key of the enumerate object.
_________

"""
#Your code should go here:

