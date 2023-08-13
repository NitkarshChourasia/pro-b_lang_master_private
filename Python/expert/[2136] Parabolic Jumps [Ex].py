"""
####  Parabolic Jumps  ####

When a bug jumps to a height y, its position can be plotted as a quadratic function with x as the time, and y as the vertical distance traveled. For example, for a bug that jumps 9 cm up and is back on the ground after 6 seconds, its trajectory can be plotted as:

Create a function that, given the max height of a vertical jump in cm and the current time in milliseconds, returns the current position of the bug rounded to two decimal places, and its direction ("up" or "down"). If the bug is already back on the ground, return 0 for the position and None for the direction.


[Examples]

___
bug_jump(9, 1000) ➞ [5, "up"]

bug_jump(9, 4000) ➞ [8, "down"]

bug_jump(9, 5500) ➞ [2.75, "down"]

bug_jump(9, 7000) ➞ [0, None]
_____



[Notes]

___
*) Time and position both start at 0.
*) You only need to translate the parabola (you don't need to scale it).
___



[math] 



-------------------------------------------------------------------
[Resources]
_________
Scaling and Translating Quadratic Functions
https://www.futurelearn.com/courses/maths-linear-quadratic/0/steps/12114
We can get more general quadratic functions by scaling and translating the standard equation 𝑦=𝑥2 . Pleasantly, any quadratic function can be obtained in this way. …
_________

"""
#Your code should go here:

