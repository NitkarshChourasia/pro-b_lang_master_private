"""
####  Matrix Padder  ####

Create a function that takes a matrix of size (m, n) and returns a matrix of size (m+2, n+2) with a pad of 0s around the perimeter.


[Examples]

___
pad_matrix([[]]) ➞ [[0, 0], [0, 0], [0, 0]]

pad_matrix([[9]]) ➞ [
  [0, 0, 0],
  [0, 9, 0],
  [0, 0, 0]
]

pad_matrix([["hi", True]]) ➞ [
  [0, 0, 0, 0],
  [0, "hi", True, 0],
  [0, 0, 0, 0]
]

pad_matrix([
  [1, 2, 5],
  [8, 6, 7],
  [3, 4, 9]
]) ➞ [
  [0, 0, 0, 0, 0],
  [0, 1, 2, 5, 0],
  [0, 8, 6, 7, 0],
  [0, 3, 4, 9, 0],
  [0, 0, 0, 0, 0]
]
_____



[Notes]

___
*) All inputs will be lists of lists.
*) Refer to the first example to handle an empty input.
___



[arrays] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Python List of Lists
https://blog.finxter.com/python-list-of-lists/
A helpful illustrated guide to nested lists in Python.
_________

"""
#Your code should go here:

