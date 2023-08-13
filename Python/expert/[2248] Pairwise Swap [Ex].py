"""
####  Pairwise Swap  ####

Given a list of elements, swap the elements of the list pairwise. If the list is of odd length, first swap pairwise until the last element, and then the last element must be swapped with the element in the list which has the highest ASCII representation score in the modified list (e.g. ASCII representation of "Arun" would be: 65 + 114 + 117 + 110 = 406).
If two elements have the same ASCII representation, swap the last element of the odd length list with the element which is having the least index in the modified (the list in which pairwise swaps have been done until the second last element) list.
For example: if the list is [1, 2, 3, 4], we see it is having even length, so it becomes [2, 1, 4, 3].
If the list is [56, 123, 41, 321, 232] as it is an odd length list, first we swap it pairwise and the list becomes [123, 56, 321, 41, 232] and then 232 has the highest ASCII score, so we swap the last element with itself.


[Examples]

___
pairwise_swap[1, 2, 3, 4] ➞ [2, 1, 4, 3]

pairwise_swap[-8, "Arun", "Bob", 34.5, 12] ➞ [12, -8, 34.5, "Bob", "Arun"]

pairwise_swap[56, 123, 41, 321, 232] ➞ [123, 56, 321, 41, 232]

pairwise_swap["Nura", "Uam", "Ulgi", "Nurav", "Nayrus"] ➞ ["Uam", "Nura", "Nurav", "Ulgi", "Nayrus"]
_____



[Notes]

For -2, take ASCII representation as ascii_value_of(-) + ascii_value_of(2) and for 6.2 take ASCII representation as ascii_value_of(6) + ascii_value_of(.) + ascii_value_of(2).


[algorithms] [arrays] [data_structures] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
ord() Function
https://docs.python.org/3/library/functions.html#ord
Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. For example, ord('a') returns the integer 97 …
_________
_________
str() Function
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object. In this tutorial, we will learn about Python str() in detail with the help of examples.
_________
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________
_________
map() Function
https://www.programiz.com/python-programming/methods/built-in/map
Applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
_________
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it. In this tutorial, we will learn about Python zip() in detail with the help of examples.
_________

"""
#Your code should go here:

