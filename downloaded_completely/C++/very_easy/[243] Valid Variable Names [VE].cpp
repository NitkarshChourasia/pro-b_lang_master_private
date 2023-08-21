/*
####  Valid Variable Names  ####

When creating variables, the variable name must always start with a letter and cannot contain spaces, though numbers and underscores are allowed to be contained in it also.
Create a function which returns true if a given variable name is valid, otherwise return false.


[Examples]

___
variableValid("result") ➞ true

variableValid("odd_nums") ➞ true

variableValid("2TimesN") ➞ false
_____



[Notes]

___
*) Inputs are given as strings.
*) Variable names with spaces are not allowed.
*) Although this question may seem like otherwise, you can't actually assign words with quotes around them as variables.
___



[conditions] [regex] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments.
_________
_________
isalpha
http://www.cplusplus.com/reference/cctype/isalpha/
Checks whether c is an alphabetic letter.
_________
_________
std::basic_string<CharT,Traits,Allocator>::npos
https://en.cppreference.com/w/cpp/string/basic_string/npos
Returns the position of the found string, but if it doesn't find the given string, it returns string::npos, where npos means no position.
_________
_________
isspace()
http://www.cplusplus.com/reference/cctype/isspace/
Checks whether c is a white-space character.
_________
_________
isdigit
http://www.cplusplus.com/reference/cctype/isdigit/
Checks whether c is a decimal digit character.
_________

*/
//Your code should go here:

