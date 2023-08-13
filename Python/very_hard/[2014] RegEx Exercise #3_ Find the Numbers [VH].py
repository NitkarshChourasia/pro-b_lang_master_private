"""
####  RegEx Exercise #3: Find the Numbers  ####

Write five regular expressions:
___
*) One called integers that will match all whole numbers, positive or negative.
*) One called floats that will match all decimal numbers, positive or negative.
*) One called positive that will match all positive numbers, whole or decimal.
*) One called negative that will match all negative numbers, whole or decimal.
*) One called numbers that will match all numbers, whole or decimal, positive or negative.
___

Details to take into account:
___
*) Fractions of 1 may or may not be preceded by a 0. All 0.5, .5, -.5 and are valid numbers.
*) Floats will have at least one decimal number. Both 4. and -3. are not valid numbers.
*) Positives numbers may or may not be preceded by a +. Both 3 and +3 are valid numbers.
*) Numbers preceded by more than one symbol or having more than one decimal point are no considered valid. All ++1, -+4, 3.3.6 are not valid numbers.
*) All numbers, valid or not, will be preceded and followed by a whitespace.
___



[Example]

___
txt = " 123.456 2 +7 -88 -.25 9.10.11 -4. +-34 -0.6 --5 "
integers = "yourregularexpressionhere"
floats = "yourregularexpressionhere"
positive = "yourregularexpressionhere"
negative = "yourregularexpressionhere"
numbers = "yourregularexpressionhere"

re.findall(integers, txt) ➞ ["2", "+7", "-88"]
re.findall(floats, txt) ➞ ["123.456", "-.25", "-0.6"]
re.findall(positive, txt) ➞ ["123.456", "2", "+7"]
re.findall(negative, txt) ➞ ["-88", "-.25", "-0.6"]
re.findall(numbers, txt) ➞ ["123.456", "2", "+7", "-88", "-.25", "-0.6"]
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) If you get stuck, check Comments for some helpful hints.
*) Find more info on RegEx in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] 



-------------------------------------------------------------------
[Resources]
_________
Online RegEx Tester and Debugger
https://regex101.com/
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________
_________
Python RegEx Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
Regular expression cheatsheet.
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________

"""
#Your code should go here:

