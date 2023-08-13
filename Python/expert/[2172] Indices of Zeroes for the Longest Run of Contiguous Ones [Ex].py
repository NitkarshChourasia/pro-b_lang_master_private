"""
####  Indices of Zeroes for the Longest Run of Contiguous Ones  ####

You are given a list of binary integers and k, the number of flips allowed.
Write a function that returns the indices of zeroes of which, when flipped, return the longest contiguous sequence of ones.


[Examples]

___
zero_indices([1, 0, 1, 1, 0, 0, 0, 1], 1) ➞ [1]

zero_indices([1, 0, 0, 0, 0, 1], 1) ➞ [1]

zero_indices([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 3) ➞ [6, 7, 9]

zero_indices([1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], 3) ➞ [7, 8, 9]
_____



[Notes]

If multiple combinations of indices tie for longest one sequence, return the indices which occur first (see examples #2, #3).


[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Sliding Window Algorithm
https://www.techiedelight.com/sliding-window-problems/
In sliding window technique, we maintain a window that satisfies the problem constraints. The window is unstable if it violates the problem constraints and it tries sta …
_________

"""
#Your code should go here:

