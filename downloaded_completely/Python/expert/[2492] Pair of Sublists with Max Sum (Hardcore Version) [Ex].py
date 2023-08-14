"""
####  Pair of Sublists with Max Sum (Hardcore Version)  ####

This challenge is a harder version of a previous challenge (which you should solve first), solving the same problem, but with much harder tests which require the solution to be pretty efficient (see Notes below).
The problem in question is the max sum sublist pair problem which, given a list of numbers, tries to find the pair of sublists with the maximum possible combined sum.
For example:
___
[1, 6, -1, -5, -2, 5, -1, 4, -7, 1, 2, 3]
_____

The max sum sublist pair is [1, 6], [5, -1, 4] which has combined sum 1 + 6 + 5 - 1 + 4 = 15.
Notably, in this challenge, we allow for empty sublists [], whose sum is 0. Thus, for the list:
___
[-1, -2, -3, 5, 4, 3, 4, 5, -9, -10]
_____

The max sum sublist pair is [5, 4, 3, 4, 5], [] with total sum 5 + 4 + 3 + 4 + 5 = 21.


[Goal]

Write an efficient function which, given a list of numbers, returns the total sum of the max sum sublist pair.


[Examples]

___
[1, 6, -1, -5, -2, 5, -1, 4, -7, 1, 2, 3] ➞ 15
# Max sum sublist pair is [1, 6], [5, -1, 4]

[-1, -2, -3, 5, 4, 3, 4, 5, -9, -10] ➞ 21
# Max sum sublist pair is [5, 4, 3, 4, 5], []

[-4, 2, -3, -2, 2, -3, 5, -2] ➞ 7
# Max sum sublist pair is [2], [5]

[0, -1, 5, -6, 5, -3, 0, -4, 5, 2, -5, 1] ➞ 12
# Max sum sublist pair is [5], [5, 2]

[-5, 3, -4, 6, 0, 0, -4, -2, -2, 7, -5, 7, -5, 5] ➞ 15
# Max sum sublist pair is [6], [7, -5, 7]
_____



[Notes]

___
*) The max sum sublist pair problem is a variant of the classic max sum sublist problem (see this challenge), which can be solved efficiently via Kadane's algorithm (see the Resources tab), which runs in linear O(n) time (where n is the length of the list).
*) As with Kadane's algorithm, your solution to this challenge will almost certainly need to run in linear O(n) time to pass all the tests. For reference, my linear time code runs in about 0.3s. As such, linear time solutions should easily pass the tests within the 12s time limit, but slower solutions should fail.
___



[algorithms] [arrays] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Kadane's algorithm
https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
A description of Kadane's algorithm for solving the max sum sublist problem.
_________

"""
#Your code should go here:

