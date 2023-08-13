"""
####  Newton-Raphson method  ####

Create a function that finds a root of a polynomial curve. Do this using the Newton-Raphson method.
___
*) Your input will be a list of coefficients for a 3rd order polynomial: c(0)*x^3 + c(1)*x^2 + c(2)*x + c(3)
*) Round your answer to three decimal places (nearest 0.001). Choose x = 0.0 as an initial guess. Twenty iterations of the algorithm are sufficient for accuracy.
*) The Newton-Raphson method uses the generic derivative df/dx. This can be calculated analytically for a polynomial, or numerically using a small step of dx (such as 0.0001). See the Resources tab for more info.
___



[Examples]

___
newton_raphson([0.0, -0.1, -0.2, 0.3]) ➞ 1.000

newton_raphson([-0.1, 0.4, 0.1, -0.8]) ➞ 3.681

newton_raphson([0.2, -0.6, 1.5, -2.7]) ➞ 2.295
_____



[Notes]

N/A


[algorithms] [arrays] [math] 



-------------------------------------------------------------------
[Resources]
_________
numpy.poly1d
https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d
A convenience class, used to encapsulate “natural” operations on polynomials so that said operations may take on their customary form in code (see Examples).
_________
_________
Newton-Raphson Method
https://brilliant.org/wiki/newton-raphson-method/
Is a way to quickly find a good approximation for the root of a real-valued function f(x)=0f(x) = 0f(x)=0. It uses the idea that a continuous and differentiable functio …
_________
_________
Newton-Raphson Method
https://www.shodor.org/unchem/math/newton/
If you've ever tried to find a root of a complicated function algebraically, you may have had some difficulty. Using some basic concepts of calculus, we have ways of nu …
_________

"""
#Your code should go here:

