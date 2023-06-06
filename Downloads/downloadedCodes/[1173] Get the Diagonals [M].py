"""
####  Get the Diagonals  ####

Given a square list (n*n size) implement a function that returns a new list containing two lists equal to the two diagonals, in the following order:
___
diagonal 1 = from upper-left to lower-right corner
diagonal 2 = from upper-right to lower-left corner
_____



[Examples]

___
get_diagonals([ [1, 2], [3, 4] ]) ➞ [ [1, 4], [2, 3] ]

get_diagonals([ ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"] ]) ➞ [ ["a", "e", "i"], ["c", "e", "g"] ]

get_diagonals([ [True] ]) ➞ [ [True], [True] ]
_____



[Notes]

___
*) Your function must also work with single elements or empty lists.
*) Try to build both diagonals with a single loop.
___



[arrays] [language_fundamentals] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Print Diagonals of 2D List
https://www.geeksforgeeks.org/python-print-diagonals-of-2d-list/
We can use one-liner list comprehension along with xrange() function. xrange() is used to iterate a certain number of times in for loops. Thus, we print the element at …
_________

"""
#Your code should go here:

