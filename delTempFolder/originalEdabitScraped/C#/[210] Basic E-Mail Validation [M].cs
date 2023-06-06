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
ValidateEmail("@gmail.com") ➞ false

ValidateEmail("hello.gmail@com") ➞ false

ValidateEmail("gmail") ➞ false

ValidateEmail("hello@gmail") ➞ false

ValidateEmail("hello@edabit.com") ➞ true
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
String Functions and Properties
https://www.completecsharptutorial.com/csharp-articles/csharp-string-function.php
In C# programming, string is another kind of data type that represents Unicode Characters. It is the alias of System.String, however, you can also write System.String i …
_________
_________
String.Substring Method (System)
https://docs.microsoft.com/en-us/dotnet/api/system.string.substring?view=netframework-4.8
Retrieves a substring from this instance. This member is overloaded. For complete information about this member, including syntax, usage, and examples, click a name …
_________
_________
Regex.Match Method
https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex.match?redirectedfrom=MSDN&view=netframework-4.8#System_Text_RegularExpressions_Regex_Match_System_String_
Searches an input string for a substring that matches a regular expression pattern and returns the first occurrence as a single Match object.
_________
_________
How to validate an email address using a regular expression?
https://stackoverflow.com/questions/201323/how-to-validate-an-email-address-using-a-regular-expression
Over the years I have slowly developed a regular expression that validates MOST email addresses correctly, assuming they don't use an IP address as the server part. I u …
_________

*/
//Your code should go here:

