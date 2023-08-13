"""
####  Recursion: Flatten the Curves  ####

The nesting of lists can be viewed indirectly as curves and barriers of the real data embedded in lists, thus, defeats the very purpose of directly accessing them thru indexes and slices. In this challenge, a function is required to flatten those curves (i.e. level, iron, compress, raze, topple) and expose those data as a single list and not as a list of lists.


[Examples]

___
flatten([[[[[["direction"], [372], ["one"], [[[[[["Era"]]]], "Sruth", 3337]]], "First"]]]])
➞ ["direction", 372, "one", "Era", "Sruth", 3337, "First"]

flatten([[4666], [5394], [466], [[["Saskia", [[[[["DXTD"]], "Lexi"]]]]]]])
➞ [4666, 5394, 466, "Saskia", "DXTD", "Lexi"]

flatten([[696], ["friend"], ["power"], [[[["Marcus"]]]], ["philus"]])
➞ [696, "friend", "power", "Marcus", "philus"]

flatten([[["deep"], [[["ocean"]]], [["Marge"]], ["rase", 876]]])
➞ ["deep", "ocean", "Marge", "rase", 876]
_____



[Notes]

___
*) There are no empty lists to handle.
*) You're expected to solve this challenge using a recursive approach.
*) You can read on more topics about recursion (see Resources tab) if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge.
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
Recursion is a method of programming or coding a problem, in which a function calls itself one or more times in its body. Usually, it is returning the return value of t …
_________
_________
Defining a Recursive Function
https://www.youtube.com/watch?v=zbfRgC3kukk
Recursive functions have two parts: the recursive case and the base case. You’ll also see how to define the factorial s...
_________

"""
#Your code should go here:

