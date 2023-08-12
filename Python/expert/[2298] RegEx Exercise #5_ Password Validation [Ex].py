"""
####  RegEx Exercise #5: Password Validation  ####

Write three regular expressions that will be passed to re.match() in order to test a password strength:
___
*) One called invalid that will match a password if it's shorter than 6 characters or longer than 30 characters, if it contains any disallowed characters, or if it does not contain at least one character from each category.
*) One called weak that will match a valid password that is either between 6 and 15 characters long or contains less than three characters from each category.
*) One called strong that will match a valid password between 16 and 30 characters long and containing at least three character from each category.
___



[Categories]

___
*) Lowercase: all lowercase letters from "a" to "z".
*) Uppercase: all uppercase letters from "A" to "Z".
*) Numbers: all digits from 0 to 9.
*) Symbols: all of the following symbols !"#$%&'()*+,-./:;<=>?@[\]^_\{|}
___



[Disallowed Characters]

Spaces, tabs, line breaks and any other character that doesn't belong in one of the four categories.


[Example]

___
# There are four invalid, four weak and four strong passwords (in that order).

passwords = [
    r'a3%Z',
    r'qwerty123456666666666666666666',
    r'sjfajfewjrjiodjfsrw0998(*(8q9432-4dfjsoijfj3))',
    r'this is an   invalid password',
    r'3d/-\b1T',
    r'This1s4VeryVeryl0n6Pa$$word',
    r'AAaa11&&',
    r'yFtZaqR%eN3nsu8VvxqK!LDfxbCnj',
    r'S*=7v!7rM5k!H+)@',
    r'H#4qq2_j[T|R!(7:;.aT',
    r'AP6&Ju~=ec<?"zj#8frDq=\3{%^P$',
    r"1111aaaaA^AA;;;1111aaaaAAAA;;'"
]

invalid = "yourregularexpressionhere"
weak = "yourregularexpressionhere"
strong = "yourregularexpressionhere"

[bool(re.match(invalid, i)) for i in passwords] ➞ [True, True, True, True, False, False, False, False, False, False, False, False]
[bool(re.match(weak, i)) for i in passwords] ➞ [False, False, False, False, True, True, True, True, False, False, False, False]
[bool(re.match(strong, i)) for i in passwords] ➞ [False, False, False, False, False, False, False, False, True, True, True, True]
_____



[Notes]

___
*) You don't need to write a function, just the pattern.
*) Do not remove import re from the code.
*) Find more info on RegEx in Resources.
*) You can find all the challenges of this series here.
___



[regex] [validation] 



-------------------------------------------------------------------
[Resources]
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
_________
re — Regular expression operations
https://docs.python.org/3/library/re.html
This module provides regular expression matching operations similar to those found in Perl.
_________
_________
Online Regex Tester and Debugger
https://regex101.com/
Online regex tester, debugger with highlighting for PHP, Python, Golang and JavaScript.
_________

"""
#Your code should go here:

