"""
####  Economical Numbers  ####

A number is Economical if the quantity of digits of its prime factorization (including exponents greater than 1) is equal to or lower than the digit quantity of the number itself.
Given an integer n, implement a function that returns a string:
___
*) "Equidigital" if the quantity of digits of the prime factorization (including exponents greater than 1) is equal to the quantity of digits of n;
*) "Frugal" if the quantity of digits of the prime factorization (including exponents greater than 1) is lower than the quantity of digits of n;
*) "Wasteful" if none of the two above conditions is true.
___



[Examples]

___
is_economical(14) ➞ "Equidigital"
# The prime factorization of 14 (2 digits) is [2, 7] (2 digits)
# Exponents equal to 1 are not counted

is_economical(125) ➞ "Frugal"
# The prime factorization of 125 (3 digits) is [5^3] (2 digits)
# Notice how exponents greater than 1 are counted

is_economical(1024) ➞ "Frugal"
# The prime factorization of 1024 (4 digits) is [2^10] (3 digits)

is_economical(30) ➞ "Wasteful"
# The prime factorization of 30 (2 digits) is [2, 3, 5] (3 digits)
_____



[Notes]

___
*) Any given n will be a positive integer greater than 1.
*) Remember to count also the exponents greater than 1 into the prime factorization: 2¹ = 2 (one digit), 2² = 22 (two digits), 2¹° = 210 (three digits)...
___



[conditions] [loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Prime Factorization
https://www.mathsisfun.com/prime-factorization.html
A Prime Number is a whole number greater than 1 that can not be made by multiplying other whole numbers. The first few prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19 and …
_________
_________
Prime Factorization ⁠— from Wolfram MathWorld
http://mathworld.wolfram.com/PrimeFactorization.html
The factorization of a number into its constituent primes, also called prime decomposition.
_________
_________
Prime Factorization
https://www.pythonpool.com/prime-factorization-python/
How to find Prime Factors of a number in Python.
_________

"""
#Your code should go here:

