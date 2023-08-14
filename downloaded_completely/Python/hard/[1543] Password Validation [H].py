"""
####  Password Validation  ####

Create a function that validates a password to conform to the following rules:
___
*) Length between 6 and 24 characters.
*) At least one uppercase letter (A-Z).
*) At least one lowercase letter (a-z).
*) At least one digit (0-9).
*) Maximum of 2 repeated characters.
"aa" is OK 👍
"aaa" is NOT OK 👎
*) Supported special characters:
! @ # $ % ^ & * ( ) + = _ - { } [ ] : ; " ' ? < > , .
___



[Examples]

___
validate_password("P1zz@") ➞ False
// Too short.

validate_password("iLoveYou") ➞ False
// Missing a number.

validate_password("Fhg93@") ➞ True
// OK!
_____



[Notes]

N/A


[conditions] [regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
Python Regular Expressions
https://www.tutorialspoint.com/python/python_reg_expressions.htm
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Re …
_________

"""
#Your code should go here:

