"""
####  Priority Sort  ####

Given a list and a set, return a sorted list with its items in ascending order but prioritize the elements in the set over the other items in the list.


[Examples]

___
priority_sort([5, 4, 3, 2, 1], {2, 3}) ➞ [2, 3, 1, 4, 5]

priority_sort([5, 4, 3, 2, 1], {3, 6}) ➞ [3, 1, 2, 4, 5]

priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}) ➞ [-4, -3, -5, -2, -1, 0]
_____



[Notes]

___
*) If the list is empty, return an empty list.
*) If the set is empty there is nothing to prioritize, but the list should still be sorted.
*) The set may contain values that are not in the list.
*) The list may contain duplicates.
*) The list and the set will only contain integer values.
___



[conditions] [language_fundamentals] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
Sorting
https://docs.python.org/3/howto/sorting.html
Python lists have a built-in list.sort() method that modifies the list in-place. There is also a sorted() built-in function that builds a new sorted list from an iterable.
_________
_________
How to Use sorted() and sort()
https://realpython.com/python-sort/
In this step-by-step tutorial, you’ll learn how to sort in Python. You'll know how to sort various types of data in different data structures, customize the order, and …
_________
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
In this tutorial, we will learn about the Python List count() method with the help of examples.
_________

"""
#Your code should go here:

