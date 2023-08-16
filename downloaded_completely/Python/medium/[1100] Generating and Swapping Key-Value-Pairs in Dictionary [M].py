"""
####  Generating and Swapping Key-Value-Pairs in Dictionary  ####

Create a function that takes:

The function returns the constructed dict. Empty lists return an empty dict.


[Examples]

___
swap_d([1, 2, 3], ["one", "two", "three"], False)
➞ { 1: "one", 2: "two", 3: "three" }

swap_d([1, 2, 3], ["one", "two", "three"], True)
➞ { "one": 1, "two": 2, "three": 3 }

swap_d(["Paris", 3, 4.5], ["France", "is odd", "is half of 9"], True)
➞ { "France": "Paris", "is odd": 3, "is half of 9": 4.5 }
_____



[Notes]

___
*) To make it simple, use only hashable (= immutable) keys.
*) To make it simple, use only unique keys.
___



[data_structures] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Convert a List to Dictionary
https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/
Given a list, write a Python program to convert the given list to dictionary such that all the odd elements have the key, and even number elements have the value. Since …
_________
_________
Map Two Lists into a Dictionary
https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-13.php
Write a Python program to remove a key from a dictionary.
_________
_________
Python Program to Swap Keys and Values in Dictionary
https://www.geeksforgeeks.org/python-program-to-swap-keys-and-values-in-dictionary/
Dictionary is quite a useful data structure in programming that is usually used to hash a particular key with value, so that they can be retrieved efficiently. Let’s di …
_________

"""
#Your code should go here:

