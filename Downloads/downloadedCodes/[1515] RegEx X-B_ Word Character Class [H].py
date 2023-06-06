"""
####  RegEx X-B: Word Character Class  ####

Write the regular expression that will help us count how many div elements are there in a string. Use the character class \W in your expression.


[Example]

___
txt1 = "<div>Hello.</div><div>My name is <b>George</b>.</div>"
txt2 = "<div><h1>The Word for Today</h1><div>aardvark</div></div>"
txt3 = "<div></div>"
pattern = "yourregularexpressionhere"

len(re.findall(pattern, txt1)) ➞ 2
len(re.findall(pattern, txt2)) ➞ 2
len(re.findall(pattern, txt3)) ➞ 1
_____



[Notes]

___
*) A div element consists of an opening tag, none or some content and a closing tag. For example: <div>Hello.</div>.
*) Do not count the opening and closing tags as separate elements.
*) Opening an closing tags will be evenly paired.
*) HTML elements can be nested.
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and character classes in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[formatting] [regex] 



-------------------------------------------------------------------
[Resources]
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
Python has a built-in package called re, which can be used to work with Regular Expressions.
_________
_________
Character Classes
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Character_Classes
Distinguish kinds of characters such as, for example, distinguishing between letters and digits.
_________
_________
Shorthand Character Classes
https://www.regular-expressions.info/shorthand.html
Since certain character classes are used often, a series of shorthand character classes are available. \d is short for [0-9]. In most flavors that support Unicode, \d i …
_________
_________
Online RegEx Tester and Debugger
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

