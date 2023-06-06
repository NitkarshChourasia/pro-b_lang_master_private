/*
####  Basic E-Mail Validation  ####

Create a function that accepts a string, checks if it's a valid email address and returns either true or false, depending on the evaluation.
___
*) The string must contain an @ character.
*) The string must contain a . character.
*) The @ must have at least one character in front of it.
e.g. "e@edabit.com" is valid while "@edabit.com" is invalid.
*) The . and the @ must be in the appropriate places.
e.g. "hello.email@com" is invalid while "john.smith@email.com" is valid.
___

If the string passes these tests, it's considered a valid email address.


[Examples]

___
validateEmail("@gmail.com") ➞ false

validateEmail("hello.gmail@com") ➞ false

validateEmail("gmail") ➞ false

validateEmail("hello@gmail") ➞ false

validateEmail("hello@edabit.com") ➞ true
_____



[Notes]

___
*) Check the Tests tab to see exactly what's being evaluated.
*) You can solve this challenge with RegEx, but it's intended to be solved with logic.
*) Solutions using RegEx will be accepted but frowned upon :(
___



[logic] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
<regex>
http://www.cplusplus.com/reference/regex/
Regular expressions are a standardized way to express patterns to be matched against sequences of characters.
_________

*/
//Your code should go here:

