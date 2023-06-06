"""
####  Geometric Mean  ####

The geometric mean of numbers a and b is the square root of their product (i.e. √(ab)). For example, the geometric mean of 2 and 8 is √(2*8)=4.
Two integers (a and b) are randomly (and independently) chosen between 1 and n (inclusive) where n is an integer greater than one. Create a function that takes a number n as an argument and returns the probability that the geometric mean of a and b is an integer.


[Examples]

___
f(2) ➞ 0.5
# There are four possible pairs: (1, 1), (2, 1), (1, 2) and (2, 2).
# The pairs (1, 1) and (2, 2) are wanted (√(1*1)=1 and √(2*2)=2)
# but the pairs (2, 1) and (1, 2) are not (√(2*1)=√2 and √(1*2)=√2).
# Thus, the probability is 2/4 = 0.5.

f(10) ➞ 0.18

f(100) ➞ 0.031
_____



[Notes]

Do not round your answer.


[geometry] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Geometric Mean
https://en.wikipedia.org/wiki/Geometric_mean
Is a mean or average, which indicates the central tendency or typical value of a set of numbers by using the product of their values (as opposed to the arithmetic mean …
_________
_________
Itertools.Product() Method
https://www.geeksforgeeks.org/python-itertools-product/
Is a library in Python which consists of multiple methods that are used in various iterators to compute a fast and code efficient solution. Here, the Product() method p …
_________

"""
#Your code should go here:

