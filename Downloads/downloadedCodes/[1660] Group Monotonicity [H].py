"""
####  Group Monotonicity  ####

Create a function which returns the indices where the monotonicity of a 1-D list changes. If there are none, return an empty list. A monotonic list is one that is either non-increasing or non-decreasing.


[Examples]

___
group_monotonic([0, 1]) ➞ []

group_monotonic([0, 2, 1]) ➞ [1]

group_monotonic([0, 1, 1, 0]) ➞ [2]
_____



[Notes]

___
*) Trivially, all points and line-segments are monotonic (see example #1).
*) Return the indices where each monotonic section stops, not where each new one begins: i.e. return the "peaks" of the triangles (see example #2).
*) Monotonic lists are allowed to be constant (see example #3).
*) You can expect positive and negative values in the list.
___



[algorithms] [math] 



-------------------------------------------------------------------
[Resources]
_________
Monotonic Function
https://en.wikipedia.org/wiki/Monotonic_function
In mathematics, a monotonic function[1] [2](or monotone function[3]) is a function between ordered sets that preserves or reverses the given order. This concept first a …
_________
_________
Python's range() Function Explained
https://www.pythoncentral.io/pythons-range-function-explained/
A look at Python's range() function. It's usage, along with an explanation about xrange(). Their differences, and how to use range() with floats!
_________
_________
range() Constructor
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence object of integers between the given start integer to the stop integer.
_________
_________
append() Method
https://www.programiz.com/python-programming/methods/list/append
Adds an item to the end of the list.
_________
_________
copysign() Method
https://www.tutorialgateway.org/python-copysign/
Used to find the absolute value of the first argument and return the absolute value with sign specified in second argument.
_________
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________

"""
#Your code should go here:

