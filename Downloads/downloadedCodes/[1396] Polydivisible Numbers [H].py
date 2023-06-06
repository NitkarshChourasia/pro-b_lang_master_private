"""
####  Polydivisible Numbers  ####

Mubashir was reading about Polydivisible Numbers on Wikipedia.
In mathematics a Polydivisible Number (or magic number) is a number in a given number base with digits abcde... that has the following properties:
___
*) Its first digit a is not 0.
*) The number formed by its first two digits ab is a multiple of 2.
*) The number formed by its first three digits abc is a multiple of 3.
*) The number formed by its first four digits abcd is a multiple of 4.
*) etc.
___

Create a function which takes an integer n and returns True if the given number is a Polydivisible Number and False otherwise.


[Examples]

___
is_polydivisible(1232) ➞ True
# 1     / 1 = 1
# 12    / 2 = 6
# 123   / 3 = 41
# 1232  / 4 = 308

is_polydivisible(123220 ) ➞ False
# 1   / 1 = 1
# 12   / 2 = 6
# 123   / 3 = 41
# 1232   / 4 = 308
# 12322   / 5 = 2464.4         # Not a Whole Number
# 123220   /6 = 220536.333...  # Not a Whole Number
_____



[Notes]

N/A


[algebra] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________
_________
Type Conversion and Type Casting
https://www.programiz.com/python-programming/type-conversion-and-casting
The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type convers …
_________
_________
enumerate() Method
https://www.programiz.com/python-programming/methods/built-in/enumerate
Adds counter to an iterable and returns it (the enumerate object).
_________
_________
Polydivisible Number
https://en.wikipedia.org/wiki/Polydivisible_number#:~:text=In%20mathematics%20a%20polydivisible%20number,is%20a%20multiple%20of%203.
Is a number in a given number base with digits abcde... that has the following properties: Its first digit a is not 0. The number formed by its first two digits ab is a …
_________
_________
all() Function
https://www.w3schools.com/python/ref_func_all.asp
Returns True if all items in an iterable are true, otherwise it returns False.
_________

"""
#Your code should go here:

