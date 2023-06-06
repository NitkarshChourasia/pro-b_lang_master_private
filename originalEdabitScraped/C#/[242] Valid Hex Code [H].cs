/*
####  Valid Hex Code  ####

Create a function that determines whether a string is a valid hex code.
A hex code must begin with a pound key # and is exactly 6 characters in length. Each character must be a digit from 0-9 or an alphabetic character from A-F. All alphabetic characters may be uppercase or lowercase.


[Examples]

___
IsValidHexCode("#CD5C5C") ➞ true

IsValidHexCode("#EAECEE") ➞ true

IsValidHexCode("#eaecee") ➞ true

IsValidHexCode("#CD5C58C") ➞ false
// Length exceeds 6

IsValidHexCode("#CD5C5Z") ➞ false
// Not all alphabetic characters in A-F

IsValidHexCode("#CD5C&C") ➞ false
// Contains unacceptable character

IsValidHexCode("CD5C5C") ➞ false
// Missing #
_____



[Notes]

N/A


[regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regex.IsMatch Method
https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex.ismatch?view=netcore-3.1#System_Text_RegularExpressions_Regex_IsMatch_System_String_
Indicates whether the regular expression finds a match in the input string.
_________
_________
RegExr: Learn, Build, & Test RegEx
https://regexr.com/
RegExr is an online tool to learn, build, & test Regular Expressions (RegEx / RegExp).
_________

*/
//Your code should go here:

