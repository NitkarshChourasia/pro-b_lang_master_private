"""
####  The Frugal Gentleman  ####

Atticus has been invited to a dinner party, and he decides to purchase a bottle of wine. However, he has little knowledge of how to choose a good bottle. Being a very frugal gentleman (yet disliking looking like a cheapskate), he decides to use a very simple rule. In any selection of two or more wines, he will always buy the second-cheapest.
Given a list of wine dictionaries, write a function that returns the name of the wine he will buy for the party. If given an empty list, return None. If given a list of only one, Atticus will buy that wine.


[Examples]

___
chosen_wine([
  { "name": "Wine A", "price": 8.99 },
  { "name": "Wine 32", "price": 13.99 },
  { "name": "Wine 9", "price": 10.99 }
]) ➞ "Wine 9"

chosen_wine([{ "name": "Wine A", "price": 8.99 }]) ➞ "Wine A"

chosen_wine([]) ➞ None
_____



[Notes]

All wines will be different prices, so there is no confusion in the ordering.


[arrays] [objects] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________

"""
#Your code should go here:

