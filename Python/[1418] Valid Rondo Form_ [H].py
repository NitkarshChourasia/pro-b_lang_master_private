"""
####  Valid Rondo Form?  ####

Rondo Form is a type of musical structure, in which there is a recurring theme/refrain, notated as A. Here are the rules for valid rondo forms:
___
*) Rondo forms always start and end with an A section.
*) In between the A sections, there should be contrasting sections notated as B, then C, then D, etc... No letter should be skipped.
*) There shouldn't be any repeats in the sequence (such as ABBACCA).
___

Create a function which validates whether a given string is a valid Rondo Form.


[Examples]

___
valid_rondo("ABACADAEAFAGAHAIAJA") ➞ True

valid_rondo("ABA") ➞ True

valid_rondo("ABBACCA") ➞ False

valid_rondo("ACAC") ➞ False

valid_rondo("A") ➞ False
_____



[Notes]

___
*) Inputs will be given as all uppercase.
*) For the purposes of this challenge, accept ABA as valid Rondo forms.
___



[loops] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
replace() Method
https://note.nkmk.me/en/python-str-replace-translate-re-sub/
Here's how to replace strings in Python. Replace substrings: replace() Specify the maximum count of replacements: count Replace multiple different substrings Replace n …
_________
_________
Regular Expressions
https://realpython.com/regex-python/
In this tutorial, you’ll explore regular expressions, also known as regexes, in Python. A regex is a special sequence of characters that defines a pattern for complex s …
_________
_________
Rondo
https://en.wikipedia.org/wiki/Rondo
Rondo and the part-equivalent French term rondeau are words long used in music in a number of ways, most often in reference to a musical form.
_________

"""
#Your code should go here:

