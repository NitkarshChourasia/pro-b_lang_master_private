"""
####  Recursion: Left Shift By Powers of Two  ####

The left shift operation is similar to multiplication by powers of two, thus, the process is repetitive and can be done recursively.
Sample calculation using the left shift operator (<<):
___
10 << 3 = 10 * 2^3 = 10 * 8 = 80
-32 << 2 = -32 * 2^2 = -32 * 4 = -128
5 << 2 = 5 * 2^2 = 5 * 4 = 20
_____

Write a recursive function that mimics (without the use of <<) the left shift operator and returns the result from the two given integers.


[Examples]

___
shift_to_left(5, 2) ➞ 20

shift_to_left(10, 3) ➞ 80

shift_to_left(-32, 2) ➞ -128

shift_to_left(-6, 5) ➞ -192

shift_to_left(12, 4) ➞ 192

shift_to_left(46, 6) ➞ 2944
_____



[Notes]

___
*) There will be no negative values for the second parameter y.
*) This challenge is more like recreating of the left shift operation, thus, the use of the operator directly is prohibited.
*) You are expected to solve this challenge via recursion.
*) An iterative version of this challenge can be found via this link.
___



[bit_operations] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Bitwise Operators
https://wiki.python.org/moin/BitwiseOperators
All of these operators share something in common -- they are "bitwise" operators. That is, they operate on numbers (normally), but instead of treating that number as if …
_________

"""
#Your code should go here:

