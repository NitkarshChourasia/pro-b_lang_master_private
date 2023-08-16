"""
####  Decimal and Binary Palindromes  ####

A number/string is a palindrome if the digits/characters are the same when read both forward and backward. Examples include "racecar" and 12321. Given a positive number n, check if n or the binary representation of n is palindromic. Return the following:
___
*) "Decimal only." if only n is a palindrome.
*) "Binary only." if only the binary representation of n is a palindrome.
*) "Decimal and binary." if both are palindromes.
*) "Neither!" if neither are palindromes.
___



[Examples]

___
palindrome_type(1306031) ➞ "Decimal only."
# decimal = 1306031
# binary  = "100111110110110101111"

palindrome_type(427787) ➞ "Binary only."
# decimal = 427787
# binary  = "1101000011100001011"

palindrome_type(313) ➞ "Decimal and binary."
# decimal = 313
# binary  = 100111001

palindrome_type(934) ➞ "Neither!"
# decimal = 934
# binary  = "1110100110"
_____



[Notes]

Check the Resources tab for ways to convert to binary.


[numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Tutorial: Convert Binary to Decimal Python Data Types
https://www.datacamp.com/community/tutorials/python-data-type-conversion
In this tutorial, you'll tackle implicit and explicit DATA TYPE CONVERSION of primitive and non-primitive data structures with the help of code examples!
_________
_________
bin(x) Method
https://docs.python.org/3/library/functions.html#bin
Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression. If x is not a Python int object, it has to define an __index__ …
_________
_________
Python Program to Convert Decimal to Binary, Octal and Hexadecimal
https://www.programiz.com/python-programming/examples/conversion-binary-octal-hexadecimal
Learn to convert decimal to binary, octal and hexadecimal, and display it.
_________

"""
#Your code should go here:

