/*
####  Incrementing Rows and Columns  ####

Write a function that takes in three parameters: r, c, i, where:
___
*) r and c are the number of rows and columns to initialize a zero matrix.
*) i represents the list of incrementing operations (+1).
___

And returns the resulting matrix after applying all the increment operations. Each increment operation will add 1 to the rows or columns specified in the incrementing list.
To illustrate:
___
finals(3, 3, ["2r", "2c", "1r", "0c"])

// Initialize a 3 x 3 matrix of zeroes.

[
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

// Apply "2r" (increment index 2 row).

[
  [0, 0, 0],
  [0, 0, 0],
  [1, 1, 1]
]

// Apply "2c" (increment index 2 column).

[
  [0, 0, 1],
  [0, 0, 1],
  [1, 1, 2]
]

// Apply "1r" (increment index 1 row).

[
  [0, 0, 1],
  [1, 1, 2],
  [1, 1, 2]
]

// Apply "0c" (increment index 0 column).
// This is the result you should return.

[
  [1, 0, 1],
  [2, 1, 2],
  [2, 1, 2]
]
_____



[Examples]

___
finals(2, 2, ["0r", "0r", "0r", "1c"]) ➞ [
  [3, 4],
  [0, 1]
]

finals(2, 2, ["0c"]) ➞ [
  [1, 0],
  [1, 0]
]

finals(3, 3, ["0c", "1c", "1c", "2c", "2c", "2c"]) ➞ [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

finals(3, 3, []) ➞ [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
_____



[Notes]

___
*) The 2D matrix is 0-indexed.
*) The matrix created will have at least one row and one column.
*) All increment operations will be exactly +1.
___



[arrays] [higher_order_functions] 



-------------------------------------------------------------------
[Resources]
_________
Vector of Vectors
https://www.geeksforgeeks.org/vector-of-vectors-in-c-stl-with-examples/
Vectors are known as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatical …
_________

*/
//Your code should go here:

