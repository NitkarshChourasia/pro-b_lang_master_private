"""
####  Sum of Two Square Numbers  ####

The function is given a non-negative integer n. Determine if there exist two non-negative integers a and b such that a**2 + b**2 == n, return True / False.


[Examples]

___
squares_sum(0) ➞ True
# 0^2 + 0^2 == 0

squares_sum(1) ➞ True
# 0^2 + 1^2 == 1

squares_sum(2) ➞ True
# 1^2 + 1^2 == 2

squares_sum(3) ➞ False
# Checking 0, 1 we can’t make the sum of squares equal to 3.

squares_sum(5) ➞ True
# 1^2 + 2^2 == 5
_____



[Notes]

The input range is 0 <= n < 2**31.


[algorithms] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Sum of Two Squares Theorem
https://en.wikipedia.org/wiki/Sum_of_two_squares_theorem
Relates the prime decomposition of any integer n > 1 to whether it can be written as a sum of two squares, such that n = a2 + b2 for some integers a, b. An integer gre …
_________
_________
How to determine whether a number can be written as a sum of two squares?
https://math.stackexchange.com/questions/787321/how-to-determine-whether-a-number-can-be-written-as-a-sum-of-two-squares
A postive integer n is representable as the sum of two squares, n=x2+y2 if and only if every prime divisor p≡3 mod 4 of n occurs with even exponent. This is good enough …
_________

"""
#Your code should go here:

