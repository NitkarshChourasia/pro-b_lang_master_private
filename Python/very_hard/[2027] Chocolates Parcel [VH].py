"""
####  Chocolates Parcel  ####

Mubashir needs to assemble a parcel of ordered chocolates. He got two types of chocolates:
___
*) Small chocolates (2 grams each)
*) Big chocolates (5 grams each)
___

Create a function that takes three parameters: Number of small available chocolates n_small, number of big chocolates available n_big and desired weight (in grams) of the final parcel order.
The function should return the required number of small chocolates to achieve the goal. The function should return -1 if the goal cannot be achieved by any possible combinations of small and big chocolates.


[Examples]

___
chocolates_parcel(4, 1, 13) ➞ 4
# 4 small chocolates = 8 grams
# 1 big chocolate = 5 grams
# 8 + 5 = 13 grams
# Required number of small chocolates = 4

chocolates_parcel(4, 1, 14) ➞ -1
# You can not make any combination to reach 14 grams.

chocolates_parcel(2, 1, 7) ➞ 1
# 1 big chocolate = 5 grams
# 1 small chocolates = 2 grams
# 5 + 2 = 7 grams
# Required number of small chocolates = 1
_____



[Notes]

___
*) Maximize the use of big chocolates that are available to achieve the desired goal. And only then should you proceed to use the small chocolates.
*) You can't break chocolates into small pieces.
___



[algorithms] [functional_programming] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Diophantine Equation
https://en.wikipedia.org/wiki/Diophantine_equation#:~:text=In%20mathematics%2C%20a%20Diophantine%20equation,the%20unknowns%20take%20integer%20values).
A polynomial equation, usually involving two or more unknowns, such that the only solutions of interest are the integer ones (an integer solution is such that all the u …
_________
_________
Dictionaries in Python
https://realpython.com/python-dicts/
In this tutorial you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, you should have a good …
_________
_________
max() Method
https://www.programiz.com/python-programming/methods/built-in/max
Returns the smallest item in an iterable. It can also be used to find the smallest item between two or more parameters.
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values. In the example below, we use the + operator to add together two values.
_________

"""
#Your code should go here:

