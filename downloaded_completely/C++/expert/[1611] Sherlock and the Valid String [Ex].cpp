/*
####  Sherlock and the Valid String  ####

Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just one character at one index in the string s, and the remaining characters will occur the same number of times.
Given a string, determine if it is valid. If so, return "YES", otherwise return "NO".
___
s= abc
// This is a valid string because frequencies are: {a: 1, b: 1, c: 1}

s = abcc
// This is a valid string because we can remove one c and have one
// of each character in the remaining string.

s = abccc
// This string is not valid as we can only remove one occurrence of c.
// That leaves character frequencies of: {a: 1, b: 1, c: 2}
_____



[Examples]

___
isValid("aabbcd") ➞ "NO"

isValid("aabbccddeefghi") ➞ "NO"

isValid("abcdefghhgfedecba") ➞ "YES"
_____



[Notes]

N/A


[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regex Tutorial
https://www.softwaretestinghelp.com/regex-in-cpp/
Regular Expression or regexes or regexp as they are commonly called are used to represent a particular pattern of string or text. Regexes are often used to denote a sta …
_________

*/
//Your code should go here:

