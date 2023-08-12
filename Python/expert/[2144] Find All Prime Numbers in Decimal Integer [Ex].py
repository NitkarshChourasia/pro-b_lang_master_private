"""
####  Find All Prime Numbers in Decimal Integer  ####

Create a function that takes an integer argument and returns a list of prime numbers found in the decimal representation of that number (not factors).
For example, extract_primes(1717) returns [7, 7, 17, 17, 71].
The list should be in ascending order. If a prime number appears more than once, every occurrence should be listed. If no prime numbers are found, return an empty list.


[Examples]

___
extract_primes(1) ➞ []

extract_primes(7) ➞ [7]

extract_primes(73) ➞ [3, 7, 73]

extract_primes(103) ➞ [3]

extract_primes(1313) ➞ [3, 3, 13, 13, 31, 131, 313]
_____



[Notes]

___
*) All test cases are positive real integers.
*) Some numbers will have leading zeros. For example, the number 103 contains the prime number 3, but also contains 03. These should be treated as the same number, so the result would simply be [3].
___



[algorithms] [cryptography] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Primality Test
https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/a/comp-number-theory-introduction
A very interesting series about some of the different ways computers find prime numbers.
_________
_________
Python Program to Check Whether a Number Is Prime or Not
https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
Given a positive integer N. The task is to write a Python program to check if the number is prime or not.
_________

"""
#Your code should go here:

