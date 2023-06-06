"""
####  RegEx XI-B: Whitespace Character Class  ####

Write the regular expression that will match all whitespaces at the beginning or the end of a string so that the re.sub() fuction in the tests (you do not need to write it) will function like the .trim() method. Use the character class \s in your expression.


[Example]

___
txt1 = "    Hello World    "
txt2 = "    We need more space   "
pattern = "yourregularexpressionhere"

re.sub(pattern, "", txt1) ➞ "Hello World"
re.sub(pattern, "", txt2) ➞ "We need more space"
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and character classes in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[regex] 



-------------------------------------------------------------------
[Resources]
_________
re.sub(pattern, repl, string, count=0, flags=0)
https://docs.python.org/3/library/re.html#re.sub
Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. If the pattern isn’t found, string is ret …
_________
_________
Character Classes
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Character_Classes
Distinguish kinds of characters such as, for example, distinguishing between letters and digits.
_________
_________
Replace Strings in Python (replace, translate, re.sub, re.subn)
https://note.nkmk.me/en/python-str-replace-translate-re-sub/
Here's how to replace strings in Python.Replace substrings: replace()Specify the maximum count of replacements: countReplace multiple different substringsReplace newlin …
_________
_________
Online RegEx Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________

"""
#Your code should go here:

