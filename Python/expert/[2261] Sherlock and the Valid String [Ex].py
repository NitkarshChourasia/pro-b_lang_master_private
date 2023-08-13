"""
####  Sherlock and the Valid String  ####

Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just one character at one index in the string s, and the remaining characters will occur the same number of times.
Given a string, determine if it is valid. If so, return "YES", otherwise return "NO".
___
s= abc
# This is a valid string because frequencies are: {a: 1, b: 1, c: 1}

s = abcc
# This is a valid string because we can remove one c and have one
# of each character in the remaining string.

s = abccc
# This string is not valid as we can only remove one occurrence of c.
# That leaves character frequencies of: {a: 1, b: 1, c: 2}
_____



[Examples]

___
is_valid("aabbcd") ➞ "NO"

is_valid("aabbccddeefghi") ➞ "NO"

is_valid("abcdefghhgfedecba") ➞ "YES"
_____



[Notes]

N/A


[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python Counter in Collections
https://www.guru99.com/python-counter-collections-example.html
Python Counter is a container that will hold the count of each of the elements present in the container. The counter is a sub-class available inside the dictionary clas …
_________

"""
#Your code should go here:

