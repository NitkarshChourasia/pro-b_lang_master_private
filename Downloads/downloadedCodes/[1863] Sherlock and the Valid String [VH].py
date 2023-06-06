"""
####  Sherlock and the Valid String  ####

Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string txt, determine if it is valid. If so, return "YES", otherwise return "NO".
For example, If txt = "abc", the string is valid because the frequencies of characters are all the same. If txt = "abcc", the string is also valid, because we can remove 1 "c" and have one of each character remaining in the string. However, if txt = "abccc", the string is not valid, because removing one character does not result in the same frequency of characters.


[Examples]

___
is_valid("aabbcd") ➞ "NO"
# We would need to remove two characters, both c and d  -> aabb or a and b -> abcd, to make it valid.
# We are limited to removing only one character, so it is invalid.

is_valid("aabbccddeefghi") ➞ "NO"
# Frequency counts for the letters are as follows:
# {"a": 2, "b": 2, "c": 2, "d": 2, "e": 2, "f": 1, "g": 1, "h": 1, "i": 1}
# There are two ways to make the valid string:
# Remove 4 characters with a frequency of 1: {f, g, h, i}.
# Remove 5 characters of frequency 2: {a, b, c, d, e}.
# Neither of these is an option.

is_valid("abcdefghhgfedecba") ➞ "YES"
# All characters occur twice except for e which occurs 3 times.
# We can delete one instance of e to have a valid string.
_____



[Notes]

N/A


[algorithms] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Counter
https://pymotw.com/2/collections/counter.html
Is a container that keeps track of how many times equivalent values are added. It can be used to implement the same algorithms for which bag or multiset data structures …
_________
_________
sorted() Function
https://www.programiz.com/python-programming/methods/built-in/sorted
Returns a sorted list from the items in an iterable. In this tutorial, we will learn to sort elements in ascending and descending order using the Python shorted() function.
_________
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Returns the number of times the specified element appears in the list.
_________

"""
#Your code should go here:

