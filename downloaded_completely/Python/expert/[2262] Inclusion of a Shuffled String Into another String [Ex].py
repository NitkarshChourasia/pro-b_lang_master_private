"""
####  Inclusion of a Shuffled String Into another String  ####

The function is given two strings s1 and s2. Determine if one of the permutations of characters of s1 is a substring of s2, return True / False.


[Examples]

___
check_inclusion("ab", "edabitbooo") ➞ True
# "ab" is in s2.

check_inclusion("ab", "edaoboat") ➞ False
# neither "ab" or "ba" is in s2.

check_inclusion("adc", "dcda") ➞ True
# "cda" is a permutation of "adc" and it is in s2.

check_inclusion("sgyuws", "oldqwqdmlvsguswyfbj") ➞ True
# "sguswy" is a permutation of s1 and it is in s2.
_____



[Notes]

All characters in both strings are lowercase letters.


[algorithms] [conditions] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
sorted() Function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________

"""
#Your code should go here:

