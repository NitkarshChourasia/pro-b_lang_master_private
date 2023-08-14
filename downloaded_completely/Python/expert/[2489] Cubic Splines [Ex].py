"""
####  Cubic Splines  ####

Cubic splines are used to smoothly connect the dots. Write implementation of the class Curve that:
___
*) Accepts a list or set of tuples (x, y).
*) Builds n-1 splines for n unique knots.
*) Computes y for given x.
*) Finds min and max of the curve.
*) Supports knot addition and removal.
*) Supports overloaded operators +, -.
___

More detailed description of the class with names of methods is in the docstrings in the Code window.


[Examples]

For the given 6 lists of knots in Tests, the following curves are constructed:



[Notes]

___
*) In practical usage of the splines x is inside the knots range, but in this challenge x can be anywhere to compute y.
*) The minimum or maximum can lie either on a knot or somewhere inside if a spline bends. The search range is restricted to the range of knots; outside the curve goes to infinity.
*) The algorithm for building splines is pretty straightforward and well explained in the wiki page: Spline (mathematics).
___



[classes] [control_flow] [loops] [math] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

