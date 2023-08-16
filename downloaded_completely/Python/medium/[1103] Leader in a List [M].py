"""
####  Leader in a List  ####

Create a function that finds each number in the given list that is greater than every number that comes after it. Your solution should return a list of the number(s) that meet these criteria.


[Examples]

___
leader([2, 3, 20, 15, 8, 3]) ➞ [20, 15, 8, 3]
# Note that 20 is greater than all the elements to it's
# right side, similarly 15 and so on.

leader([2, 3, 20, 15, 8, 25, 3]) ➞ [25, 3]
# Note that 20 cannot be added because it is not greater than 25.

leader([1, 2, 3, 4, 5]) ➞ [5]
# 5 is technically greater than the (zero) remaining items.

leader([8, 7, 1, 2, 10, 3, 5]) ➞ [10, 5]
# 10 is greater than all items to the right of it, so include.
# 3 is not greater than all items to the right of it, so exclude.
# 5 is greater than the remaining items, so include.
_____



[Notes]

Add elements in the new list in the same order they occur in the input list.


[arrays] [language_fundamentals] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Any All in Python
https://www.geeksforgeeks.org/any-all-in-python/
Any returns true if any of the items is True. It returns False if empty or all are false. Any can be thought of as a sequence of OR operations on the provided iterables …
_________
_________
Python max() Function
https://www.w3schools.com/python/ref_func_max.asp
Returns the item with the highest value, or the item with the highest value in an iterable. If the values are strings, an alphabetically comparison is done.
_________
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________
_________
List insert() Method
https://www.w3schools.com/python/ref_list_insert.asp
Inserts the specified value at the specified position.
_________

"""
#Your code should go here:

