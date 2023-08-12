"""
####  Simultaneous Linear Equations  ####

Given two simultaneous linear equations in this form: a*x + b*y = c, d*x + e*y = f, devise a function that returns the values of x and y as (x, y). The numbers a through f are non-zero integers. If there is not a unique solution or if there is no solution at all, return False. Input is given as: [[a, b, c], [d, e, f]]. Solutions, if they exist, will be integers.


[Examples]

___
sle([[3, 4, 19], [2, -1, 9]]) ➞ (5, 1)

sle([[3, 2, -2], [2, 5, -5]]) ➞ (0, -1)

sle([[4, -3, 18], [8, -6, 36]]) ➞ False

sle([[2, 3, 13], [5, -1, 7]]) ➞ (2, 3)
_____



[Notes]

Can you do this without using numpy?


[algebra] [math] 



-------------------------------------------------------------------
[Resources]
_________
Determinant
https://en.wikipedia.org/wiki/Determinant
In linear algebra, the determinant is a scalar value that can be computed from the elements of a square matrix and encodes certain properties of the linear transformati …
_________
_________
Determinant of a Matrix
https://www.mathsisfun.com/algebra/matrix-determinant.html
The determinant of a matrix is a special number that can be calculated from a square matrix.
_________
_________
Cramer's Rule
https://en.wikipedia.org/wiki/Cramer%27s_rule
In linear algebra, Cramer's rule is an explicit formula for the solution of a system of linear equations with as many equations as unknowns, valid whenever the system h …
_________

"""
#Your code should go here:

