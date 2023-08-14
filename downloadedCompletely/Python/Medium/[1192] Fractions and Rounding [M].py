"""
####  Fractions and Rounding  ####

Given a fraction (given in the format "1/2" for example) and n number of decimal places, return a sentence in the following format:
"{fraction} rounded to {n} decimal places is {answer}"


[Examples]

___
frac_round("1/3", 5) ➞ "1/3 rounded to 5 decimal places is 0.33333"

frac_round("2/8", 4) ➞ "2/8 rounded to 4 decimal places is 0.2500"

frac_round("22/7", 2) ➞ "22/7 rounded to 2 decimal places is 3.14"
_____



[Notes]

___
*) Add trailing zeros if n is greater than the actual number of decimal places the fraction has (see example #2).
*) Numbers greater than one may be given as top-heavy fractions (no mixed numbers).
*) n won't be 1 because that would cause "decimal places" to be "decimal place", making the challenge more cumbersome than it needs to be.
___



[formatting] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Using % and .format() for great good!
https://pyformat.info/
Python has had awesome string formatters for many years but the documentation on them is far too theoretic and technical. With this site we try …
_________
_________
eval() Method
https://www.programiz.com/python-programming/methods/built-in/eval
Parses the expression passed to this method and runs python expression (code) within the program.
_________
_________
String Format Cookbook
https://mkaz.blog/code/python-string-format-cookbook/
Python v2.7 introduced a new string fomatting method, that is now the default in Python3. I started this string formatting cookbook as a quick reference to help me form …
_________
_________
round() Method
https://www.programiz.com/python-programming/methods/built-in/round
Returns a floating-point number rounded to the specified number of decimals.
_________

"""
#Your code should go here:

