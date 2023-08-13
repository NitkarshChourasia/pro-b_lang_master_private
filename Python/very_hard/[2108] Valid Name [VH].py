"""
####  Valid Name  ####

For this exercise, keep in mind the following two terms (mutually exclusive):

A valid name is a name written in one of the following ways:
___
*) H. Wells
*) H. G. Wells
*) Herbert G. Wells
*) Herbert George Wells
___

The following names are invalid:
___
*) Herbert or Wells (single names not allowed)
*) H Wells or H. G Wells (initials must end with dot)
*) h. Wells or H. wells or h. g. Wells (incorrect capitalization)
*) H. George Wells (middle name expanded, while first still left as initial)
*) H. G. W. (last name is not a word)
*) Herb. G. W. (dot only allowed after initial, not word)
___



[Rules]


Your task is to write a function that determines whether a name is valid or not. Return True if the name is valid, False otherwise.


[Examples]

___
valid_name("H. Wells") ➞ True

valid_name("H. G. Wells") ➞ True

valid_name("Herbert G. Wells") ➞ True

valid_name("Herbert") ➞ False
# Must be 2 or 3 words

valid_name("h. Wells") ➞ False
# Incorrect capitalization

valid_name("H Wells") ➞ False
# Missing dot after initial

valid_name("H. George Wells") ➞ False
# Cannot have: initial first name + word middle name

valid_name("H. George W.") ➞ False
# Last name cannot be initial
_____



[Notes]

N/A


[conditions] [functional_programming] [regex] 



-------------------------------------------------------------------
[Resources]
_________
isupper() Method
https://www.programiz.com/python-programming/methods/string/isupper
Returns whether or not all characters in a string are uppercased or not.
_________
_________
len() Method
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________

"""
#Your code should go here:

