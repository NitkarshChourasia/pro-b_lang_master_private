/*
####  Password Validation  ####

Create a function that validates a password to conform to the following rules:
___
*) Length between 6 and 24 characters.
*) At least one uppercase letter (A-Z).
*) At least one lowercase letter (a-z).
*) At least one digit (0-9).
*) Maximum of 2 repeated characters.
"aa" is OK 👍
"aaa" is NOT OK 👎
*) Supported special characters:
! @ # $ % ^ & * ( ) + = _ - { } [ ] : ; " ' ? < > , .
___



[Examples]

___
ValidatePassword("P1zz@") ➞ false
// Too short.

ValidatePassword("iLoveYou") ➞ false
// Missing a number.

ValidatePassword("Fhg93@") ➞ true
// OK!
_____



[Notes]

N/A


[conditions] [regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regex Class
https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex?view=netframework-4.8
Illustrates how the Regex Class works.
_________
_________
Regular Expression Language - Quick Reference
https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference
A regular expression is a pattern that the regular expression engine attempts to match in input text. A pattern consists of one or more character literals, operators, o …
_________

*/
//Your code should go here:

