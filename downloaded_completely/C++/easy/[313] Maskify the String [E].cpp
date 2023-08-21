/*
####  Maskify the String  ####

Usually when you sign up for an account to buy something, your credit card number, phone number or answer to a secret question is partially obscured in some way. Since someone could look over your shoulder, you don't want that shown on your screen. Hence, the website masks these strings.
Your task is to create a function that takes a string, transforms all but the last four characters into "#" and returns the new masked string.


[Examples]

___
maskify("4556364607935616") ➞ "############5616"

maskify("64607935616") ➞ "#######5616"

maskify("1") ➞ "1"

maskify("") ➞ ""
_____



[Notes]

___
*) The maskify function must accept a string of any length.
*) An empty string should return an empty string (fourth example above).
___



[formatting] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
string::replace
http://www.cplusplus.com/reference/string/string/replace/
Replaces the portion of the string that begins at character pos and spans len characters (or the part of the string in the range between [i1,i2)) by new contents.
_________
_________
std::string
http://www.cplusplus.com/reference/string/string/
Strings are objects that represent sequences of characters.
_________
_________
<string>
http://www.cplusplus.com/reference/string/
This header introduces string types, character traits and a set of converting functions.
_________
_________
Strings
https://www.w3schools.com/cpp/cpp_strings.asp
Are used for storing text. A string variable contains a collection of characters surrounded by double quotes.
_________

*/
//Your code should go here:

