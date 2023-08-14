"""
####  RegEx Exercise #0: Existentialism  ####

Write three regular expressions: one called "nothing" that will match only an empty string, one called "anything" that will match any string empty or not, and one called "something" that will match non-empty strings only.


[Example]

___
txt1 = ""
txt2 = "This is not an empty string."

nothing = "yourregularexpressionhere"
anything = "yourregularexpressionhere"
something = "yourregularexpressionhere"

bool(re.match(nothing, txt1)) ➞ True
bool(re.match(nothing, txt2)) ➞ False
re.findall(nothing, txt1) ➞ [""]
re.findall(nothing, txt2) ➞ []

bool(re.match(anything, txt1)) ➞ True
bool(re.match(anything, txt2)) ➞ True
re.findall(anything, txt1) ➞ [""]
re.findall(anything, txt2) ➞ ["This is not an empty string."]

bool(re.match(something, txt1)) ➞ False
bool(re.match(something, txt2)) ➞ True
re.findall(something, txt1) ➞ []
re.findall(something, txt2) ➞ ["This is not an empty string."]
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] 



-------------------------------------------------------------------
[Resources]
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
Python RegEx Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
Regular expression cheatsheet.
_________
_________
Online RegEx Tester and Debugger
https://regex101.com/
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

