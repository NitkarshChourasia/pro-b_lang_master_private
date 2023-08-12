"""
####  Recursion: License Plate  ####

Traveling through Europe one needs to pay attention to how the license plate in the given country is displayed. When crossing the border you need to park on the shoulder, unscrew the plate, re-group the characters according to the local regulations, attach it back and proceed with the journey.
Create a solution that can format the dmv number into a plate number with correct grouping. The function input consists of string s and group length n. The output has to be upper case characters and digits. The new groups are made from right to left and connected by -. The original order of the dmv number is preserved.


[Examples]

___
license_plate("5F3Z-2e-9-w", 4) ➞ "5F3Z-2E9W"

license_plate("2-5g-3-J", 2) ➞ "2-5G-3J"

license_plate("2-4A0r7-4k", 3) ➞ "24-A0R-74K"

license_plate("nlj-206-fv", 3) ➞ "NL-J20-6FV"
_____



[Notes]

___
*) You are expected to solve this challenge via a recursive approach.
*) An iterative version of this challenge can be found via this link.
___



[logic] [recursion] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Recursive Functions
https://www.python-course.eu/python3_recursive_functions.php
"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."
_________
_________
Defining a Recursive Function
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

