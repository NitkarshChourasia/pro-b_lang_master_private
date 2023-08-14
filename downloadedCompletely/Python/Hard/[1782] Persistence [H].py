"""
####  Persistence  ####

The additive persistence of an integer, n, is the number of times you have to replace n with the sum of its digits until n becomes a single digit integer.
The multiplicative persistence of an integer, n, is the number of times you have to replace n with the product of its digits until n becomes a single digit integer.
Create two functions that take an integer as an argument and:



[Examples: Additive Persistence]

___
additive_persistence(1679583) ➞ 3
# 1 + 6 + 7 + 9 + 5 + 8 + 3 = 39
# 3 + 9 = 12
# 1 + 2 = 3
# It takes 3 iterations to reach a single-digit number.

additive_persistence(123456) ➞ 2
# 1 + 2 + 3 + 4 + 5 + 6 = 21
# 2 + 1 = 3

additive_persistence(6) ➞ 0
# Because 6 is already a single-digit integer.
_____



[Examples: Multiplicative Persistence]

___
multiplicative_persistence(77) ➞ 4
# 7 x 7 = 49
# 4 x 9 = 36
# 3 x 6 = 18
# 1 x 8 = 8
# It takes 4 iterations to reach a single-digit number.

multiplicative_persistence(123456) ➞ 2
# 1 x 2 x 3 x 4 x 5 x 6 = 720
# 7 x 2 x 0 = 0

multiplicative_persistence(4) ➞ 0
# Because 4 is already a single-digit integer.
_____



[Notes]

The input n is never negative.


[loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Additive and Multiplicative Persistence in Python
https://stackoverflow.com/questions/35590958/additive-and-multiplicative-persistence-in-python
I am having some trouble with my code. I have to find the additive and multiplicative persistence of a number. So far I can find the persistence just one time, but it h …
_________
_________
How to return the product of integers in an iterable?
https://stackoverflow.com/questions/595374/whats-the-function-like-sum-but-for-multiplication-product
Returns the sum of numbers in an iterable. sum([3,4,5]) == 3 + 4 + 5 == 12 I'm looking for the function that returns the product instead. somelib.somefunc([3,4,5]) == 3 …
_________

"""
#Your code should go here:

