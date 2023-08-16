"""
####  Minimum Removals to Make Two Strings Anagrams  ####

Create a function that returns the smallest number of letter removals so that two strings are anagrams of each other.


[Examples]

___
min_removals("abcde", "cab") ➞ 2
# Remove "d", "e" to make "abc" and "cab".

min_removals("deafk", "kfeap") ➞ 2
# Remove "d" and "p" from the first and second word, respectively.

min_removals("acb", "ghi") ➞ 6
# Remove all letters from both words to get "" and "".
_____



[Notes]

___
*) An anagram is any string that can be formed by shuffling the characters of the original string. For example: baedc is an anagram of abcde.
*) An empty string can be considered an anagram of itself.
*) Characters won't be used more than once per string.
___



[data_structures] [strings] 



-------------------------------------------------------------------
[Resources]
_________
symmetric_difference() Method
https://www.w3schools.com/python/ref_set_symmetric_difference.asp
Returns a set that contains all items from both set, but not the items that are present in both sets.
_________
_________
Opposite of set.intersection in Python?
https://stackoverflow.com/questions/29947844/opposite-of-set-intersection-in-python
In Python you can use a.intersection(b) to find the items common to both sets. Is there a way to do the disjoint opposite version of this? Items that are not common to …
_________
_________
Python Set Operations
https://www.geeksforgeeks.org/python-set-operations-union-intersection-difference-symmetric-difference/
This article demonstrates different operations on Python sets (union, intersection, difference and symmetric difference).
_________

"""
#Your code should go here:

