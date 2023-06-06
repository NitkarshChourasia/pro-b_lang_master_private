"""
####  Is It an Ordered Sublist?  ####

Given two lists smlst and biglst, we say smlst is an ordered sublist of biglst if all the elements of smlst can be found in biglst, and in the same order.
Examples:
___
*) [4, 3, 2] is an ordered sublist of [5, 4, 3, 2, 1].
*) [5, 3, 1] is an ordered sublist of [5, 4, 3, 2, 1].
*) [5, 3, 1] is not and ordered sublist of [1, 2, 3, 4, 5] since elements are not in the same - [1, 2, 3] is an ordered sublist of [3, 2, 1, 2, 3].
___

Write a function that, given lists smlst and biglst, decides if smlst is an ordered sublist of biglst.


[Examples]

___
is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]) ➞ True

is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]) ➞ True

is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]) ➞ False

is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]) ➞ True
_____



[Notes]

Be careful of examples like the fourth example, where the elements of smlst appear multiple times in biglst.


[arrays] [language_fundamentals] [loops] [sorting] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Exception Handling Using Try, Except and Finally Statement
https://www.programiz.com/python-programming/exception-handling
In this tutorial, you'll learn how to handle exceptions in your Python program using try, except and finally statements with the help of examples.
_________
_________
index() Method
https://www.programiz.com/python-programming/methods/list/index
Returns the index of the specified element in the list.
_________
_________
Indexing and Slicing for Lists and other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
Python, one of the most in-demand machine learning languages, supports slice notation for any sequential data type like lists, strings, and others. Discover more about …
_________

"""
#Your code should go here:

