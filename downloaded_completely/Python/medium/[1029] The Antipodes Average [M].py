"""
####  The Antipodes Average  ####

In this challenge, you are given a list and in turn, you must obtain a smaller list, following three steps:
___
*) Split the list into two parts of equal length. If the given list has an odd length, then you have to eliminate the number in the middle of the list for obtaining two equal parts.
*) Sum each number of the first part with each number of the reversed second part, obtaining a new single list having the same length of the previous two.
*) Divide by two each number in the final list.
___

Given a list of integers lst, implement a function that returns a new list applying the above algorithm.


[Examples]

___
antipodes_average([1, 2, 3, 4]) ➞ [2.5, 2.5]
# Left part = [1, 2]
# Reversed right part = [4, 3]
# List resulting from the sum of each pair = [5, 5]
# Each number is divided by two = [2.5, 2.5]

antipodes_average([1, 2, 3, 4, 5]) ➞ [3, 3]
# The length of list is odd, number 3 (in the middle) is eliminated
# Left = [1, 2]
# Reversed right = [5, 4]
# Sum = [6, 6]
# Division by two = [3, 3]

antipodes_average([-1, -2]) ➞ [-1.5]
#  (-1 + -2) / 2 = [-1.5]
_____



[Notes]

___
*) Every given lst will contain at least two numbers.
*) Into the given lst, numbers will always be whole (either positives or negatives), but the numbers into the returned final list can also be a float (either positives or negatives, see the examples #1 and #3).
*) You can do three separated steps, or thinking about how the algorithm can be synthesized for obtaining the result.
___



[algorithms] [arrays] [math] 



-------------------------------------------------------------------
[Resources]
_________
Ceil and floor equivalent in Python without Math module?
https://stackoverflow.com/questions/32558805/ceil-and-floor-equivalent-in-python-3-without-math-module
TLDR: You can use x // y instead of math.floor(x / y) and -(-x // y) instead of math.ceil(x / y).
_________
_________
zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
Learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables in parallel and create dictionaries wit …
_________

"""
#Your code should go here:

