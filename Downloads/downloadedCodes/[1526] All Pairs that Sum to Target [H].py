"""
####  All Pairs that Sum to Target  ####

Create a function that returns all pairs of numbers in a list that sum to a target. Sort the pairs in ascending order with respect to the smaller number, then order each pair in this order: [smaller, larger].


[Examples]

___
all_pairs([2, 4, 5, 3], 7) ➞ [[2, 5], [3, 4]]
# 2 + 5 = 7, 3 + 4 = 7

all_pairs([5, 3, 9, 2, 1], 3) ➞ [[1, 2]]

all_pairs([4, 5, 1, 3, 6, 8], 9) ➞ [[1, 8], [3, 6], [4, 5]]
# Sorted: 1 < 3 < 4; each pair is ordered [smaller, larger]
_____



[Notes]

___
*) If no pairs are found, return an empty list [].
*) You are only allowed to use each number once in a pair.
*) See Comments for a hint.
___



[algorithms] [arrays] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
The Popular Two-Sum Coding Problem
https://coderbyte.com/algorithm/two-sum-problem
The two sum problem is a common interview question, and it is a variation of the subset sum problem. There is a popular dynamic programming solution for the subset sum …
_________
_________
itertools.combinations() module to print all possible combinations
https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/
Given an array of size n, generate and print all possible combinations of r elements in array. This problem has existing recursive solution please refer Print all possi …
_________

"""
#Your code should go here:

