/*
####  Diagonal Domination  ####

A square matrix (same number of rows as columns) is called row diagonally dominant if "the absolute value of each entry in the main diagonal is strictly larger than the sum of the absolute values of the other entries in that row".
To illustrate ...
___
[
  [10, 3, 6],
  [2, -9, -6],
  [1, -1, 4]
]
_____

The absolute values from top left to bottom right are:
___
*) 10 = First item of first row.
*) 9 = Second item of second row.
*) 4 = Third item of third row.
___

... making a row diagonal dominant total of 23.
In the first row ...
___
*) The value of the row diagonal dominant is 10.
*) The sum of the other absolute values are 3 and 6 make a total of 9.
___

... so far, the matrix is row diagonally dominant, since 10 > 9.
In the second row ...
___
*) The value of the row diagonal dominant is 9.
*) The sum of the other absolute values in the second row are 3 and 6 which make a total of 9.
___

... meaning the matrix is not row diagonally dominant since 9 <= 9.
___
[
  [10, 3, 6],
  [3, -9, -6],
  [1, -1,  4]
]
_____

For a square to be row diagonally dominant, all of the rows in the square have to be like Row 1.
Write a function that determines if a given square matrix is row diagonally dominant.


[Examples]

___
diagDom([
  [2, -1],
  [-1, 2]
]) ➞ true

diagDom([
  [0, 1],
  [1, 0]
]) ➞ false

diagDom([
  [10, 3, 6],
  [2, -9, -6],
  [1, -1, 4]
]) ➞ true

diagDom([
  [10, 3, 6],
  [4, -9, -6],
  [1, -1, 4]
]) ➞ false
_____



[Notes]

As in the examples, the size of the matrices will change, but they will always be square.


[arrays] [language_fundamentals] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
2D Vector In C++ With User Defined Size
https://www.geeksforgeeks.org/2d-vector-in-cpp-with-user-defined-size/
A 2D vector is a vector of vector. Like 2D arrays, we can declare and assign values to a 2D vector! Assuming you are familiar with a normal vector in C++, with the hel …
_________

*/
//Your code should go here:

