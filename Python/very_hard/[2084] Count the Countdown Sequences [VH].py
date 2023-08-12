"""
####  Count the Countdown Sequences  ####

A countdown sequence is a descending sequence of k integers from k down to 1 (e.g. 5, 4, 3, 2, 1). Write a function that returns a list [x, y] where x is the number that represents how many of countdown sequences are in a given list and y is a list of those sequences in order which they appear in the list.


[Examples]

___
final_countdown([4, 8, 3, 2, 1, 2]) ➞ [1, [[3, 2, 1]]]
# In this example we have 1 countdown sequence: 3, 2, 1

final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]) ➞ [2, [[5, 4, 3, 2, 1], [3, 2, 1]]]
# We have 2 countdown sequences:
# 5, 4, 3, 2, 1 and 3, 2, 1

final_countdown([4, 3, 2, 1, 3, 2, 1, 1]) ➞ [3, [[4, 3, 2, 1], [3, 2, 1], [1]]]
# We have 3 countdown sequences:
# 4, 3, 2, 1 ; 3, 2, 1 and 1

final_countdown([1, 1, 2, 1]) ➞ [3, [[1], [1], [2, 1]]]

final_countdown([]) ➞  [0, []]
_____



[Notes]

___
*) [1] is a valid countdown sequence.
*) All numbers will be greater than 0.
___



[algorithms] [arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Indexing and Slicing for Lists and other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
Python, one of the most in-demand machine learning languages, supports slice notation for any sequential data type like lists, strings, and others.
_________
_________
Python Nested Loops
https://www.tutorialspoint.com/python/python_nested_loops.htm
Python programming language allows to use one loop inside another loop. Following section shows few examples to illustrate the concept.
_________
_________
Functions Creating Iterators for Efficient Looping
docs.python.org/3/library/itertools.html
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
_________

"""
#Your code should go here:

