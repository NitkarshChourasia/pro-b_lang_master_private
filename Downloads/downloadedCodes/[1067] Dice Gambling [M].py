"""
####  Dice Gambling  ####

Create a function that takes a list consisting of dice rolls from 1-6. Return the sum of your rolls with the following conditions:



[Examples]

___
rolls([1, 2, 3]) ➞ 4
# The second roll, 2, counts as 0 as a result of rolling 1.

rolls([2, 6, 2, 5]) ➞ 17
# The 2 following the 6 was multiplied by 2.

rolls([6, 1, 1]) ➞ 8
# The first roll makes the second roll worth 2, but the
# second roll was still 1 so the third roll doesn't count.
_____



[Notes]

Even if a 6 is rolled after a 1, 6 isn't summed but the 6's "effect" still takes place.


[algorithms] [conditions] [games] [math] 



-------------------------------------------------------------------
[Resources]
_________
Using the Python zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
If you use zip() with n arguments, then the function will return an iterator that generates tuples of length n.
_________
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
range() Method
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________

"""
#Your code should go here:

