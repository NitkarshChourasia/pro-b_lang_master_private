"""
####  Sticky Keys Typing  ####

Someone is typing on the sticky keyboard. Occasionally a key gets stuck and more than intended number of characters of a particular letter is being added into the string. The function input contains original and typed strings. Determine if the typed string has been made from the original. Return True if it is and False if the typed string cannot have been made from the original.


[Examples]

___
is_long_pressed("alex", "aaleex") ➞ True

is_long_pressed("saeed", "ssaaedd") ➞ False

is_long_pressed("leelee", "lleeelee") ➞ True

is_long_pressed("Tokyo", "TTokkyoh") ➞ False

is_long_pressed("laiden", "laiden") ➞ True
_____



[Notes]

N/A


[conditions] [logic] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
itertools.groupby()
https://www.geeksforgeeks.org/itertools-groupby-in-python/
Python’s Itertool is a module that provides various functions that work on iterators to produce complex iterators. This module works as a fast, memory-efficient tool th …
_________
_________
Regular Expression Operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________

"""
#Your code should go here:

