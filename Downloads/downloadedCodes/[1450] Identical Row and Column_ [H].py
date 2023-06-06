"""
####  Identical Row and Column?  ####

Write a function that returns True if there exists a row that is identical to a column in a 2-D matrix, otherwise False.
To illustrate:
___
[
  [1, 2, 3, 4],
  [2, 4, 9, 8],
  [5, 9, 7, 7],
  [6, 8, 1, 0]
]

# 2nd row + 2nd column are identical: [2, 4, 9, 8]
_____



[Examples]

___
has_identical([
  [4, 4, 4, 4],
  [2, 4, 9, 8],
  [5, 4, 7, 7],
  [6, 4, 1, 0]
]) ➞ True

has_identical([
  [4, 4, 9, 4],
  [2, 1, 9, 8],
  [5, 4, 7, 7],
  [6, 4, 1, 0]
]) ➞ False

has_identical([
  [4, 4]
  [2, 1]
]) ➞ False

has_identical([
  [4, 2]
  [2, 1]
]) ➞ True
_____



[Notes]

Non-square matrices should return False.


[arrays] [validation] 



-------------------------------------------------------------------
[Resources]
_________
any() Function
https://www.w3schools.com/python/ref_func_any.asp
Returns True if any item in an iterable are true, otherwise it returns False.
_________
_________
zip() Function
https://www.w3schools.com/python/ref_func_zip.asp
Returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator a …
_________

"""
#Your code should go here:

