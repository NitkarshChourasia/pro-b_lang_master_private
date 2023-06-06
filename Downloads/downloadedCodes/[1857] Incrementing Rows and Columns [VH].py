"""
####  Incrementing Rows and Columns  ####

Write a function that takes in three parameters: r, c, i, where:
___
*) r and c are the number of rows and columns to initialize a zero matrix.
*) i represents the list of incrementing operations (+1).
___

And returns the resulting matrix after applying all the increment operations. Each increment operation will add 1 to the rows or columns specified in the incrementing list.
To illustrate:
___
final(3, 3, ["2r", "2c", "1r", "0c"])

# Initialize a 3 x 3 matrix of zeroes.

[
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

# Apply "2r" (increment index 2 row).

[
  [0, 0, 0],
  [0, 0, 0],
  [1, 1, 1]
]

# Apply "2c" (increment index 2 column).

[
  [0, 0, 1],
  [0, 0, 1],
  [1, 1, 2]
]

# Apply "1r" (increment index 1 row).

[
  [0, 0, 1],
  [1, 1, 2],
  [1, 1, 2]
]

# Apply "0c" (increment index 0 column).
# This is the result you should return.

[
  [1, 0, 1],
  [2, 1, 2],
  [2, 1, 2]
]
_____



[Examples]

___
final(2, 2, ["0r", "0r", "0r", "1c"]) ➞ [
  [3, 4],
  [0, 1]
]

final(2, 2, ["0c"]) ➞ [
  [1, 0],
  [1, 0]
]

final(3, 3, ["1c", "2c", "2c", "3c", "3c", "3c"]) ➞ [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

final(3, 3, []) ➞ [
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
Python Matrix and Introduction to NumPy
https://www.programiz.com/python-programming/matrix
You can treat lists of a list (nested list) as matrix in Python. However, there is a better way of working Python matrices using NumPy package. NumPy is a package for s …
_________
_________
Python Matrix: Transpose, Multiplication, NumPy Arrays Examples
https://www.guru99.com/python-matrix.html
What is Python Matrix? A Python matrix is a specialized two-dimensional rectangular array of data stored in rows and columns. The data in a matrix can be numbers, strin …
_________
_________
range() Method
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________

"""
#Your code should go here:

