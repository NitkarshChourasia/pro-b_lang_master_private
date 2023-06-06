"""
####  Concatenate to Form Target List  ####

Create a function that returns True if smaller lists can concatenate to form the target list and False otherwise.


[Examples]

___
canConcatenate([[1, 2, 3, 4], [5, 6], [7]], [1, 2, 3, 4, 5, 6, 7]) ➞ True

canConcatenate([[2, 1, 3], [5, 4, 7, 6]], [7, 6, 5, 4, 3, 2, 1]) ➞ True

canConcatenate([[2, 1, 3], [5, 4, 7, 6, 7]], [1, 2, 3, 4, 5, 6, 7]) ➞ False
# Duplicate 7s not found in target list.

canConcatenate([[2, 1, 3], [5, 4, 7]], [1, 2, 3, 4, 5, 6, 7]) ➞ False
# Missing 6 from target list.
_____



[Notes]

___
*) Lists do not have to be sorted (see example #2).
*) Lists should concatenate to create the final list exactly (see examples #3 and #4).
___



[arrays] [sorting] [validation] 



-------------------------------------------------------------------
[Resources]
_________
How to flatten a shallow list in Python?
https://stackoverflow.com/questions/406121/flattening-a-shallow-list-in-python
Is there a simple way to flatten a list of iterables with a list comprehension, or failing that, what would you all consider to be the best way to flatten a shallow lis …
_________
_________
sorted() Function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
numpy.concatenate Method
https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
Join a sequence of arrays along an existing axis.
_________

"""
#Your code should go here:

