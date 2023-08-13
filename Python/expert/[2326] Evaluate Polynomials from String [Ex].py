"""
####  Evaluate Polynomials from String  ####

You will be given a polynomial expression in string form. The expression will contain any of the following operations, written using standard mathematical notation for a single variable, "x", as illustrated in the examples below:
___
*) addition: x + 1
*) subtraction: x – 2
*) multiplication: 3x
*) division: x / 4
*) exponentation: x^5
*) brackets: x(x + 1)
___

Your task is to write a function that can evaluate such a polynomial for a given value of x. You will receive two arguments: the polynomial string and the input number.
If the mathematical expression contains an error, you should return "invalid".


[Examples]

___
evaluate_polynomial("x+1", 5) ➞ 6

evaluate_polynomial("5x^2", 3) ➞ 45

evaluate_polynomial("(x(x+1))/2", 4) ➞ 10

evaluate_polynomial("4(x + 3))/2", 5) ➞ "invalid"
# Invalid because parentheses not balanced.
_____



[Notes]

The string will not contain spaces.


[algebra] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Evaluate Expressions Dynamically
https://realpython.com/python-eval-function/#math-expressions
In this step-by-step tutorial, you'll learn how Python's eval() works and how to use it effectively in your programs. Additionally, you'll learn how to minimize the sec …
_________
_________
eval() Method
https://www.programiz.com/python-programming/methods/built-in/eval
Parses the expression passed to this method and runs python expression (code) within the program.
_________
_________
String replace() Method
https://www.programiz.com/python-programming/methods/string/replace
Returns a copy of the string where all occurrences of a substring is replaced with another substring.
_________
_________
Regular Expressions: Regexes in Python (Part 1)
https://realpython.com/regex-python/
In previous tutorials in this series, you've seen several different ways to compare string values with direct character-by-character comparison. In this tutorial, you'l …
_________

"""
#Your code should go here:

