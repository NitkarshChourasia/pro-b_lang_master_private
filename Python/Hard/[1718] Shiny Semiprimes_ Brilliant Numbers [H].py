"""
####  Shiny Semiprimes: Brilliant Numbers  ####

In this challenge, you have to establish if a given number is Brilliant. A Brilliant number is a semiprime that can be obtained only by multiplicating two, and only two, different primes with the same number of digits.
A semiprime can be:
___
*) A composite number equal to the product of two different primes.
*) A composite number equal to the square of a prime.
___

Given an integer n, implement a function that returns True if n is a Brilliant number, or False if it's not.


[Examples]

___
is_brilliant(11) ➞ False
# 11 is a prime.

is_brilliant(9) ➞ True
# 9 is equal to the square of a prime: 3²

is_brilliant(21) ➞ True
# 21 is equal to the product of two different primes: 3 x 7
# 3 and 7 have the same digital length.

is_brilliant(22) ➞ False
# 22 is equal to the product of two different primes: 2 x 11
# 2 and 11 have different digital lengths.
_____



[Notes]

___
*) The given n will be a positive integer greater than 0.
*) Remember that a Brilliant number is a semiprime that can be obtained only with a single combination of different primes having the same digital length.
___



[higher_order_functions] [loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
gmpy2
https://pypi.org/project/gmpy2/
Is an optimized, C-coded Python extension module that supports fast multiple-precision arithmetic. gmpy2 is based on the original gmpy module. gmpy2 adds support for co …
_________
_________
is_prime, next prime
https://python.hotexamples.com/examples/gmpy2/-/is_prime/python-is_prime-function-examples.html
These are the top rated real world Python examples of gmpy2extracted from open source projects. You can rate examples to help us improve the quality of examples.
_________

"""
#Your code should go here:

