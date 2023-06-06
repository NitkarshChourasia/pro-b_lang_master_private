"""
####  Burglary Series (16): Nested Objects (Dicts)  ####

And who cursed the most in the fight between you and your spouse?
Given a dict with three rounds, with nested dicts as your score per round, return who cursed the most based on the following:
___
*) If you, return "ME!"
*) If your spouse, return "SPOUSE!"
*) If a draw, return "DRAW!"
___



[Examples]

___
determine_who_cursed_the_most({
  "round1": { "me": 10, "spouse": 5 },
  "round2": { "me": 5, "spouse": 10 },
  "round3": { "me": 10, "spouse": 10 }}) ➞ "DRAW!"

determine_who_cursed_the_most({
  "round1": { "me": 40, "spouse": 5 },
  "round2": { "me": 9, "spouse": 10 },
  "round3": { "me": 9, "spouse": 10 }}) ➞ "ME!"

determine_who_cursed_the_most({
  "round1": { "me": 10, "spouse": 5 },
  "round2": { "me": 9, "spouse": 44 },
  "round3": { "me": 10, "spouse": 55 }}) ➞ "SPOUSE!"
_____



[Notes]

N/A


[arrays] [loops] [objects] 



-------------------------------------------------------------------
[Resources]
_________
Dictionaries
https://realpython.com/python-dicts/
In this Python dictionaries tutorial you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, yo …
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
Ternary Operator
https://www.geeksforgeeks.org/ternary-operator-in-python/
Also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. It simply a …
_________

"""
#Your code should go here:

