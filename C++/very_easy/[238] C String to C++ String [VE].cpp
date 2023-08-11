/*
####  C String to C++ String  ####

This is a C string:
___
{"H", "e", "l", "l", "o", "!", "\0"}
_____

In C, you could also type "Hello!" when declaring a char [n+1] type. N is the size of the string "Hello!", but +1 is there because of "\0". In C++, it looks like "Hello!". The "\0" char is the end of a string, and it isn't written in the string.
Create a function that will return a C++ string from the given C string.


[Examples]

___
cppStr({"H", "i", "!", "\0"}) ➞ "Hi!"

cppStr({"H", "e", "l", "l", "o", "!", "\0"}) ➞ "Hello!"

cppStr({"J", "A", "V", "a", "\0"}) ➞ "JAVa"
_____



[Notes]

N/A


[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
std::vector::begin
http://www.cplusplus.com/reference/vector/vector/begin/
Returns an iterator pointing to the first element in the vector.
_________
_________
Convert Character Array to String in C++
https://www.geeksforgeeks.org/convert-character-array-to-string-in-c/
This article shows how to convert a character array to a string in C++. The std::string in c++ has a lot of inbuilt functions which makes implementation much easier tha …
_________
_________
std::tolower
http://www.cplusplus.com/reference/locale/tolower/
Converts parameter c to its lowercase equivalent if c is an uppercase letter and has a lowercase equivalent, as determined by the ctype facet of locale loc. If no such …
_________

*/
//Your code should go here:

