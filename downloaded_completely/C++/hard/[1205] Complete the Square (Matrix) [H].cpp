/*
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
completeSquare([
  [2, 5]
]) ➞ [
  [2, 5],
  [0, 0]
]

completeSquare([
  [2, 5],
  [1, 7]
]) ➞ [
  [2, 5],
  [1, 7]
]

completeSquare([
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
Vector of Vectors
https://www.geeksforgeeks.org/vector-of-vectors-in-c-stl-with-examples/
Vectors are known as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatical …
_________

*/
//Your code should go here:

