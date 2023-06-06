"""
####  Recursion: Right Shift by Division  ####

The right shift operation is similar to floor division by powers of two, thus, the process is repetitive and can be done recursively.
Sample calculation using the right shift operator ( >> ):
___
80 >> 3 = floor(80/2^3) = floor(80/8) = 10
-24 >> 2 = floor(-24/2^2) = floor(-24/4) = -6
-5 >> 1 = floor(-5/2^1) = floor(-5/2) = -3
_____

Write a function that mimics (without the use of >>) the right shift operator and returns the result from the two given integers.


[Examples]

___
shift_to_right(80, 3) ➞ 10

shift_to_right(-24, 2) ➞ -6

shift_to_right(-5, 1) ➞ -3

shift_to_right(4666, 6) ➞ 72

shift_to_right(3777, 6) ➞ 59

shift_to_right(-512, 10) ➞ -1
_____



[Notes]

___
*) There will be no negative values for the second parameter y.
*) This challenge is more like recreating of the right shift operation, thus, the use of the operator directly is prohibited.
*) You are expected to solve this challenge via recursion.
*) An iterative version of this challenge can be found via this link.
___



[bit_operations] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Recursive Functions
https://www.python-course.eu/python3_recursive_functions.php
"Now, it's my belief that Python is a lot easier than to teach to students programming and teach them C or C++ or Java at the same time because all the details of the l …
_________
_________
Defining A Recursive Function
https://www.youtube.com/watch?v=zbfRgC3kukk
In this lesson, you’ll learn that all recursive functions have two parts: the recursive case and the base case. You’ll also see how to define the factorial s...
_________
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________

"""
#Your code should go here:

