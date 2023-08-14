"""
####  Roll the Dice  ####

Las Vegas style dice have 6 sides numbered 1 to 6. When rolling 2 dice, a six is 5 times more likely than a two because a six can be rolled 5 different ways (1 + 5, 5 + 1, 2 + 4, 4 + 2, 3 + 3), while a two can only be rolled 1 way (1 + 1).
Create a function that accepts two arguments:the number of dice rolled, and the outcome of the roll. The function returns the number of possible combinations that could produce that outcome. The number of dice can vary from 1 to 6.
For the example given above:
___
*) dice_roll(2, 6) would return 5
*) dice_roll(2, 2) would return 1
___



[Examples]

___
dice_roll(1, 3) ➞ 1

dice_roll(2, 5) ➞ 4
# 1 + 4, 4 + 1, 2 + 3, 3 + 2

dice_roll(3, 4) ➞ 3
# 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1

dice_roll(4, 18) ➞ 80

dice_roll(6, 20) ➞ 4221
_____



[Notes]

1 + 5 and 5 + 1 are distinct combinations because die #1 can show 1 while die #2 can show 5, or die #1 can show 5 while die #2 can show 1.


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Functions Creating Iterators for Efficient Looping
https://docs.python.org/3/library/itertools.html
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
_________
_________
Itertools in Python 3
https://realpython.com/python-itertools/
Master Python's itertools module by constructing practical examples. We'll start out simple and then gradually increase in complexity, encouraging you to "think iterati …
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
range() Type
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________

"""
#Your code should go here:

