/*
####  Alphanumeric Restriction  ####

Create a function that returns true if the given string has any of the following:
___
*) Only letters and no numbers.
*) Only numbers and no letters.
___

If a string has both numbers and letters, or contains characters which don't fit into any category, return false


[Examples]

___
alphanumericRestriction("Bold") ➞ true

alphanumericRestriction("123454321") ➞ true

alphanumericRestriction("H3LL0") ➞ false

alphanumericRestriction("ed@bit") ➞ false
_____



[Notes]

Any string that contains spaces or is empty should return false.


[language_fundamentals] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
isdigit()
https://www.programiz.com/cpp-programming/library-function/cctype/isdigit
Checks if the given character is a digit or not.
_________

*/
//Your code should go here:

