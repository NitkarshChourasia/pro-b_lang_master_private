"""
####  Recursion: N-Length Letter Groups  ####

Write a function that returns an array of strings populated from the slices of n-length characters of the given word (a slice after another while n-length applies onto the word).


[Examples]

___
collect("intercontinentalisationalism", 6)
➞ ["ationa", "interc", "ntalis", "ontine"]

collect("strengths", 3)
➞ ["eng", "str", "ths"]

collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15)
➞ ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]
_____



[Notes]

___
*) Ensure that the resulting array is lexicographically ordered.
*) Return an empty array if the given string is less than n.
*) You are expected to solve this challenge via a recursive approach.
*) You can check on the Resources tab for more details about recursion.
*) An iterative version of this challenge can be found via this link.
___



[arrays] [recursion] [sorting] [strings] 



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
"At least for the people who send me mail about a new language that they're designing, the general advice is: do it to learn about how to write a compiler. " (Dennis Ri …
_________
_________
Defining A Recursive Function
https://www.youtube.com/watch?v=zbfRgC3kukk
In this lesson, you’ll learn that all recursive functions have two parts: the recursive case and the base case. You’ll also see how to define the factorial s...
_________

"""
#Your code should go here:

