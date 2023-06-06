"""
####  Generating Words from Names  ####

Write a function that returns True if a given name can generate an array of words.


[Examples]

___
anagram("Justin Bieber", ["injures", "ebb", "it"]) ➞ True

anagram("Natalie Portman", ["ornamental", "pita"]) ➞ True

anagram("Chris Pratt", ["chirps", "rat"]) ➞ False
# Not all letters are used

anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) ➞ False
# "s" does not exist in the original name
_____



[Notes]

___
*) Each letter in the name may only be used once.
*) All letters in the name must be used.
___



[arrays] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
split() Method
https://www.w3schools.com/python/ref_string_split.asp
Split a string into a list where each word is a list item.
_________
_________
count() Method
https://www.w3schools.com/python/ref_string_count.asp
Returns the number of times a specified value appears in the string.
_________
_________
sorted() Function
https://www.w3schools.com/python/ref_func_sorted.asp
Returns a sorted list of the specified iterable object. You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numeri …
_________

"""
#Your code should go here:

