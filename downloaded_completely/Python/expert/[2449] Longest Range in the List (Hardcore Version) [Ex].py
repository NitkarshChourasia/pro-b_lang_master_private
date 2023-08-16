"""
####  Longest Range in the List (Hardcore Version)  ####

This challenge is a harder version of a previous challenge, but now with an additional efficiency requirement (see the "The catch" discussion below). We first recall the problem:
Given a list of integers, find the length of the longest range of consecutive integers that are contained in the sorted version of the list.
Here's an illustrative example. Consider the list:
___
[4, 9, 10, 5, 17, 3, 8, 11, 1, 12, 18, 20]
_____

... which, after sorting, becomes:
___
[1, 2, 4, 5, 8, 9, 10, 11, 12, 17, 18, 20]
_____

The longest consecutive subsequence is clearly [8, 9, 10, 11, 12], which has length 5.


[The Catch]

Looking at the problem, a natural way to approach it is to first sort the list. However, the lists in the tests have been designed so that sorting is a little too slow (more details on the notes below).
Thus, you will probably want a faster solution that does not rely on sorting.


[Examples]

___
max_consec([4, 9, 10, 5, 17, 3, 8, 11, 1, 12, 18, 20]) ➞ 5
# After sorting list becomes [1, 2, 4, 5, 8, 9, 10, 11, 12, 17, 18, 20]
# Longest consecutive subsequence is [8, 9, 10, 11, 12], which has length 5

max_consec([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]) ➞ 6
# After sorting get [1, 2, 2, 3, 4, 5, 5, 6, 8, 8, 9, 10, 11, 13, 13, 14]
# Longest consecutive subsequence is [1, 2, 3, 4, 5, 6], which has length 6
_____



[Notes]

___
*) The intended solution to this challenge runs in linear O(n) time, and I think that a linear solution will be needed to pass the tests.
*) It is well known that sorting a list of length n can be done in O(n log n) time. However, this is a worst-case scenario, as sorting is often faster if the list already has some order to it. As such, to make sorting unviable, the tests start by generating a very large (2**20 elements) random list, then inserting consecutive sequences into that list.
*) Generating such a massive list takes a fair amount of the available time, with some variation (6~7 seconds). As such, the two rounds of tests (i.e. the two times that your function is run) are allotted a total run time of 5s. For reference, the run times for my solution vary in the 3.8s-4.2s range.
*) I apologize in advance for the short time margin for the tests. As it turns out, even for n = 2**20 one still has log n = 20, so sorting runs in about O(20n), still making it pretty hard to beat (and more so because, from what I hear, sorting in Python runs using C code). As such, even for such a large list, my linear O(n) solution only beats sorting by a factor of about 1.5~1.7. This discrepancy could be made larger for even larger lists, but such lists can not be created within the 12s time limit for the server.
___



[algorithms] [arrays] [numbers] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

