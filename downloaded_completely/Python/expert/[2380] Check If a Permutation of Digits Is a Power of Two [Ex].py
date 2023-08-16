"""
####  Check If a Permutation of Digits Is a Power of Two  ####

The function is given an integer n. Find out if any permutation of digits of n such that the first digit is not 0 is equal to 2^k, return True / False.


[Examples]

___
check_power2(1) ➞ True
# 2^0 == 1

check_power2(13) ➞ False
# Neither 13 or 31 is a power of 2.

check_power2(61) ➞ True
# 2^4 == 16

check_power2(33) ➞ False
# 33 is not a power of 2.

check_power2(562) ➞ True
# 2^8 == 256

check_power2(921) ➞ False
# None of 921, 912, 291, 219, 192, 129 is a power of 2.
_____



[Notes]

The input number 0 < n < pow(2, 64) within the unsigned long long int range in C++.


[algorithms] [conditions] [logic] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
range() Type
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
Generate All Permutation of a Set
https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
Permutation is an arrangement of objects in a specific order. Order of arrangement of object is very important. The number of permutations on a set of n elements is giv …
_________
_________
math.log() Method
https://www.w3schools.com/python/ref_math_log.asp
Returns the natural logarithm of a number, or the logarithm of number to base.
_________

"""
#Your code should go here:

