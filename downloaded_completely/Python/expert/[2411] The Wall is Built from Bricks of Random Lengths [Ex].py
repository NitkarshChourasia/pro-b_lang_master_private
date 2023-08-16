"""
####  The Wall is Built from Bricks of Random Lengths  ####

Your function is given a list of rows (the wall). Each row consists of bricks of differing lengths. The sum of brick’s lengths in each row is the same. Imagine a vertical line inside the interval (0, total_row_len), i.e. not at the most left or most right points, inside. This line crosses a certain number of bricks at some rows. If the line passes at a point where one brick finishes and the next one begins, then it does not cross a brick at this row. Find a horizontal point in which the vertical line crosses the least amount of bricks from all the rows. Return the minimum number of crossed bricks.


[Examples]

___
least_bricks_cross([
  [1, 2, 2, 1],
  [3, 1, 2],
  [1, 3, 2],
  [2, 4],
  [3, 1, 2],
  [1, 3, 1, 1]
]) ➞ 2

# At point x = 4, the line crosses the first and fourth row from the above.
_____

___
least_bricks_cross([
  [1], [1], [1]
]) ➞ 3

# At any point within (0, 1) the line will cross all three bricks.
_____

___
least_bricks_cross([
  [5, 4, 1, 5, 5],
  [1, 2, 3, 2, 2, 4, 4, 2],
  [5, 3, 5, 1, 3, 3],
  [3, 5, 5, 2, 5]
]) ➞ 1

# At point x = 8, the line crosses the first row.
_____



[Notes]

N/A


[algorithms] [arrays] [control_flow] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Python max()
https://www.programiz.com/python-programming/methods/built-in/max
The max() function returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
_________

"""
#Your code should go here:

