"""
####  Kaprekar Numbers  ####

A Kaprekar Number is a positive integer that is equal to a number formed by first squaring, then splitting and summing its two lexicographical parts:
___
*) If the quantity of digits of the squared number is even, the left and right parts will have the same length.
*) If the quantity of digits of the squared number is odd, then the right part will be the longer half, with the left part being the shorter or equal to zero if the quantity of digits is equal to 1.
___

Given a positive integer n implement a function that returns True if it's a Kaprekar number, and False if it's not.


[Examples]

___
is_kaprekar(3) ➞ False
# n² = "9"
# Left + Right = 0 + 9 = 9 ➞ 9 != 3

is_kaprekar(5) ➞ False
# n² = "25"
# Left + Right = 2 + 5 = 7 ➞ 7 != 5

is_kaprekar(297) ➞ True
# n² = "88209"
# Left + Right = 88 + 209 = 297 ➞ 297 == 297
_____



[Notes]

Trivially, 0 and 1 are Kaprekar Numbers being the only two numbers equal to their square. Any number formed only by digits equal to 9 will always be a Kaprekar Number.


[numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Kaprekar Number
https://en.wikipedia.org/wiki/Kaprekar_number
A natural number in a given number base is a p-Kaprekar number if the representation of its square in that base can be split into two parts, where the second part has d …
_________
_________
eval() Function
https://www.w3schools.com/python/ref_func_eval.asp
Evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
_________
_________
How to remove leading and trailing zeros in a string?
https://stackoverflow.com/questions/13142347/how-to-remove-leading-and-trailing-zeros-in-a-string-python
How to remove leading and trailing zeros in a string in python.
_________

"""
#Your code should go here:

