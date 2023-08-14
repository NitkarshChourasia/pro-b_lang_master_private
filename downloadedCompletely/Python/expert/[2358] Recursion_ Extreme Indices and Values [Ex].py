"""
####  Recursion: Extreme Indices and Values  ####

Write a function that extracts the upper and lower bounds of the elements in the list, value-wise, including its corresponding index, list-wise. Although these tasks are achievable with the use of some built-in Array functions, the purpose and intent of this challenge is for your to solve it recursively.
Output Structure:
___
[{index: lower_bound}, {index: upper_bound}]
_____



[Examples]

___
extremes([107, 19, -18, -79, 36, 23, 97]) ➞ [{3: -79}, {0: 107}]

extremes([31, 7, 2, 13, 7, 9, 10, 13]) ➞ [{2: 2}, {0: 31}]

extremes([4, 4, 4, 4, 4, 4]) ➞ "No bounds!"
_____



[Notes]

___
*) Return "No bounds!" if the lower bound happens to be equal to its supposed upper bound (because logically and numerically, lower and upper bound values cannot be equal, thus, their respective names (see above example).
*) The use of index(), max() and min() are restricted.
*) You can read more about recursion (see Resources tab) if you aren't familiar with it yet or haven't fully understood the concept before taking up this challenge.
___



[arrays] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Recursive Functions in Python 3
https://www.python-course.eu/python3_recursive_functions.php
Recursion is a method of programming or coding a problem, in which a function calls itself one or more times in its body. Usually, it is returning the return value of t …
_________
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________

"""
#Your code should go here:

