"""
####  Sexy Primes  ####

Sexy primes are primes that differ by 6.
For example, (5, 11) comprise a sexy prime pair, while (5, 11, 17) comprise a set of sexy prime triplets.
Create a function that takes two numbers as argument, the set length n (2 for pairs, 3 for triplets), and the limit. Return a list of sorted tuples of sexy primes up to (but excluding) the limit.


[Examples]

___
sexy_primes(2, 100) ➞ [(5, 11), (7, 13), (11, 17), (13, 19), (17, 23), (23, 29), (31, 37), (37, 43), (41, 47), (47, 53), (53, 59), (61, 67), (67, 73), (73, 79), (83, 89)]

sexy_primes(3, 100) ➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79)]

sexy_primes(3, 250) ➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79), (97, 103, 109), (101, 107, 113), (151, 157, 163), (167, 173, 179), (227, 233, 239)]
_____



[Notes]

N/A


[algebra] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Sexy Prime Triplets
https://prime-numbers.info/article/sexy-prime-triplets
Sexy prime triplets are a set of three prime numbers of the form {p, p + 6, p + 12}.
_________
_________
Convert a List Into a Tuple
https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/
Given a list, write a Python program to convert the given list into a tuple.
_________

"""
#Your code should go here:

