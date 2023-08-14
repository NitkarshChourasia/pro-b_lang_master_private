"""
####  ABA Integers: the Undulating Numbers  ####

In this challenge, you have to establish if a given number is undulating. A number n is undulating when the following conditions are all true:
___
*) n has at least three digits.
*) n has exactly two different digits.
*) The two digits of n are alternating without repeating groups.
___

If we think of the first digit of an undulating number as an "A", and the second digit as a "B", we notice a sequence of the form "ABA" that can repeat infinite times and ends either with an "A" or with a "B", but without clusters of "AA" or "BB" in it.
Given a positive integer n, implement a function that returns True if n is an Undulating number, or False if it's not.


[Examples]

___
is_undulating(121) ➞ True
# A = 1, B = 2
# The sequence ABA is valid

is_undulating(373737) ➞ True
# A = 3, B = 7
# The sequence ABABABAB is valid

is_undulating(12) ➞ False
# Less than three digits

is_undulating(12122) ➞ False
# The sequence ABABB is not valid

is_undulating(85856) ➞ False
# More than two different digits
_____



[Notes]

N/A


[conditions] [numbers] [regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Undulating Number
https://en.wikipedia.org/wiki/Undulating_number
A number that has the digit form ABABAB... when in the base 10 number system. It is sometimes restricted to non-trivial undulating numbers which are required to have at …
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________
_________
Undulating Number — from Wolfram MathWorld
http://mathworld.wolfram.com/UndulatingNumber.html
A number of the form aba..., abab..., etc. The first few nontrivial undulants (with the stipulation that a!=b) are 101, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212 …
_________

"""
#Your code should go here:

