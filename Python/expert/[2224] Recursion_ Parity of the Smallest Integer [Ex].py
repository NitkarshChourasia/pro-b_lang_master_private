"""
####  Recursion: Parity of the Smallest Integer  ####

Write a function that returns the smallest integer in a list with its corresponding index and its parity. Although these tasks can be equivocally achievable with the use of some built-in and list functions, the purpose and intent of this challenge is for you to solve it recursively.
Output Structure:
___
{"@index " + index_of_smallest: smallest_integer, "parity": "odd|even"}
_____



[Examples]

___
bitwise_one_zero([107, 19, -18, -79, 36, 23, 97]) ➞ {"@index 3": -79, "parity": "odd"}

bitwise_one_zero([31, 7, 2, 13, 7, 9, 10, 13]) ➞ {"@index 2": 2, "parity": "even"}

bitwise_one_zero([3, 3, 3, 3, 3, 3]) ➞ {"@index 0": 3, "parity": "odd"}
_____



[Notes]

___
*) The use of index() and min() are restricted.
*) You can read more about recursion (see Resources tab) if you aren't familiar with it or haven't fully understood the concept before taking up this challenge.
___



[arrays] [recursion] 



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
Is a method of programming or coding a problem, in which a function calls itself one or more times in its body. Usually, it is returning the return value of this functi …
_________

"""
#Your code should go here:

