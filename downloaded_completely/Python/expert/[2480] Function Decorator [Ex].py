"""
####  Function Decorator  ####

Functions in Python are first class citizens. This means that they support operations such as being passed as an argument, returned from a function, modified, and assigned to a variable.
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Create a function decorator that wraps a function, making a new function with extended behavior. The input is a simple mathematical function y(x). The output is a function f(val, dict) with the following properties:
___
*) If val is a single number then f returns y(val).
*) If val is a string equal to "length" or "area" then f returns a piece-wise linear approximation of the curve length or trapezoidal approximation of the area under the curve. The region for the curve length or area is provided in the dictionary (e.g. {"begin": -3, "end": 2, "step": 0.1}).
*) If len(vals) is not equal to one or if it is not a string "length" or "area" then f returns None.
___



[Examples]

___
f = decor(lambda x: x * x)
f() ➞ None
f(3) ➞ 9
f(3, 4) ➞ None
f("volume", **{"begin": 0, "end": 2, "step": 0.001}) ➞ None
f("area", **{"begin": 0, "end": 2, "step": 0.001}) ➞ 2.67
_____



[Notes]

___
*) No need to round the results, it’s done in the tests.
*) The returned function f should accept positional and keyword arguments.
___



[functional_programming] [math] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

