"""
####  Wrong Number  ####

Mubashir needs your help to find out a wrong number in a 2D list.
Imagine a 2D list of numbers given below:
___
lst = [
  [1, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]
_____

You can notice that:
___
*) The end number of each row is the sum of each row's previous numbers.
*) The end number of each column is the sum of each column's previous numbers.
___

See below examples for a better understanding:
___
lst1 = [
  [2, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]

# 2 is incorrect in first row and first column.
# Replace it with 1.

lst2 = [
  [1, 2, 3, 7 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]

# 7 is incorrect in first row and fourth column.
# Replace it with 6.

lst3 = [
  [1, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,46]
]

# 46 is incorrect in fourth row and fourth column.
# Replace it with 45.
_____



[Examples]

___
wrong_number(arr1) ➞ 1

wrong_number(arr2) ➞ 6

wrong_number(arr3) ➞ 45
_____



[Notes]

N/A


[algorithms] [loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
reduce() Method
https://www.geeksforgeeks.org/reduce-in-python/
Used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” mo …
_________

"""
#Your code should go here:

