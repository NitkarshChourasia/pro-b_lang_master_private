"""
####  String Compression from Characters Array  ####

The function is given an array of characters. Compress the array into a string using the following rules. For each group of consecutively repeating characters:
___
*) If the number of repeating characters is one, append the string with only this character.
*) If the number n of repeating characters x is greater than one, append the string with "x" + str(n).
___



[Examples]

___
compress(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"

compress(["a"]) ➞ "a"

compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) ➞ "ab12"

compress(["a", "a", "a", "b", "b", "a", "a"]) ➞ "a3b2a2"
_____



[Notes]

N/A


[arrays] [control_flow] [language_fundamentals] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Functions Creating Iterators for Efficient Looping
https://docs.python.org/3/library/itertools.html
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
_________
_________
Count Consecutive Characters in Python User itertools.groupby
https://stackoverflow.com/questions/34443946/count-consecutive-characters
Counting consecutive characters made (relatively) easy using the groupby method of the itertools module in Python.
_________
_________
String join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string.
_________
_________
Python Conditions
https://www.w3schools.com/python/python_conditions.asp
In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that …
_________

"""
#Your code should go here:

