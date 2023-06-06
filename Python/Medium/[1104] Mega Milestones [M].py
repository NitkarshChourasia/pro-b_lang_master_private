"""
####  Mega Milestones  ####

Given an number, return a string which contains varying amounts of the word 'MEGA' depending on the given number's order of magnitude.
___
*) If the number is less than 100, return "not a mega milestone".
*) Otherwise, start with the string "MEGA milestone".
*) For every order of magnitude over 100 that the number is, add the word "MEGA" to the start of the string.
___

See the examples below for further clarification!


[Examples]

___
how_mega_is_it(54) ➞ "not a mega milestone"

how_mega_is_it(143) ➞ "MEGA milestone"

how_mega_is_it(1000) ➞ "MEGA MEGA milestone"

how_mega_is_it(9999.9) ➞ "MEGA MEGA milestone"

how_mega_is_it(10000) ➞ "MEGA MEGA MEGA milestone"
_____



[Notes]

___
*) Large negative numbers can also be considered as MEGA, so use the absolute values.
*) You can expect decimal numbers as well as whole numbers.
___



[formatting] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
round()
https://www.geeksforgeeks.org/round-function-python/
Rounds off to the given number of digits and returns the floating point number, if no number of digits is provided for round off, it rounds off the number to the neares …
_________
_________
Python abs()
https://www.programiz.com/python-programming/methods/built-in/abs
Returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.
_________

"""
#Your code should go here:

