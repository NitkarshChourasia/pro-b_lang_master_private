"""
####  Leaderboard Sort  ####

Given an array of users, each defined by an object with the following properties: name, score, reputation create a function that sorts the array to form the correct leaderboard.
The leaderboard takes into consideration the score of each user of course, but an emphasis is put on their reputation in the community, so to get the trueScore, you should add the reputation multiplied by 2 to the score.
Once you know the trueScore of each user, sort the array according to it in descending order.


[Examples]

___
leaderboards([
  { "name": "a", "score": 100, "reputation": 20 },
  { "name": "b", "score": 90, "reputation": 40 },
  { "name": "c", "score": 115, "reputation": 30 },
]) ➞ [
  { "name": "c", "score": 115, "reputation": 30 },  # trueScore = 175
  { "name": "b", "score": 90, "reputation": 40 },   # trueScore = 170
  { "name": "a", "score": 100, "reputation": 20 }   # trueScore = 140
]
_____



[Notes]

N/A


[arrays] [objects] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
How to Use sorted() and sort() in Python
https://realpython.com/python-sort/
In this step-by-step tutorial, you’ll learn how to sort in Python. You'll know how to sort various types of data in different data structures, customize the order, and …
_________
_________
Dictionaries
https://realpython.com/python-dicts/
In this Python dictionaries tutorial you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, yo …
_________
_________
Sorting a Dictionary
https://towardsdatascience.com/sorting-a-dictionary-in-python-4280451e1637
We can sort lists, tuples, strings, and other iterable objects in python since they are all ordered objects. Well, as of python 3.7, dictionaries remember the order of …
_________

"""
#Your code should go here:

