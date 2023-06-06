"""
####  New Numbers  ####

A new number is a number that is not a permutation of any smaller number. 869 is not a new number because it is just a permutation of smaller numbers, 689 and 698. 509 is a new number because it can't be formed by a permutation of any smaller number (leading zeros not allowed).
Write a function that takes a non-negative integer and returns True if the integer is a new number and False if it is not.


[Examples]

___
is_new(3) ➞ True

is_new(30) ➞ True

is_new(321) ➞ False

is_new(123) ➞ True
_____



[Notes]

A curious fact: out of the first one million integers, only 8002 are new.


[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to generate all permutations of a list?
https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list
Starting with Python 2.6 (and if you're on Python 3) you have a standard-library tool for this: itertools.permutations. import itertools list(itertools.permutations([1 …
_________

"""
#Your code should go here:

