"""
####  Anti-Divisors of a Number  ####

The anti-divisors are numbers that do not divide a given number by the largest possible margin, and they can be found following a simple set of rules:
___
*) Every number greater than 1 and lower than n is checked.
*) Every checked number must not be a divisor of n.
*) If the checked number is odd and it is a divisor of n * 2 - 1 or n * 2 + 1 it's an anti-divisor.
*) If the checked number is even and it is a divisor of n * 2, it's an anti-divisor.
___

Given an integer n, implement a function that returns a list containing the anti-divisors of n sorted in ascending order.


[Examples]

___
anti_divisors(10) ➞ [3, 4, 7]
# 3 is a divisor of 21 (10 * 2 + 1)
# 4 is a divisor of 20 (10 * 2)
# 7 is a divisor of 21

anti_divisors(12) ➞ [5, 8]
# 5 is a divisor of 25 (12 * 2 + 1)
# 8 is a divisor of 24 (12 * 2)

anti_divisors(20) ➞ [3, 8, 13]
# 3 is a divisor of 39 (20 * 2 - 1)
# 8 is a divisor of 40 (20 * 2)
# 13 is a divisor of 39
_____



[Notes]

The given n can be any integer, either positive, negative or 0.


[algorithms] [conditions] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
The Anti-Divisor
https://oeis.org/A066272/a066272a.html
The anti-divisor, or unbiased non-divisor, is a concept related very closely to the concept of prime numbers, and the concept of a divisor. Every integer is either prim …
_________

"""
#Your code should go here:

