"""
####  RegEx III: Boundary Assertions  ####

Write a regular expression that ensures the word "end" is inside of another word (e.g. "bending"). You must use RegEx boundary assertions. Non-word characters such as !, ?, etc. cannot be boundaries.


[Examples]

___
pattern = "yourregularexpressionhere"

bool(re.search(pattern, "The end of the story.")) ➞ False
bool(re.search(pattern, "Endings are pointless.")) ➞ False
bool(re.search(pattern, "Let"s send!")) ➞ False
bool(re.search(pattern, "We viewed the rendering at the end.")) ➞ True
bool(re.search(pattern, "Sometimes bending the rules is good.")) ➞ True
_____



[Notes]

___
*) You cannot use \w, *, . or + in your expression.
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and boundary assertions in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[formatting] [regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regex Boundaries and Delimiters—Standard and Advanced
https://www.rexegg.com/regex-boundaries.html
Although this page starts with the regex word boundary \b, it aims to go far beyond: it will also introduce less-known boundaries, as well as explain how to make your o …
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
Python has a built-in package called re, which can be used to work with Regular Expressions.
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________

"""
#Your code should go here:

