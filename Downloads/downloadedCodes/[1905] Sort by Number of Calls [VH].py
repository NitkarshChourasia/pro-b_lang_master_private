"""
####  Sort by Number of Calls  ####

Create a function that takes a list of functions and sorts them in ascending order based on how many calls are needed for them to return a non-function.


[Examples]

___
f1 = lambda: "hello"
# f1() ➞ "hello"

f2 = lambda: lambda: "edabit"
# f2()() ➞ "edabit"

f3 = lambda: lambda: lambda: "user"
# f3()()() ➞ "user"

func_sort([f2, f3, f1]) ➞ [f1, f2, f3]
# [f2, f3, f1] ➞ [2, 3, 1] ➞ [1, 2, 3] ➞ [f1, f2, f3]

func_sort([f1, f2, f3]) ➞ [f1, f2, f3]
# [f1, f2, f3] ➞ [1, 2, 3] ➞ [1, 2, 3] ➞ [f1, f2, f3]

func_sort([f2, "func"]) ➞ ["func", f2]
# [f2, "func"] ➞ [2, 0] ➞ [0, 2] ➞ ["func", f2]
_____



[Notes]

___
*) Treat non-functions as needing zero calls.
*) Every function will be called with empty parameters.
*) Every function will need to be called at least once.
*) The potentially returned values include ints, floats, and lists, among others.
___



[closures] [functional_programming] [higher_order_functions] 



-------------------------------------------------------------------
[Resources]
_________
callable() Method
https://docs.python.org/3/library/functions.html#callable
Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will …
_________
_________
Sorting HOW TO
https://docs.python.org/3/howto/sorting.html
Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterable.
_________
_________
Lambda Expressions
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: lambda a, b: a+b. Lambda functions can be used whe …
_________

"""
#Your code should go here:

