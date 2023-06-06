"""
####  Backspace Attack  ####

Suppose a hash # represents the BACKSPACE key being pressed. Write a function that transforms a string containing # into a string without any #.


[Examples]

___
erase("he##l#hel#llo") ➞ "hello"

erase("major# spar##ks") ➞ "majo spks"

erase("si###t boy") ➞ "t boy"

erase("####") ➞ ""
_____



[Notes]

___
*) In addition to characters, backspaces can also remove whitespaces.
*) If the number of hashes exceeds the previous characters, remove those previous characters entirely (see example #3).
*) If there only exist backspaces, return an empty string (see example #4).
___



[regex] [scope] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Substituting Patterns in Text Using Regex
https://www.geeksforgeeks.org/python-substituting-patterns-in-text-using-regex/
Regular Expression (regex) is meant for pulling out the required information from any text which is based on patterns. They are also widely used for manipulating the pa …
_________
_________
Slice and Concatenation
https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/
Remove the ith character from the string using slice + concatenation
_________

"""
#Your code should go here:

