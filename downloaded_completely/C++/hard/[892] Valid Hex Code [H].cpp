/*
####  Valid Hex Code  ####

Create a function that determines whether a string is a valid hex code.
A hex code must begin with a pound key # and is exactly 6 characters in length. Each character must be a digit from 0-9 or an alphabetic character from A-F. All alphabetic characters may be uppercase or lowercase.


[Examples]

___
isValidHexCode("#CD5C5C") ➞ true

isValidHexCode("#EAECEE") ➞ true

isValidHexCode("#eaecee") ➞ true

isValidHexCode("#CD5C58C") ➞ false
// Length exceeds 6

isValidHexCode("#CD5C5Z") ➞ false
// Not all alphabetic characters in A-F

isValidHexCode("#CD5C&C") ➞ false
// Contains unacceptable character

isValidHexCode("CD5C5C") ➞ false
// Missing #
_____



[Notes]

N/A


[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
isxdigit
http://www.cplusplus.com/reference/cctype/isxdigit/
Checks whether c is a hexdecimal digit character.
_________
_________
ispunct
http://www.cplusplus.com/reference/cctype/ispunct/
Check if a character is a punctuation mark.
_________
_________
RegExr: Learn, Build, & Test RegEx
https://regexr.com/
RegExr is an online tool to learn, build, & test Regular Expressions (RegEx / RegExp).
_________

*/
//Your code should go here:

