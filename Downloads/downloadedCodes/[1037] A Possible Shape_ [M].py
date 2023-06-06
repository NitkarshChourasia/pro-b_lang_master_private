"""
####  A Possible Shape?  ####

Given the number n and a list of interior angles angles, return whether or not it's possible to make a convex polygon with n sides with the angles given. Remember that angles must be under 180°.
___
is_shape_possible(3, [80, 70, 30]) ➞ True
_____


A shape with 3 sides and the angles 80°, 70° and 30° is a possible shape.


[Examples]

___
is_shape_possible(4, [90, 90, 90, 90]) ➞ True

is_shape_possible(3, [20, 20, 140]) ➞ True

is_shape_possible(1, [21]) ➞ False
# n must be larger than 2

is_shape_possible(5, [500, 10, 10, 10, 10]) ➞ False
# You can't have an interior angle bigger than 180°
_____



[Notes]

___
*) Return False if n is less than 3 (see example #3).
*) There will always be an n number of positive integers given as angles.
*) The sum of interior angles is (n - 2) x 180°.
___



[math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Rules for Interior Angles
https://www.mathsisfun.com/geometry/interior-angles-polygons.html
An explanation for calculating the sum of the interior angles in an N sided shape.
_________
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________
_________
max() Function
https://www.programiz.com/python-programming/methods/built-in/max
Returns the largest item in an iterable. It can also be used to find the largest item between two or more parameters.
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________

"""
#Your code should go here:

