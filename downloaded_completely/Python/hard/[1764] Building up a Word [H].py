"""
####  Building up a Word  ####

You are given an input list of strings, ordered by ascending length.
Write a function that returns True if, for each pair of consecutive strings, the second string can be formed from the first by adding a single letter either at the beginning or end.


[Examples]

___
can_build(["a", "at", "ate", "late", "plate", "plates"]) ➞ True

can_build(["a", "at", "ate", "late", "plate", "plater", "platter"]) ➞ False
# "platter" is formed by adding "t" in the middle of "plater"

can_build(["it", "bit", "bite", "biters"]) ➞ False
# "biters" is formed by adding two letters - we can only add one

can_build(["mean", "meany"]) ➞ True
_____



[Notes]

___
*) Return False if a word is NOT formed by adding only one letter.
*) Return False if the letter is added to the middle of the previous word.
*) Letters in tests will all be lower case.
___



[arrays] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
zip() Function
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it. In this tutorial, we will learn about Python zip() in detail with the help of examples.
_________

"""
#Your code should go here:

