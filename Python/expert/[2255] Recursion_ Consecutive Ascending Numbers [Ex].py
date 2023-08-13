"""
####  Recursion: Consecutive Ascending Numbers  ####

Write a function that will return True if a given string (divided and grouped into a size) will contain a set of consecutive ascending numbers, otherwise, return False.


[IMPORTANT]

The expected solution for this challenge is done recursively. Please check out the Resources tab for more details about recursion if it needs be.


[Examples]

___
is_ascending("123124125") ➞ True
# Contains a set of consecutive ascending numbers
# if grouped into 3's : 123, 124, 125

is_ascending("101112131415") ➞ True
# Contains a set of consecutive ascending numbers
# if grouped into 2's : 10, 11, 12, 13, 14, 15

is_ascending("32332432536") ➞ False
# Regardless of the grouping size, the numbers can't be consecutive.

is_ascending("326325324323") ➞ False
# Though the numbers (if grouped into 3's) are consecutive but descending.

is_ascending("666667") ➞ True
# Consecutive numbers: 666 and 667.
_____



[Notes]

___
*) A number can consist of any number of digits, so long as the numbers are adjacent to each other, and the string has at least two of them.
*) An iterative version of this challenge can be found via this link.
___



[arrays] [numbers] [recursion] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Recursive Functions
https://www.python-course.eu/python3_recursive_functions.php
"Much of my work has come from being lazy. I didn't like writing programs, and so, when I was working on the IBM 701, writing programs for computing missile trajectorie …
_________
_________
Defining Recursive Functions
https://www.youtube.com/watch?v=zbfRgC3kukk
In this lesson, you’ll learn that all recursive functions have two parts: the recursive case and the base case. You’ll also see how to define the factorial s...
_________

"""
#Your code should go here:

