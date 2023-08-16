"""
####  Concert Seats  ####

Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.
Everyone can see the front-stage in the example below:
___
# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.
_____

Not everyone can see the front-stage in the example below:
___
# FRONT STAGE
[[1, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 10, 4, 4], 
[6, 6, 7, 6, 5, 5]]

# The 10 is directly in front of the 6 and blocking its view.
_____

The function should return True if every number can see the front-stage, and False if even a single number cannot.


[Examples]

___
can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]) ➞ True

can_see_stage([
  [0, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ True

can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]) ➞ False

can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]) ➞ False

# Number must be strictly smaller than 
# the number directly behind it.
_____



[Notes]

___
*) Numbers must be strictly greater than the number in front of it.
*) All numbers within the lists will be whole numbers greater than or equal to zero.
___



[arrays] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Any All in Python
https://www.geeksforgeeks.org/any-all-in-python/
Returns true if any of the items is True. It returns False if empty or all are false. Any can be thought of as a sequence of OR operations on the provided iterables. It …
_________
_________
Rotating a Two-Dimensional Array
https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
Method and reason for the method of rotating a two-dimensional array in Python, for those looking to compare sideways arrays.
_________
_________
Two-dimensional Lists (Arrays) in Python
https://snakify.org/en/lessons/two_dimensional_lists_arrays/
Often tasks have to store rectangular data table. [say more on this!] Such tables are called matrices or two-dimensional arrays. In Python any table can be represented …
_________
_________
zip() Method
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it.
_________

"""
#Your code should go here:

