"""
####  Bingo Check  ####

Create a function that takes a 5x5 2D list and returns True if it has at least one Bingo, and False if it doesn't.


[Examples]

___
bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
]) ➞ True

bingo_check([
  ["x", 43, 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, 65, "x", 83, 54],
  [67, 98, 39, "x", 44],
  [21, 59, 24, 30, "x"]
]) ➞ True

bingo_check([
  ["x", "x", "x", "x", "x"],
  [64, 12, 47, 32, 90],
  [37, 16, 68, 83, 54],
  [67, 19, 98, 39, 44],
  [21, 75, 24, 30, 52]
]) ➞ True

bingo_check([
  [45, "x", 31, 74, 87],
  [64, 78, 47, "x", 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, "x", 44],
  [21, "x", 24, 30, 52]
]) ➞ False
_____



[Notes]

Only check for diagonals, horizontals and verticals.


[algorithms] [arrays] [conditions] 



-------------------------------------------------------------------
[Resources]
_________
range() Function
https://www.w3schools.com/python/ref_func_range.asp
Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
_________
_________
numpy.vstack() Function
https://www.geeksforgeeks.org/numpy-vstack-in-python/
Is used to stack the sequence of input arrays vertically to make a single array.
_________
_________
numpy.rot90() Function
https://www.geeksforgeeks.org/numpy-rot90-python/
Performs rotation of an array by 90 degrees.
_________
_________
numpy.diag() Function
https://www.geeksforgeeks.org/numpy-diag-python/
Extracts a diagonal or constructs a diagonal array.
_________

"""
#Your code should go here:

