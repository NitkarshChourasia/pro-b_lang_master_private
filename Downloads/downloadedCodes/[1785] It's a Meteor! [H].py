"""
####  It's a Meteor!  ####

In a video game, a meteor will fall toward the main character's home planet. Given the meteor's trajectory as a string in the form y = mx + b and the character's position as a tuple of (x, y), return True if the meteor will hit the character and False if it will not.


[Examples]

___
will_hit("y = 2x - 5", (0, 0)) ➞ False

will_hit("y = -4x + 6", (1, 2)) ➞ True

will_hit("y = 2x + 6", (3, 2)) ➞ False
_____



[Notes]

___
*) The b value will never be zero or blank.
*) The m value will always be an integer.
*) If the m value is 1, the "1" will be shown.
*) For example, "y = x + 5" will be shown as "y = 1x + 5".
*) If the m value is -1, the "-1" will be shown.
*) For example, "y = -x + 2" will be shown as "y = -1x + 2".
___



[algebra] [algorithms] [games] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to Check if a Point is on a Line If You Have an Equation?
https://virtualnerd.com/algebra-1/relations-functions/graphing-linear-equations/identifying-linear-equations/check-point-line-equation
Wondering if a point is part of the equation of a line? Got the equation of the line but no graph? No problem! Just take that point and plug it into the equation and si …
_________
_________
eval(): Evaluate Expressions Dynamically
https://realpython.com/python-eval-function/
In this step-by-step tutorial, you'll learn how Python's eval() works and how to use it effectively in your programs. Additionally, you'll learn how to minimize the sec …
_________

"""
#Your code should go here:

