"""
####  Recursion: Index Parity of Largest Even  ####

Finding an even integer in an list is kind of trivial and superficial to most programming enthusiasts. This challenge will take it to the next level.
Write a function that returns the largest even integer in a list with its corresponding index and the parity of that index, but determining the parity of that index is limited to not using the modulo operator %. Therefore, devise a way to resolve it.
Although these tasks are achievable with the use of some built-in Array functions, the purpose and intent of this challenge is for your to solve it recursively.


[Output Structure]

___
{"@odd|even index " + index_of_largest: largest_integer}
_____



[Examples]

___
bitwise_index([107, 19, 36, -18, -78, 24, 97]) ➞ {"@even index 2": 36}

bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]) ➞ {"@even index 6": 10}

bitwise_index([4, 4, 4, 4, 4, 4]) ➞ {"@even index 0": 4}

bitwise_index([-31, -7, -13, -7, -9, -13]) ➞ "No even integer found!"
_____



[Notes]

___
*) The use of the modulo operator %, index() and max() functions are restricted.
*) You can read more about recursion (see Resources tab) if you aren't familiar with it yet or haven't fully understood the concept before taking up this challenge.
___



[arrays] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Recursive Functions
https://www.python-course.eu/python3_recursive_functions.php
Recursion has something to do with infinity. I know recursion has something to do with infinity. I think I know recursion has something to do with infinity. He is sure …
_________
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Check Whether the Number Is Odd or Even Without Using Mod Operator
https://www.faceprep.in/c/check-whether-the-number-is-odd-or-even-without-using-mod-operator/
It is very simple to find if the given number is either odd or even without using the modulus operator. Even without using the modulus operator, a number can be checked …
_________

"""
#Your code should go here:

