"""
####  RegEx XVII: Quantifiers  ####

Quantifiers indicate numbers of characters or expressions to match.
x* matches the preceding item "x" 0 or more times:
___
re.findall("bo*", "A ghost boooooed") ➞ ["booooo"]
_____

x+ matches the preceding item "x" 1 or more times. Equivalent to {1,}:
___
re.findall("a+", "caaaaaaandy") ➞ ["aaaaaa"]
_____

x? matches the preceding item "x" 0 or 1 times. If used immediately after any of the quantifiers *, +, ?, or {}, makes the quantifier lazy (matching the minimum number of times), as opposed to the default, which is greedy (matching the maximum number of times):
___
re.findall("e?le?", "angle") ➞ ["le"]
re.findall("e?le?", "angel") ➞ ["el"]
_____

Write the regular expression that will match only the street. You must use a quantifier in your expression.


[Example]

___
txt = "Harry Potter, 4 Privet Drive, Little Whinging, Surrey"
pattern = "yourregularexpressionhere"

re.findall(pattern, txt) ➞ ["4 Privet Drive"]
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx and quantifiers in Resources.
*) You can find all the challenges of this series in my Basic RegEx collection.
___



[formatting] [regex] 



-------------------------------------------------------------------
[Resources]
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________
_________
Online Regex Tester and Debugger
https://regex101.com
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________
_________
Regular Expressions Reference: Quantifiers
https://www.regular-expressions.info/refrepeat.html
JGsoft .NET Java Perl PCRE PCRE2 PHP Delphi R JavaScript VBScript XRegExp Python Ruby std::regex Boost Tcl ARE POSIX BRE POSIX ERE GNU BRE GNU ERE …
_________
_________
Python RegEx
https://www.w3schools.com/python/python_regex.asp
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.
_________
_________
Python Regular Expression Cheatsheet
https://www.debuggex.com/cheatsheet/regex/python
RegEx Cheatsheet
_________

"""
#Your code should go here:

