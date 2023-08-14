"""
####  Jumbled Equations  ####

In this challenge, you are given a list of one or more arithmetic operators and a list of numbers. Take each of the operators and mate it with any three separate numbers in the list to create a valid equation. Your answer should contain all possible equations.


[Examples]

___
jumbled([["+"], [2, 1, 3]]) ➞ ["1+2=3"]

jumbled(["+", "*"], [36, 28, 71, 4, 12, 7, 11]]) ➞ ["4*7=28", "4+7=11"]

jumbled([["+", "-", "*", "**"], [1, 2, 3, 0]]) ➞ ["1+2=3", "2**0=1", "3**0=1", "3-1=2", "3-2=1"]
# Each equation must contain 3 discrete numbers from the list.
# "1+0=1" or "3-3=0" are not allowed.
_____



[Notes]

___
*) For operators with commutative properties, return only the equation with the smallest term first. "4*6=24" not "6*4=24".
*) Return your answer as a list sorted lexicographically.
___



[arrays] [loops] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
Itertools in Python
https://realpython.com/python-itertools/
Master Python's itertools module by constructing practical examples. We'll start out simple and then gradually increase in complexity, encouraging you to "think iterati …
_________
_________
itertools — Functions creating iterators for efficient looping
https://docs.python.org/3/library/itertools.html
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
_________
_________
eval() Method
https://www.programiz.com/python-programming/methods/built-in/eval
Parses the expression passed to this method and runs python expression (code) within the program.
_________
_________
sorted() Method
https://www.programiz.com/python-programming/methods/built-in/sorted
The sorted() function returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the …
_________

"""
#Your code should go here:

