"""
####  Is It a Right-Angled Triangle?  ####

Find out if a right-angled triangle can be made given some facts about the shape.
___
*) Given varying information about a shape, create a function that returns True if the shape could be a right-angle triangle and False if not.
*) You will be given a list of numbers and a string stating whether the numbers are angles or sides.
*) The information may indicate more than one possible shape, but we just need to know if these details could be found in a right-angled triangle.
___



[Examples]

___
is_right_angle([30, 60], "angle") ➞ True
# A third angle could be 90

is_right_angle([20, 20, 20, 20], "angle") ➞ False
# More than 3 sides

is_right_angle([4, 5, 3], "side") ➞ True
# 3**2 + 4**2 = 5**2

is_right_angle([4, 5], "side") ➞ True
# Third side may be 3
_____



[Notes]

Check the Resources for more info on right-angle triangles.


[geometry] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Right Triangle
https://en.wikipedia.org/wiki/Right_triangle
A triangle in which one angle is a right angle (that is, a 90-degree angle). The relation between the sides and angles of a right triangle is the basis for trigonometry.
_________

"""
#Your code should go here:

