"""
####  First Recurrence Index  ####

Create a function that identifies the very first item that has recurred in the string argument passed. It returns the identified item with the index where it first appeared and the very next index where it resurfaced ⁠— entirely as an dictionary; or as an empty dictionary if the argument is either None, an empty string, or no recurring item exists.


[Examples]

___
recur_index("DXTDXTXDTXD") ➞ {"D": [0, 3]}
// D first appeared at index 0, resurfaced at index 3
// T appeared and resurfaced at indices 3 and 6 but D completed the cycle first

recur_index("YXZXYTUVXWV") ➞ {"X": [1, 3]}

recur_index("YZTTZMNERXE") ➞ {"T": [2, 3]}

recur_index("AREDCBSDERD") ➞ {"D": [3, 7]}

recur_index("") ➞ {}

recur_index(None) ➞ {}
_____



[Notes]

___
*) You can solve this challenge via a recursive approach, alternatively.
*) A recursive version of this challenge can be found here.
___



[arrays] [logic] [objects] [validation] 



-------------------------------------------------------------------
[Resources]
_________
any() Function
https://beginnersbook.com/2019/03/python-any-function/
Accepts iterable (list, tuple, dictionary etc.) as an argument and return true if any of the element in iterable is true, else it
_________
_________
Dictionary Comprehension
https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
Learn all about Python dictionary comprehension: how you can use it to create dictionaries, to replace (nested) for loops or lambda functions with map(), filter() and r …
_________
_________
When to Use a List Comprehension
https://realpython.com/list-comprehension-python/
Python list comprehensions make it easy to create lists while performing sophisticated filtering, mapping, and conditional logic on their members. In this tutorial, you …
_________

"""
#Your code should go here:

