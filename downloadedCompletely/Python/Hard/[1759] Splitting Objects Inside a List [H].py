"""
####  Splitting Objects Inside a List  ####

You bought a few bunches of fruit over the weekend. Create a function that splits a bunch into singular objects inside a list.


[Examples]

___
split_bunches([
  { "name": "grapes", "quantity": 2 }
]) ➞ [
  { "name": "grapes", "quantity": 1 },
  { "name": "grapes", "quantity": 1 }
]


split_bunches([
  { "name": "currants", "quantity": 1 },
  { "name": "grapes", "quantity": 2 },
  { "name": "bananas", "quantity": 2 }
]) ➞ [
  { "name": "currants", "quantity": 1},
  { "name": "grapes", "quantity": 1 },
  { "name": "grapes", "quantity": 1 },
  { "name": "bananas", "quantity": 1 },
  { "name": "bananas", "quantity": 1 }
]
_____



[Notes]

___
*) The input list will never be empty.
*) Objects will always have a name and quantity over 0.
*) The returned object should have each fruit in the same order as the original.
___



[arrays] [loops] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Flatten a List of Lists in One Line
https://coderwall.com/p/rcmaea/flatten-a-list-of-lists-in-one-line-in-python
A protip by terrasea about python, list comprehension, and flatten lists.
_________
_________
How to Iterate Through a Dictionary
https://realpython.com/iterate-through-dictionary-python/
In this step-by-step tutorial, you'll take a deep dive into how to iterate through a dictionary in Python. Dictionaries are a fundamental data structure, and you'll be …
_________

"""
#Your code should go here:

