"""
####  Finitely Expressible Rational Numbers in a Number Base  ####

A number is finitely expressible if you can write it in floating point form and only use a finite number of digits.
___
*) 1/3 is not finitely expressible in base 10 as it requires an infinite number of digits to write out: 0.333333 ...
*) 3/2 is finitely expressible in base 10 as it requires only two digits: 1.5
___

Create a function that takes in a rational number in the form of a tuple and a number base as arguments and returns true if the rational is finitely expressible in the number base and false if not.
___
isFinitelyExpressible((numerator, denominator), number_base)
_____



[Examples]

___
isFinitelyExpressible((1, 3), 10) ➞ False
# 0.3333...

isFinitelyExpressible((4, 1), 10) ➞ True
# 4

isFinitelyExpressible((4, 7), 2)  ➞ False
# 0.1001001...
_____



[Notes]

___
*) The rational numbers given to you will be in lowest terms.
*) Python doesn't have infinite floating point precision so writing out a number in a base won't work and the bases in the tests will be quite large.
___



[algorithms] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Euclid's Greatest Common Divisor Algorithm
https://en.wikipedia.org/wiki/Euclidean_algorithm
Provides the greatest common divisor for two numbers.
_________

"""
#Your code should go here:

