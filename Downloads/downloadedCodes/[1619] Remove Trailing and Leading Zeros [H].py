"""
####  Remove Trailing and Leading Zeros  ####

Create a function that takes in a number as a string n and returns the number without trailing and leading zeros.
___
*) Trailing Zeros are the zeros after a decimal point which don't affect the value (e.g. the last three zeros in 3.4000 and 3.04000).
*) Leading Zeros are the zeros before a whole number which don't affect the value (e.g. the first three zeros in 000234 and 000230).
___



[Examples]

___
remove_leading_trailing("230.000") ➞ "230"

remove_leading_trailing("00402") ➞ "402"

remove_leading_trailing("03.1400") ➞ "3.14"

remove_leading_trailing("30") ➞ "30"
_____



[Notes]

___
*) Return a string.
*) If you get a number with .0 on the end, return the integer value (e.g. return "4" rather than "4.0").
*) If the number is 0, 0.0, 000, 00.00, etc... return "0".
___



[formatting] [numbers] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python Trim String - rstrip(), lstrip(), strip()
https://www.journaldev.com/23625/python-trim-string-rstrip-lstrip-strip
Python Trim String, Python strip() function, Python lstrip(), Python rstrip(), Python remove leading and trailing whitespaces from string example code.
_________
_________
Converting Data Types: Numbers, Strings, Lists, Tuples
https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3
This Python 3 tutorial will guide you through converting data types including numbers, strings, tuples and lists, as well as provide examples to help familiarize yourse …
_________
_________
rstrip() Method
https://www.programiz.com/python-programming/methods/string/rstrip
Returns a copy of the string with trailing characters removed (based on the string argument passed).
_________
_________
string() Method
https://www.geeksforgeeks.org/string-endswith-python/
Returns True if a string ends with the given suffix otherwise returns False.
_________
_________
endswith() Method
https://www.w3schools.com/python/ref_string_endswith.asp
Check if the string ends with a punctuation sign (.)...
_________

"""
#Your code should go here:

