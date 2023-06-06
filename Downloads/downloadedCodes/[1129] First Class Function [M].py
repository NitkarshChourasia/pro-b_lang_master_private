"""
####  First Class Function  ####

Create a function that takes a number as its parameter and returns another function. The returned function must take a list of numbers as its parameter, and return a list of the numbers divided by the number that was passed into the first function.


[Examples]

___
first = factory(15)
# returns a function first.

lst = [30, 45, 60]
# 30 / 15 = 2, 45 / 15 = 3, 60 / 15 = 4

first(lst) ➞ [2, 3, 4]
_____

___
second = factory(2)
# returns a function second.

lst = [2, 4, 6]
# 2 / 2 = 1, 4 / 2 = 2, 6 / 2 = 3

second(lst) ➞ [1, 2, 3]
_____



[Notes]

Rounding not required.


[arrays] [closures] [functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
Python Closures
https://www.programiz.com/python-programming/closure
In this tutorial, you'll learn about Python closure, how to define a closure, and the reasons you should use it. Before getting into what a closure is, we have to first …
_________
_________
Closures
https://www.learnpython.org/en/Closures
A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Let us get to it step by step. Firstly, a Nested Functi …
_________
_________
Python Nested Function
https://www.tutorialspoint.com/python-closures
To better understand python closures, lets first understand what’s nested function and python class. In short, python closure is also a function which encapsulates data …
_________

"""
#Your code should go here:

