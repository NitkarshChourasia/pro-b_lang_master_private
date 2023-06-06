"""
####  Maya Number System  ####

Maya numeral system was vigesimal (base 20) and positional: units, tens, hundreds (and so on) were read as descendant progressive powers of 20, instead of 10 like we do with our decimal system. Some examples:
___
- 39 => (1 x 20¹) + (19 x 20º)
- 815 => (2 x 20²) + (0 x 20¹) + (15 x 20º)
- 16125 => (2 x 20³) + (0 x 20²) + (6 x 20¹) + (5 x 20º)
_____

Every digit (as to say the number to be multiplied for the power of 20) was symbolized with a combination of pebbles (dots), woodsticks (lines) and shells (used for the number 0) following a base5 system. See the table below:

You must implement a function that, given a non-negative integer, returns a list of strings, with each string representing the symbolized single digit.
Symbols to use are "@" for shells, "-" for lines and "o" for dots. Dots have to be placed before the lines.


[Examples]

___
# Be careful, spaces between symbols are placed only for better readability!
# Don't use spaces in returned strings.

maya_number(39) ➞ ["o", "o o o o - - -"]

maya_number(815) ➞ ["o o", "@", "- - -"]

maya_number(16125) ➞ ["o o", "@", "o -", "-"]
_____



[Notes]

___
*) Check the Resources tab for more info on Maya numerals (and Maya arithmetic).
*) All given integers are valid, no exceptions to handle.
___



[formatting] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Modulo Operator and Floor Division
https://blog.tecladocode.com/pythons-modulo-operator-and-floor-division/
Learn about the some less well-known operators in Python: modulo and floor division—as well as how they interact with each other and how they're related!
_________
_________
Maya Number System and Mathematics
https://mayaarchaeologist.co.uk/2016/12/28/maya-numbers/
Ancient Maya arithmetic and numeration system, with its Dot-and-Bar notation and concept of zero, is a fascinating topic. In this article, we will explain how to read t …
_________
_________
Modular Arithmetic
https://en.wikipedia.org/wiki/Modular_arithmetic
In mathematics, modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" when reaching a certain value—the modulus (plural moduli). The mo …
_________

"""
#Your code should go here:

