"""
####  What Gives a Bad Mood?  ####

The factors said to have the greatest impact on someone's mood are: weather, meals, and sleep. Your task is, given a list of sublists of different values for: Mood, Weather, Meals, and Sleep, determine which other variable has had the greatest impact on the mood.


[Examples]

___
greatest_impact([
  [1, 1, 3, 10],
  [1, 1, 3, 10],
  [1, 1, 3, 10]
]) ➞ "Weather"

# As it was always low but all others were high.

greatest_impact([
  [10, 10, 3, 10],
  [10, 10, 3, 10],
  [10, 10, 3, 10]
]) ➞ "Nothing"

# As all were always high.
_____



[Notes]

The mood will always go from 1 to 10, the weather will always go from 1 to 10, the meals will always go from 1 to 3, and the sleep will always go from 1 to 10. In cases of mood and weather, 1 is negative and 10 is positive. All sublists values will be in the order [Mood, Weather, Meals, Sleep].


[algorithms] [arrays] 



-------------------------------------------------------------------
[Resources]
_________
Indexing a Sublist
https://www.geeksforgeeks.org/python-indexing-a-sublist/
In Python, we have several ways to perform the indexing in list, but sometimes, we have more than just an element to index, the real problem starts when we have a subli …
_________
_________
How to Iterate Through a Dictionary
https://realpython.com/iterate-through-dictionary-python/
In this step-by-step tutorial, you'll take a deep dive into how to iterate through a dictionary in Python. Dictionaries are a fundamental data structure, and you'll be …
_________
_________
Using the Python zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________
_________
all() Method
https://www.w3schools.com/python/ref_func_all.asp
Returns True if all items in an iterable are true, otherwise it returns False.
_________

"""
#Your code should go here:

