"""
####  Give Steps to Sort a List  ####

Given a shuffled list l, return a sequence of transpositions which sorts the list (as in sorted(l)). A transposition is a pair of indices (i, j) representing that l[i] and l[j] be swapped. Specifically, the output is a list of transpositions to be applied. Transpositions are applied as in:
___
def apply_transpositions(l, swaps):
  for i, j in swaps:
  l[i], l[j] = l[j], l[i]
return l
_____



[Examples]

___
sorting_steps([5, -5]) ➞ [(0, 1)]
# Swap first and second elements.

sorting_steps([4, 3, 2, 1]) ➞ [(0, 3), (1, 2)] or even [(0, 1), (1, 2), (2, 3), (0, 1), (1, 2), (0, 1)]

sorting_steps([6, 6]) ➞ []
_____



[Notes]

Output is not unique! A given list may be sorted with varying numbers of transpositions stemming from various sorting techniques. You need only produce output which works. (This gives the problem algorithimic freedom!)


[algorithms] [arrays] [loops] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
index() Method
https://www.programiz.com/python-programming/methods/list/index
Returns the index of the specified element in the list.
_________
_________
append() Method
https://www.programiz.com/python-programming/methods/list/append
Adds an item to the end of the list. In this tutorial, we will learn about the Python append() method in detail with the help of examples.
_________
_________
Sorting Algorithms
https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
Refers to arranging data in a particular format. Sorting algorithm specifies the way to arrange data in a particular order. Most common orders are in nu...
_________

"""
#Your code should go here:

