"""
####  Alpha-Range  ####

As you know, the function range() returns a range of numbers, but it doesn't work on alphabets. In this challenge, we try to fill this gap.
Write a function alpha-range() which takes three arguments start, stop, and step (which its default value is one). The function must return a list of alphabetical characters, ranging from start character to stop character based on step value.
The function must follow these conditions:
___
*) If step is zero or more than 26 or less than -26, return "step must be a non-zero value between -26 and 26, exclusive".
*) Both start and stop must share the same case, otherwise, return "both start and stop must share the same case".
___

Like range() function:
___
*) step must not be zero.
___

Unlike range() function:
___
*) returned list must be inclusive.
*) the order of characters doesn't affect the output (i.e. the output of alpha_range("a", "f") is the same as alpha_range("f", "a"), see examples).
___



[Examples]

___
alpha_range("a", "f") ➞ ["a", "b", "c", "d", "e", "f"]

alpha_range("f", "a") ➞ ["a", "b", "c", "d", "e", "f"]

alpha_range("a", "f", -1) ➞ ["f", "e", "d", "c", "b", "a"]

alpha_range("f", "a", -1) ➞ ["f", "e", "d", "c", "b", "a"]

alpha_range("A", "F", -1) ➞ ["F", "E", "D", "C", "B", "A"]

alpha_range("A", "F", 0) ➞ "step must be a non-zero value between -26 and 26, exclusive"

alpha_range("A", "F", -26) ➞ "step must be a non-zero value between -26 and 26, exclusive"

alpha_range("a", "F", -1) ➞ "both start and stop must share the same case"
_____



[Notes]

All the start and stop values in the tests are valid alphabetical characters.


[arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
chr() and ord()
https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods#:~:text=of%20Data%20columns-,Python%20chr()%20and%20ord(),how%20they%20can%20be%20used.
In this lesson, we'll work with the python chr() and ord() functions. Python’s built-in function chr() is used for converting an Integer to a Character, while the funct …
_________
_________
Map vs List Comprehension
https://www.geeksforgeeks.org/python-map-vs-list-comprehension/
Suppose we have a function and we want to compute this function for different values in a single line of code . This is where map() function plays its role ! map() func …
_________
_________
Python range()
https://www.programiz.com/python-programming/methods/built-in/range
The range() type returns an immutable sequence of numbers between the given start integer to the stop integer.
_________

"""
#Your code should go here:

