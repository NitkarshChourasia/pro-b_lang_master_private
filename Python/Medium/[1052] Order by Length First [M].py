"""
####  Order by Length First  ####

Graded lexicographic order (grlex order for short) is a way of ordering words that:

For example, in grlex order:
___
*) "tray" < "trapped" since "tray" has length 4 while "trapped" has length 7.
*) "trap" < "tray" since both have length 4, but "trap" comes before "tray" in the dictionary.
___

Given a list of words, return that list in grlex order.


[Examples]

___
make_grlex(["small", "big"]) ➞ ["big", "small"]

make_grlex(["cat", "ran", "for", "the", "rat"]) ➞ ["cat", "for", "ran", "rat", "the"]

make_grlex(["this", "is", "a", "small", "test"]) ➞ ["a", "is", "test", "this", "small"]
_____



[Notes]

N/A


[conditions] [math] [sorting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Sorted Function Using Key Parameter
https://medium.com/analytics-vidhya/sorted-function-using-key-parameter-in-python-7aa9b8cebfb6
Will return new sorted list of the iterable object(list,dictionary,tuple). By default, it will sort in ascending order. key(Optional): If we specify key,it will sort the…
_________
_________
len and alphabetical
https://stackoverflow.com/questions/46484895/sort-string-array-first-on-length-then-alphabetically-in-python-3?rq=1
How to sort an array in python firstly by the length of the words (longest to shortest), and then alphabetically?
_________
_________
Python Sorting
https://developers.google.com/edu/python/sorting#exercise:-list1.py
The easiest way to sort is with the sorted(list) function, which takes a list and returns a new list with those elements in sorted order. The original list is not changed.
_________
_________
How to sort by length of string followed by alphabetical order?
https://stackoverflow.com/questions/4659524/how-to-sort-by-length-of-string-followed-by-alphabetical-order
Python's sort is stable, which means that sorting the list by length leaves the elements in alphabetical order when the length is equal.
_________

"""
#Your code should go here:

