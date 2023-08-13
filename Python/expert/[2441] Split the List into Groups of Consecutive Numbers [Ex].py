"""
####  Split the List into Groups of Consecutive Numbers  ####

The function is given two parameters: a list of integers and the group’s length. Determine if it is possible to split all numbers from the list into groups of the specified length such that there are consecutive numbers in each group, return True / False.


[Examples]

___
consecutive_nums([1, 3, 5], 1) ➞ True
# It is always possible to create groups of length 1.

consecutive_nums([5, 6, 3, 4], 2) ➞ True
# Two groups of length 2: [3, 4], [5, 6]

consecutive_nums([1, 3, 4, 5], 2) ➞ False
# It is possible to make one group of length 2, but not a second one.

consecutive_nums([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) ➞ True
# [1, 2, 3], [2, 3, 4], [6, 7, 8]

consecutive_nums([1, 2, 3, 4, 5], 4) ➞ False
# The list length is not divisible by the group’s length.
_____



[Notes]

N/A


[algorithms] [arrays] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Python While Loops
https://www.w3schools.com/python/python_while_loops.asp
With the while loop we can execute a set of statements as long as a condition is true.
_________

"""
#Your code should go here:

