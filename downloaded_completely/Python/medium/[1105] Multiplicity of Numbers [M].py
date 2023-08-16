"""
####  Multiplicity of Numbers  ####

Write a function that returns a list of elements [number, multiplicity]. The multiplicity of a number refers to the number of times it occurs in the list.
To illustrate:
___
[5, 5, 1, 1, 5, 5, 3]
[[5, 4], [1, 2], [3, 1]]

# Since 5 appears 4 times, 1 appears twice, and 3 appearance once.
_____

The final list should only include unique elements, and the elements should be ordered by when they first appeared in the original list.


[Examples]

___
multiplicity([1, 1, 1, 2, 2, 3]) ➞ [[1, 3], [2, 2], [3, 1]]

multiplicity([1, 1, 1, 1, 1]) ➞ [[1, 5]]

multiplicity([1, 5, 4, 3, 2]) ➞ [[1, 1], [5, 1], [4, 1], [3, 1], [2, 1]]
_____



[Notes]

N/A


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
How can I count the occurrences of a list item?
https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
Given an item, how can I count its occurrences in a list in Python?
_________
_________
Using collections.OrderedDict.fromkeys()
https://favtutor.com/blogs/remove-duplicates-from-list-python
This is the fastest method to achieve the target of removing duplicates from the python list. This method will first remove the duplicates and return a dictionary that …
_________

"""
#Your code should go here:

