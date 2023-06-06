"""
####  Max Increase While Keeping City Skyline  ####

In a 2 dimensional list, each value represents the height of a building located there. You are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings).
At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance.
Create a function that updates the heights of the buildings to the maximum possible under conditions: keep the original vertical and horizontal skylines; keep the zero heights equal to zero.


[Examples]

___
[
  [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0]
]

# Skyline viewed from top or bottom: [9, 4, 8, 7]
# Skyline viewed from left or right: [8, 7, 9, 3]

[
  [8, 0, 8, 7],
  [7, 4, 7, 7],
  [9, 4, 8, 7],
  [0, 3, 3, 0]
]

# Grid after increasing the height of buildings
# without affecting skylines.
_____



[Notes]

Height 0 is considered to be a protected park and nothing should be built on top of it.


[arrays] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Python For Loops
https://www.w3schools.com/python/python_for_loops.asp
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other program …
_________

"""
#Your code should go here:

