"""
####  RegEx Exercise #1: Find the Times  ####

Write a regular expression to find all the times in a string. Times will be in 24-hours format with hours and minutes and optionally seconds: hh:mm(:ss). Match only valid times.


[Example]

___
txt1 = "Breakfast at 09:00 in the room 123:456."
txt2 = "The incident took place last Wednesday at 00:56:41."
txt3 = "We will have two meetings: from 10:30 to 11:00 and from 11:45 to 11:75."
pattern = "yourregularexpressionhere"

re.findall(pattern, txt1) ➞ ["09:00"]
re.findall(pattern, txt2) ➞ ["00:56:41"]
re.findall(pattern, txt3) ➞ ["10:30", "11:00", "11:45"]
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx in Resources.
*) If you're stuck, check Comments for some hints.
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
Online RegEx Tester and Debugger
https://www.regex101.com/
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Python RegEx Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
Regular expression cheatsheet.
_________

"""
#Your code should go here:

