"""
####  Split the String into Substrings with Non-overlapping Characters  ####

The function is given a string with lower-case characters. Split the string into as many substrings as possible such that each character appears in only one substring. Return the list of lengths of the resulting substrings.


[Examples]

___
split_string("abbccc"), [1, 2, 3]
# "a", "bb", "ccc"

split_string("abbacdceef"), [4, 3, 2, 1]
# "abba", "cdc", "ee", "f"

split_string("abacded"), [3, 1, 3]
# "aba", "c", "ded"

split_string("abcdea"), [6]
# "abcdea" because first letter is equal to the last letter.
_____



[Notes]

Xavier would deeply appreciate if you solve this challenge with recursion using greedy approach.


[algorithms] [conditions] [recursion] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Recursive Functions
https://www.python-course.eu/python3_recursive_functions.php
Recursion is a method of programming or coding a problem, in which a function calls itself one or more times in its body. Usually, it is returning the return value of t …
_________
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in our Python programs by mastering concepts such as recursive functions and recursive data structures. We’ll also talk about maintaini …
_________
_________
Defining a Recursive Function
https://www.youtube.com/watch?v=zbfRgC3kukk
Learn that all recursive functions have two parts: the recursive case and the base case. You’ll also see how to define the factorial symbol recursively.
_________

"""
#Your code should go here:

