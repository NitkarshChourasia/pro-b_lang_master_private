"""
####  Validate Phone Numbers  ####

Write a function that returns True if the phone number is in a valid format. Valid formats are as follows:



[Examples]

___
validate("578-332-1114") ➞ True

validate("57-332-1114") ➞ False

validate("577 332  1114") ➞ False
# More than one space in between digits clusters.

validate("57 332 1114") ➞ False
# Unacceptable digit cluster length.

validate("157%332-1114") ➞ False
# Unacceptable delimiter.
_____



[Notes]

___
*) The country code will always be +1 or 1.
*) Each phone number will contain either 10 or 11 digits (depending on whether the country code exists).
*) There must either be exactly one space, a delimiter, or no space at all between the digit clusters.
*) You do not have to worry about extensions.
___



[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regex Tester and Debugger
https://regex101.com/
With highlighting for PHP, PCRE, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

