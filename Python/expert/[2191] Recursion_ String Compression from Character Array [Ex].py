"""
####  Recursion: String Compression from Character Array  ####

The function is given an array of characters. Recursively compress the array into a string using the following rules. For each group of consecutively repeating characters:
___
*) If the number of repeating characters is one, append the string with only this character.
*) If the number n of repeating characters x is greater than one, append the string with "x" + str(n).
___



[Examples]

___
compress(["t", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "s", "s", "s", "h"]) ➞ "te14s3h"

compress(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"

compress(["a"]) ➞ "a"

compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) ➞ "ab12"

compress(["a", "a", "a", "b", "b", "a", "a"]) ➞ "a3b2a2"
_____



[Notes]

___
*) You are expected to solve this challenge using the concept of recursion.
*) Check out the Resources tab for more details on recursion.
*) An iterative version of this challenge (which was originally published by @Evgeny SH) can be found via this link.
___



[arrays] [recursion] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Defining Recursive Functions
https://www.youtube.com/watch?v=zbfRgC3kukk
In this lesson, you’ll learn that all recursive functions have two parts: the recursive case and the base case. You’ll also see how to define the factorial symbol recur …
_________
_________
Recursive Functions
https://www.python-course.eu/python3_recursive_functions.php
Recursion has something to do with infinity. I know recursion has something to do with infinity. I think I know recursion has something to do with infinity. He is sure …
_________

"""
#Your code should go here:

