"""
####  Recursion: Isolated or Grouped?  ####

Write a function that extracts the max value of a number in a list. If there are two or more max values, return it as a list, otherwise, return the number. This process could be relatively easy with some of the built-in list functions but the required approach is recursive.


[Examples]

___
iso_group([31, 7, 2, 13, 7, 9, 10, 13]) ➞ 31

iso_group([1, 3, 9, 5, 1, 7, 9, -9]) ➞ [9, 9]

iso_group([97, 19, -18, 97, 36, 23, -97]) ➞ [97, 97]

iso_group([-31, -7, -13, -7, -9, -13]) ➞ [-7, -7]

iso_group([-1, -3, -9, -5, -1, -7, -9, -9]) ➞ [-1, -1]

iso_group([107, 19, -18, 79, 36, 23, 97]) ➞ 107
_____



[Notes]

You can read more about recursion (see the Resources tab) if you aren't familiar with it yet or haven't fully understood the concept before taking up this challenge.


[arrays] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Thinking Recursively in Python
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Recursive Functions in Python 3
https://www.python-course.eu/python3_recursive_functions.php
"The digital revolution is far more significant than the invention of writing or even of printing." (Douglas Engelbart)
_________
_________
Avoid Mutable Default Arguments
https://nikos7am.com/posts/mutable-default-arguments/
A very common error in Python is the use of an empty list as a default argument to a function. This is not the right way to do it and can cause unwanted behavior. See f …
_________

"""
#Your code should go here:

