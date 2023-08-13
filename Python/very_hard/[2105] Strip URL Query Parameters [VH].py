"""
####  Strip URL Query Parameters  ####

Create a function that takes a URL (string), removes duplicate query parameters and parameters specified within the 2nd argument (which will be an optional list).


[Examples]

___
strip_url_params("https://edabit.com?a=1&b=2&a=2") ➞ "https://edabit.com?a=2&b=2"

strip_url_params("https://edabit.com?a=1&b=2&a=2", ["b"]) ➞ "https://edabit.com?a=2"

strip_url_params("https://edabit.com", ["b"]) ➞ "https://edabit.com"
_____



[Notes]

___
*) The 2nd argument params_to_strip is optional.
*) params_to_strip can contain multiple params.
*) If there are duplicate query parameters with different values, use the value of the last occurring parameter (see examples #1 and #2 above).
___



[algorithms] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.programiz.com/python-programming/methods/string/split
Breaks up a string at the specified separator and returns a list of strings.
_________
_________
join() string Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
RegEx Tester and Debugger
https://regex101.com
With highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Data Structures
https://docs.python.org/3/tutorial/datastructures.html
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.in …
_________
_________
urllib.parse — Parse URLs into components
https://docs.python.org/3/library/urllib.parse.html
This module defines a standard interface to break Uniform Resource Locator (URL) strings up in components (addressing scheme, network location, path etc.), to combine t …
_________

"""
#Your code should go here:

