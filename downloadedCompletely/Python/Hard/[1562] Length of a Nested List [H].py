"""
####  Length of a Nested List  ####

Python's len() method will return the number of elements in a list. For example, the list below contains 2 elements:
___
[1, [2, 3]]
# 2 elements, number 1 and list [2, 3]
_____

Suppose we instead wanted to know the total number of non-nested items in the nested list. In the above case, [1, [2, 3]] contains 3 non-nested items, 1, 2 and 3.
Create a function that returns the total number of non-nested items in a nested list.


[Examples]

___
get_length([1, [2, 3]]) ➞ 3

get_length([1, [2, [3, 4]]]) ➞ 4

get_length([1, [2, [3, [4, [5, 6]]]]]) ➞ 6

get_length([1, [2], 1, [2], 1]) ➞ 5
_____



[Notes]

An empty list should return 0.


[arrays] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________

"""
#Your code should go here:

