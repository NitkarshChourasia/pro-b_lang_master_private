"""
####  Hall Monitor 2  ####

A floor plan is arranged as follows:
___
*) You may freely move between rooms 1 and 2.
*) You may freely move between rooms 3 and 4.
*) However, you can enter the hallway to move between rooms 2 and 4.
___


Create a function that validates whether the route taken between rooms is possible. The hallway will be given as the letter "H".


[Examples]

___
possible_path([1, 2, "H", 4, 3]) ➞ True

possible_path(["H", 1, 2]) ➞ False

possible_path([4, 3, 4, "H", 4, "H"]) ➞ True
_____



[Notes]

___
*) A route may begin or end in any room (including the hallway).
*) All inputs are either numbers 1-4 or the letter "H".
*) No rooms will repeat.
___



[algorithms] [interview] [objects] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
Are used to store data values in key: value pairs.
_________
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it. In this tutorial, we will learn about Python zip() in detail with the help of examples.
_________
_________
all() Function
https://www.programiz.com/python-programming/methods/built-in/all
Returns True if all elements in the given iterable are true. If not, it returns False.
_________

"""
#Your code should go here:

