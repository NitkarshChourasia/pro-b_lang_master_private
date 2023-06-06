"""
####  Gold Distribution  ####

Mubashir and his friend Matt found some gold piles. They decided to follow simple rules to distribute the gold among them.
___
*) Gold will be divided into n piles.
*) Each person will choose bigger gold pile either from far left or far right.
*) If the weight of both piles is equal then the person will choose left pile.
___

Help them by creating a function that takes an array of gold piles gold and returns a two-element array with [Mubashir's Gold, Matt's Gold].


[Examples]

___
gold_distribution([4, 2, 9, 5, 2, 7]) ➞ [14, 15]
# Mubashir will choose 7, Remaining piles = [4, 2, 9, 5, 2]
# Matt will choose 4, Remaining piles = [2, 9, 5, 2]
# Mubashir will choose 2, Remaining piles = [9, 5, 2]
# Matt will choose 9, Remaining piles = [5, 2]
# Mubashir will choose 5, Remaining piles = [2]
# Matt will choose 2
# Mubashir = 7+2+5 = 14, Matt = 4+9+2 = 15

gold_distribution([10, 1000, 2, 1]) ➞ [12, 1001]

gold_distribution([10, 9, 1, 2, 8, 4]) ➞ [16, 18]
_____



[Notes]

Mubashir gets to pick his gold first!


[algorithms] [arrays] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Remove List Items
https://www.w3schools.com/python/python_lists_remove.asp
The remove() method removes the specified item.
_________
_________
List Methods
https://www.w3schools.com/python/python_lists_methods.asp
Python has a set of built-in methods that you can use on lists.
_________
_________
List pop() Method
https://www.w3schools.com/python/ref_list_pop.asp
Removes the element at the specified position.
_________
_________
Python Operators
https://www.w3schools.com/python/python_operators.asp
Operators are used to perform operations on variables and values.
_________
_________
Python Lists
https://www.w3schools.com/python/python_lists.asp
Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, …
_________
_________
While Loops
https://www.w3schools.com/python/python_while_loops.asp
Requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
_________

"""
#Your code should go here:

