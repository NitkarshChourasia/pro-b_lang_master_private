"""
####  Is the List Circular?  ####

Write a function that determines if a list is circular. A list is circular if its sublists can be reordered such that each sublist's last element is equal to the next sublist's first element.
For example, the list [[1, 1, 1], [9, 2, 3, 4], [4, 1], [1, 2, 5, 7, 9]] is circular because we can re-arrange the elements to create the following list:
___
[[9, 2, 3, 4], [4, 1], [1, 1, 1], [1, 2, 5, 7, 9]]
_____



[Examples]

___
is_circular([[9, 8], [6, 9, 1], [8, 4, 2], [1, 9], [2, 1, 6]]) ➞ True
# Can be reordered: [[9, 8], [8, 4, 2], [2, 1, 6], [6, 9, 1], [1, 9]]

is_circular([[1, 1], [1, 2]]) ➞ False

is_circular([[2, 1], [1, 2]]) ➞ True

is_circular([[2, 1], [1, 2], [2, 1], [1, 3, 1], [1, 4, 4]]) ➞ False
_____



[Notes]

___
*) In a circular re-ordering, the last sublist's last element must be identical to the first sublist's first element.
*) Sublists will contain at least one element.
___



[arrays] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
itertools — Creating iterators for efficient looping
https://docs.python.org/2/library/itertools.html#itertools.permutations
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
_________

"""
#Your code should go here:

