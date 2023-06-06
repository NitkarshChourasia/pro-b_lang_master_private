"""
####  RegEx XXII: Named Groups  ####

A named capturing group will match "x" in (?P<name>x) and will store the match under the name name.
Let's see an example. To extract the United States area code from a phone number, we could use:
___
txt = "(214) 987-6482"
m = re.match("\((?P<area>\d{3})\)", txt)

m.group("area") ➞ 214
_____

Write a regular expression to match the year, month and day in a string. Store the matches in three groups named year, month and day respectively. All strings will be given in the following format YYYY-MM-DD.


[Example]

___
txt = "2020-04-18"
pattern = "yourregularexpressionhere"
m = re.search(pattern, txt)

m.group("year") ➞ "2020"
m.group("month") ➞ "04"
m.group("day") ➞ "18"
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and named capturing groups in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[formatting] [regex] 



-------------------------------------------------------------------
[Resources]
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________
_________
Named Capturing Groups
https://www.regular-expressions.info/named.html
Nearly all modern regular expression engines support numbered capturing groups and numbered backreferences. Long regular expressions with lots of groups and backreferen …
_________
_________
Python Regular Expression Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
Python Regex Cheatsheet
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

