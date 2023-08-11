"""
####  Combinator  ####

Create a function that, given a list of string lists, returns an list of all combinations as concatenated strings.

The function will accept an optional second string parameter. This parameter, if specified, is to be used to combine two strings.


[Examples]

___
combinator([["a", "b"], ["c", "d"]]) ➞ ["ac", "ad", "bc", "bd"]

combinator([["a"], ["a", "b"], "abc"]) ➞ ["aaa", "aab", "aac", "aba", "abb", "abc"]

combinator([["foo", "bar"], ["baz", "bamboo"]], " ") ➞ ["foo baz", "foo bamboo", "bar baz", "bar bamboo"]

combinator([[]]) ➞ []
_____



[Notes]

___
*) The order of the given strings must be retained in the combinations.
*) You can assume that:
The function is always called with a list of string lists and lists can be empty.
___



[algorithms] [arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Functions Creating Iterators for Efficient Looping
https://docs.python.org/3/library/itertools.html
This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
_________
_________
Itertools in Python 3
https://realpython.com/python-itertools/
Master Python's itertools module by constructing practical examples. We'll start out simple and then gradually increase in complexity, encouraging you to "think iterati …
_________
_________
Strings
https://www.w3schools.com/python/python_strings.asp
In python are surrounded by either single quotation marks, or double quotation marks. 'hello' is the same as "hello".
_________

"""
#Your code should go here:

