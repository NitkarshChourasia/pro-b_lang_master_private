"""
####  Number of Boomerangs  ####

A boomerang is a V-shaped sequence that is either upright or upside down. Specifically, a boomerang can be defined as: sub-list of length 3, with the first and last digits being the same and the middle digit being different.
Some boomerang examples:
___
[3, 7, 3], [1, -1, 1], [5, 6, 5]
_____

Create a function that returns the total number of boomerangs in a list.
To illustrate:
___
[3, 7, 3, 2, 1, 5, 1, 2, 2, -2, 2]
# 3 boomerangs in this sequence:  [3, 7, 3], [1, 5, 1], [2, -2, 2]
_____

Be aware that boomerangs can overlap, like so:
___
[1, 7, 1, 7, 1, 7, 1]
# 5 boomerangs (from left to right): [1, 7, 1], [7, 1, 7], [1, 7, 1], [7, 1, 7], and [1, 7, 1]
_____



[Examples]

___
count_boomerangs([9, 5, 9, 5, 1, 1, 1]) ➞ 2

count_boomerangs([5, 6, 6, 7, 6, 3, 9]) ➞ 1

count_boomerangs([4, 4, 4, 9, 9, 9, 9]) ➞ 0
_____



[Notes]

[5, 5, 5] (triple identical digits) is NOT considered a boomerang because the middle digit is identical to the first and last.


[arrays] [loops] 



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.w3schools.com/python/ref_list_count.asp
Returns the number of elements with the specified value.
_________
_________
List Comprehensions
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
Constructs that allow sequences to be built from other sequences.
_________
_________
sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds start and items of the given iterable from left to right.
_________

"""
#Your code should go here:

