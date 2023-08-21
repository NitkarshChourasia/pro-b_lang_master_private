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
validatePassword("P1zz@") ➞ false
// Too short.

validatePassword("iLoveYou") ➞ false
// Missing a number.

validatePassword("Fhg93@") ➞ true
// OK!
_____



[Notes]

N/A


[conditions] [regex] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Regex Specific Password Restrictions
https://stackoverflow.com/questions/39709887/regex-specific-password-restrictions
I need to validate password to fulfill at least three combinations of these rules: Upper case, lower case, number, special char The password also needs to be at least 8 …
_________

*/
//Your code should go here:

