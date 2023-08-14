"""
####  Decrypt the String from Digits to Letters  ####

Given a string s consisting from digits and #, translate s to English lowercase characters as follows:
___
*) Characters ("a" to "i") are represented by ("1" to "9").
*) Characters ("j" to "z") are represented by ("10#" to "26#").
___



[Examples]

___
decrypt("10#11#12") ➞ "jkab"

decrypt("1326#") ➞ "acz"

decrypt("25#") ➞ "y"
_____



[Notes]

N/A


[conditions] [cryptography] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
chr() and ord() Methods
https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods
In this lesson, we'll work with the python chr() and ord() functions. Python’s built in function chr() is used for converting an Integer to a Character, while..
_________
_________
maketrans() and translate() Functions
https://www.tutorialspoint.com/python-maketrans-and-translate-functions
Returns a mapping table for translation usable for translate() method. This is a static method that creates a ...
_________
_________
Regexes
https://realpython.com/regex-python/
In previous tutorials in this series, you've seen several different ways to compare string values with direct character-by-character comparison. In this tutorial, you'l …
_________
_________
Replace Strings
https://note.nkmk.me/en/python-str-replace-translate-re-sub/
This post describes how to replace strings in Python. Replace substrings: replace(). Specify the maximum count of replacements: count. Replace multiple different substr …
_________
_________
Looping Through Dictionary Items
https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp
When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
_________

"""
#Your code should go here:

