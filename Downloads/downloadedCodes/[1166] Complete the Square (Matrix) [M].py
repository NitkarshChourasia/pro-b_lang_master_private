"""
####  Complete the Square (Matrix)  ####

Sadly, the mathematical world is biased in favor of square matrices. As such, this challenge will help rectangular matrices by making them square.
For example, for the matrix:
___
[
  [1, 2],
  [3, 4],
  [5, 6]
]
_____

This can be done by padding it with a column of zeroes on the right to get:
___
[
  [1, 2, 0],
  [3, 4, 0],
  [5, 6, 0]
]
_____

While for the matrix:
___
[
  [1, 2, 3, 4],
  [5, 6, 7, 8]
]
_____

One can pad it with two rows of zeros at the bottom to get:
___
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
]
_____

Write a function that pads a rectangular matrix with zeros on the right or at the bottom to make it square.


[Examples]

___
complete_square([
  [2, 5]
]) ➞ [
  [2, 5],
  [0, 0]
]

complete_square([
  [2, 5],
  [1, 7]
]) ➞ [
  [2, 5],
  [1, 7]
]

complete_square([
  [1, 2],
  [3, 4],
  [5, 6]
 ]) ➞ [
  [1, 2, 0],
  [3, 4, 0],
  [5, 6, 0]
]
_____



[Notes]

___
*) Matrices should be padded on the right or at the bottom, but not both simultaneously (i.e. the size of the biggest direction shouldn't change).
*) If the input is already a square matrix, just return that matrix.
___



[arrays] [language_fundamentals] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Making a Matrix Square and Padding It with Desired Value in Numpy
https://stackoverflow.com/questions/10871220/making-a-matrix-square-and-padding-it-with-desired-value-in-numpy
Making a Matrix Square and Padding It with Desired Value in Numpy.
_________
_________
numpy.pad
http://docs.scipy.org/doc/numpy/reference/generated/numpy.pad.html
Number of values padded to the edges of each axis. ((before_1, after_1), … (before_N, after_N)) unique pad widths for each axis. ((before, after),) yields same before a …
_________

"""
#Your code should go here:

