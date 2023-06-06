"""
####  Remix the String  ####

Create a function that takes both a string and a list of integers and rearranges the letters in the string to be in the order specified by the index numbers. Return the "remixed" string.


[Examples]

___
remix("abcd", [0, 3, 1, 2]) ➞ "acdb"
_____

The string you'll be returning will have:
___
*) "a" at index 0
*) "b" at index 3
*) "c" at index 1
*) "d" at index 2
___

... because the order of those characters maps to their corresponding numbers in the index list.
___
remix("PlOt", [1, 3, 0, 2]) ➞ "OPtl"

remix("computer", [0, 2, 1, 5, 3, 6, 7, 4]) ➞ "cmourpte"
_____



[Notes]

___
*) Be sure not to change the original case.
*) Assume you'll be given a string and list of equal length, both containing valid characters (A-Z, a-z, or 0-9).
*) The list of numbers could potentially be more than nine (i.e. double figures).
___



[arrays] [formatting] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Using the Python zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________
_________
Splitting, Concatenating, and Joining Strings
https://realpython.com/python-string-split-concatenate-join/
In Python, strings are represented as str objects, which are immutable: this means that the object as represented in memory can not be directly altered. These two facts …
_________
_________
How to Use sorted() and sort() Functions
https://realpython.com/python-sort/
In this step-by-step tutorial, you’ll learn how to sort in Python. You'll know how to sort various types of data in different data structures, customize the order, and …
_________
_________
Iterating Over Dictionary
https://dev-notes.eu/2017/09/iterating-over-dictionary-in-python/
A dictionary in Python is a collection of unordered values accessed by key rather than index. Dictionary elements have no intrinsic order. This short article shows sev …
_________

"""
#Your code should go here:

