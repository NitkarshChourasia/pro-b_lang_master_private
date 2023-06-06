"""
####  Oddly or Evenly Positioned  ####

Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).


[Examples]

___
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions

char_at_pos("EDABIT", "odd") ➞ "EAI"
# "E", "A" and "I" occupy the 1st, 3rd and 5th positions

char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd") ➞ ["A", "B", "T", "A", "I", "Y"]
_____



[Notes]

___
*) Lists are zero-indexed, so, index+1 = position or position-1 = index.
*) There will not be an empty string or an empty list.
*) (Optional) Try solving this challenge in a single-line lambda function.
*) A more advanced version of this challenge can be found here.
___



[arrays] [functional_programming] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Indexing and Slicing for Lists, Tuples, Strings, and other Sequential Types
https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
Python supports slice notation for any sequential data type like lists, strings, tuples, bytes, bytearrays, and ranges. Also, any new data structure can add its support …
_________
_________
Lists
https://developers.google.com/edu/python/lists
Python has a great built-in list type named "list". List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and …
_________
_________
isinstance() Function
https://www.w3schools.com/python/ref_func_isinstance.asp
Returns True if the specified object is of the specified type, otherwise False. If the type parameter is a tuple, this function will return True if the object is one o …
_________

"""
#Your code should go here:

