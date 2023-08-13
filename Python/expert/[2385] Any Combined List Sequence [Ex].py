"""
####  Any Combined List Sequence  ####

The goal is to test if a consecutive sequence can be formed. A consecutive sequence is defined as a sequence of incrementing numbers (e.g. 1, 2, 3 or 5, 6, 7, 8). The twist is that you have to consider the combination of lists as shown. You can combine any two elements from different lists.
___
[-5 1 3 5 ] => [3 5 1 -5 ] => [3+4  5+3  1+8  15-5] = [7 8 9 10] => True
[4 3 8  15] => [4 3 8  15]
_____

Also important is that the lists can be of different sizes, allowing for partially unpaired numbers in some cases.
___
[2 2 2  ] => [2 2 2 0] => [2+5  2+6  2+7  10+0] = [7 8 9 10] => True
[10 5 6 7] => [5 7 6 10]
_____



[Notes]

___
*) Each list has at least 2 elements.
*) Try the easier version.
___



[arrays] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Python Lists
https://www.w3schools.com/python/python_lists.asp
Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, …
_________

"""
#Your code should go here:

