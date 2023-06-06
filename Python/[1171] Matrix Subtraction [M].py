"""
####  Matrix Subtraction  ####

Two matrices must have an equal number of rows and columns to be subtracted. In which case, the subtracted of two matrices A and B will be a matrix which has the same number of rows and columns as A and B.
The result of the subtraction of A and B, denoted A - B is computed by subtracting corresponding elements of A and B.
Create a function that takes 2 x 2D lists lst1 and lst2 as an argument and returns a 2D list (matrix C). C = A-B.


[Examples]

___
subtract_matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
_____



[Notes]

Treat strings of numbers as integers.


[algebra] [arrays] [interview] [math] 



-------------------------------------------------------------------
[Resources]
_________
Adding and Subtracting Matrices
https://www.geeksforgeeks.org/adding-and-subtracting-matrices-in-python/
If shape of two arrays are not same, that is arr1.shape != arr2.shape, they must be broadcastable to a common shape. We can use np.add() method to add elements of two m …
_________
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
Is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other programming langua …
_________
_________
range() Function
https://www.w3schools.com/python/ref_func_range.asp
Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
_________

"""
#Your code should go here:

