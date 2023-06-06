"""
####  RegEx XX: Capturing Groups  ####

A Capturing Group will match the characters or expressions within the parenthesis (). The matches will also be stored, and can be backreferenced by a backlash followed by its number. For example, \1 will access the first capturing group that appears in the expression.
___
txt1 = "foo, you are such a foo"
txt2 = "foo, you are such a bar"
txt3 = "bar, you are such a bar"
txt4 = "bar, you are such a foo"
pattern = r"(\w+),.*\1"

bool(re.match(pattern, txt1)) ➞ True
bool(re.match(pattern, txt2)) ➞ False
bool(re.match(pattern, txt3)) ➞ True
bool(re.match(pattern, txt4)) ➞ False
_____

Capturing groups are often used along with quantifiers. Quantifiers will use the capturing group as a whole.
___
re.findall("(go)+", "gogogo") ➞ ["gogogo"]
_____

Write a regular expression to match MAC-addresses. MAC-addresses consists of 6 two-digits hexadecimal numbers separated by a colon. Use a capturing group in your expression.
___
txt = "01:32:54:67:89:AB "
pattern = "yourregularexpressionhere"

bool(re.match(pattern, txt)) ➞ True
_____

Warning: the function re.findall() will output any capturing groups separately. If you don't want re.findall() to output a capture group, consider using non-capturing groups. Non capturing groups are formatted (?:x), where "x" is the character or expression you want to match but not capture. Non capturing groups won't be remembered and can't be accessed later in your expression.


[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and capturing groups in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[formatting] [regex] 



-------------------------------------------------------------------
[Resources]
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
Python Regular Expression Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
Python RegEx Cheatsheet
_________
_________
Parentheses for Grouping and Capturing
https://www.regular-expressions.info/brackets.html
By placing part of a regular expression inside round brackets or parentheses, you can group that part of the regular expression together. This allows you to apply a qua …
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________

"""
#Your code should go here:

