"""
####  Group in Order  ####

Create a function that groups a list of numbers based on a size parameter. The size represents the maximum length of each sub-list.
___
[1, 2, 3, 4, 5, 6], 3
[[1, 3, 5], [2, 4, 6]]
# Divide list into groups of size 3.

[1, 2, 3, 4, 5, 6], 2
[[1, 4], [2, 5], [3, 6]]
# Divide list into groups of size 2.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4
[[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9]]
# "Leftover" lists are okay.
_____



[Examples]

___
group([1, 2, 3, 4], 2) ➞ [[1, 3], [2, 4]]

group([1, 2, 3, 4, 5, 6, 7], 4) ➞ [[1, 3, 5, 7], [2, 4, 6]]

group([1, 2, 3, 4, 5], 1) ➞ [[1], [2], [3], [4], [5]]

group([1, 2, 3, 4, 5, 6], 4) ➞ [[1, 3, 5], [2, 4, 6]]
_____



[Notes]

___
*) The size parameter represents the maximum size for each sub-list (see ex.4). You should try to fill each sub-list evenly. In other words, ex.4 should be [[1, 3, 5], [2, 4, 6]], not [[1, 3, 5, 6], [2, 4]].
*) Keep the relative order of the numbers in each sub-list the same as the order in the original list.
*) When distributing the numbers into the sub-lists, each sub-list should have a number in it prior to receiving a new number (e.g. for example 1, your sub-lists will be of size 2, and because there are 4 numbers, you will need 2 sub-lists. When interating through the original list to fill the sub-lists it should go [[],[]] -> [[1],[]] -> [[1],[2]] -> [[1, 3], [2]] -> [[1, 3], [2, 4]]).
___



[arrays] [closures] [scope] 



-------------------------------------------------------------------
[Resources]
_________
Python Indexing and Slicing for Lists and other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
List is arguably the most useful and ubiquitous type in Python. One of the reasons it’s so handy is Python slice notation. In short, slicing is a flexible tool to build …
_________
_________
range() Method
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
How to Slice Lists/Arrays and Tuples in Python 
https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
A guide to slicing Python lists/arrays and Tuples, using multiple forms of syntax. We can use the short form of Python slicing, or the slice method.
_________

"""
#Your code should go here:

