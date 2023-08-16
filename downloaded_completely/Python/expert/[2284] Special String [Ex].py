"""
####  Special String  ####

A string is said to be a "special" string if either of two conditions are met:
___
*) All of the characters are the same (e.g. "aaa").
*) All characters, except the middle one, are the (e.g. "aadaa").
___

A special substring is any substring of a string that meets one of those criteria. Given a string, determine how many special substrings can be formed from it.
Given the string s = "mnonopoo" we have the following special substrings:
___
{ "m", "n", "o", "n", "o", "p", "o", "o", "oo", "non", "ono", "opo" }
_____

You just have to return the total number of that special substrings. In this case, it is 12. Another example is s = "aaaa", so the substrings will be:
___
{ "a", "a", "a", "a", "aa", "aa", "aa", "aaa", "aaa", "aaaa" }
# The function will return 10
_____



[Examples]

___
special_string("mnonopoo") ➞ 12

special_string("asasd") ➞ 7

special_string("aaaa") ➞ 10
_____



[Notes]

N/A


[data_structures] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How do we use re.finditer() method in Python regular expression?
https://www.tutorialspoint.com/How-do-we-use-re-finditer-method-in-Python-regular-expression
How do we use re.finditer() method in Python regular expression? - According to Python docs,re.finditer(pattern, string, flags=0) Return an iterator yielding ...
_________
_________
Regular Expression Operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl. Both patterns and strings to be searched can be Unicode strings (str) as we …
_________

"""
#Your code should go here:

