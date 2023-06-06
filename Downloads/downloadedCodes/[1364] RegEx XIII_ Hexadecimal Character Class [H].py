"""
####  RegEx XIII: Hexadecimal Character Class  ####

You might get text that looks like it's all English characters but it very well may not be: pànts != pants
To ensure that you only get the characters you want in a string you will need to use the character classes that accept hexadecimal digits.
Write a regular expression that will match the word "edabit". Use the hexadecimal character classes \x or \u in your expression.
You are not allowed to use any of the following characters: \w, \W, \d, \D, \t, \T, \S, \c, ., [, ] as well as any of the letters in the word edabit.


[Example]

___
txt = "edabit"
pattern = "yourregularexpressionhere"

bool(re.match("^{}$".format(pattern), txt)) ➞ True
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) You might want to use a raw string for this challenge.
*) Find more info on RegEx and character classes in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[formatting] [regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
To Remove Unicode Characters From a String With a Regular Expression
https://www.kite.com/python/answers/how-to-remove-specific-unicode-characters-from-a-string-with-a-regular-expression-in-python
Unicode characters are represented by code points. Removing specified Unicode characters results in a new string with the Unicode characters removed. For example, remov …
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
ord() Method
https://www.geeksforgeeks.org/ord-function-python/
Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte whe …
_________
_________
Text to Hex Converter
https://www.browserling.com/tools/text-to-hex
Useful, free online tool that converts plain text to hex string. No ads, nonsense or garbage, just a text to hex converter. Press button, get result.
_________
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). However, Unicode strings and 8-bit strings cannot be mixed: that …
_________
_________
Python Raw String
https://www.journaldev.com/23598/python-raw-string
Python raw string is created by prefixing a string literal with ‘r’ or ‘R’. Python raw string treats backslash (\) as a literal character. This is useful when we want t …
_________

"""
#Your code should go here:

