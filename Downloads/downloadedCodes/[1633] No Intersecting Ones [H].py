"""
####  No Intersecting Ones  ####

A no-intersecting ones matrix is one where no two ones exist on the same row or column.
To illustrate:
___
[
  [1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0]
]
_____

The list below is not a non-intersecting ones matrix:
___
[
  [1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

// Column 2 has two 1s.
_____

Write a function that returns True if a 2D matrix is a no-intersecting ones matrix and False otherwise.


[Examples]

___
no_intersecting_nes([
  [0, 1],
  [1, 0]
]) ➞ True

no_intersecting_ones([
  [1, 1],
  [0, 0]
]) ➞ False

no_intersecting_ones([
  [0, 0, 0, 1],
  [1, 0, 0, 0],
  [0, 1, 0, 0]
]) ➞ True
_____



[Notes]

N/A


[arrays] [higher_order_functions] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Sum of Items in List
https://www.geeksforgeeks.org/sum-function-python/
Is required everywhere. Python provides an inbuilt function sum() which sums up the numbers in the list.
_________

"""
#Your code should go here:

