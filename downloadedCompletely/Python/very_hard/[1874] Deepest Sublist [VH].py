"""
####  Deepest Sublist  ####

You are given a list which may contain sublists. Your task is to find the depth of the deepest sublist.
___
*) [a] = 1 depth
*) [[a]] = 2 depth
*) [[[a]]] = 3 depth, etc
___



[Examples]

___
deepest([1, [2, 3], 4, [5, 6]]) ➞ 2

deepest([[[[[[[[[[1]]]]]]]]]]) ➞ 10

deepest([1, 4, [1, 4, [1, 4, [1, 4, [5]]]]]) ➞ 5
_____



[Notes]

N/A


[arrays] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Python Nested List
https://www.learnbyexample.org/python-nested-list/
A list can contain any sort object, even another list (sublist), which in turn can contain sublists themselves, and so on. This is known as nested list. You can use the …
_________
_________
Lists of Lists, Functions, and Recursion
https://web.mit.edu/music21/doc/usersGuide/usersGuide_05_listsOfLists.html
In the last Chapter, we discussed Python Lists, how the Stream object is similar to a List, and how we can put Note objects into a Stream, look at their offsets, and .s …
_________

"""
#Your code should go here:

