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
Java String matches Example
https://examples.javacodegeeks.com/core-java/lang/string/java-string-matches-example/
In this example we are going to talk about matches String Class method. You can use this method to test a String against a regular expression. Testing a String against …
_________
_________
Regex
https://regexone.com/
Regular expressions are extremely useful in extracting information from text such as code, log files, spreadsheets, or even documents. And while there is a lot of theor …
_________

*/
//Your code should go here:

