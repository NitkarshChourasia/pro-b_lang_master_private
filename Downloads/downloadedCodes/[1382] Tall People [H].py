"""
####  Tall People  ####

Create a function that takes a 2D array as an argument and returns the number of people whose view is blocked by a tall person. The concert stage is pointed towards the top of the 2D array and the tall person (represented by a 2) blocks the view of all the people (represented by a 1) behind them.


[Examples]

___
block([
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 2],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1]
]) ➞ 2

# The tall person blocks 2 people behind him thus
# the function returns 2.


block([
  [1, 2, 1, 1],
  [1, 1, 1, 2],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
]) ➞ 5

# There are 2 tall people that block everyone behind
# them. The first tall person in the first row blocks 3
# people behind him while the second tall person in
# the second row blocks 2 people behind him thus the
# function returns 5.


block([
  [1, 1, 1, 1],
  [2, 1, 1, 2],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
]) ➞ 4
_____



[Notes]




[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Python | Using 2D arrays/lists the right way
https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
Python | Using 2D arrays/lists the right way
_________
_________
Two-dimensional lists (arrays)
https://snakify.org/en/lessons/two_dimensional_lists_arrays/
In real-world Often tasks have to store rectangular data table. [say more on this!] Such tables are called matrices or two-dimensional arrays. In Python any table can b …
_________

"""
#Your code should go here:

