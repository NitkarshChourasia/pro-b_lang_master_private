"""
####  Recursion: Consecutive Number Series  ####

Write a function that will return True if a given string (divided and grouped into a size) will contain a set of consecutive numbers (regardless of orientation: whether ascending or descending), otherwise, return False.


[IMPORTANT]

The expected solution for this challenge is done recursively. Please check out the Resources tab for more details about recursion in Java.


[Examples]

___
is_consecutive("121314151617") ➞ True
# Contains a set of consecutive ascending numbers
# if grouped into 2's : 12, 13, 14, 15, 16, 17

is_consecutive("123124125") ➞ True
# Contains a set of consecutive ascending numbers
# if grouped into 3's : 123, 124, 125

is_consecutive("32332432536") ➞ False
# Regardless of the grouping size, the numbers can't be consecutive.

is_consecutive("326325324323") ➞ True
# Contains a set of consecutive descending numbers
# if grouped into 3's : 326, 325, 324, 323

is_consecutive("667666") ➞ True
# Consecutive descending numbers: 667 and 666.

is_consecutive("999897959493") ➞ False
_____



[Notes]

___
*) A number can consist of any number of digits, so long as the numbers are adjacent to each other, and the string has at least two of them.
*) An iterative version of this challenge can be found via this link.
___



[numbers] [recursion] [sorting] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
re.findall() Method
https://blog.finxter.com/python-re-findall/
This article is all about the findall() method of Python’s re library. The findall() method is the most basic way of using regular expressions in Python: If you want to …
_________
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Recursive Functions
https://www.python-course.eu/python3_recursive_functions.php
Recursion has something to do with infinity. I know recursion has something to do with infinity. I think I know recursion has something to do with infinity. He is sure …
_________
_________
Defining Recursive Functions
https://www.youtube.com/watch?v=zbfRgC3kukk
In this lesson, you’ll learn that all recursive functions have two parts: the recursive case and the base case. You’ll also see how to define the factorial s...
_________

"""
#Your code should go here:

