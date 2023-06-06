/*
####  Most Left Digit  ####

Write a function that takes a string as an argument and returns the left most digit in the string.


[Examples]

___
leftDigit("TrAdE2W1n95!") ➞ 2

leftDigit("V3r1ta$") ➞ 3

leftDigit("U//DertHe1nflu3nC3") ➞ 1

leftDigit("J@v@5cR1PT") ➞ 5
_____



[Notes]

___
*) Each string will have at least two numbers.
*) Return the result as an integer.
___



[numbers] [sorting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
isdigit
http://www.cplusplus.com/reference/cctype/isdigit/
Check if character is decimal digit.
_________
_________
How to convert a char to an int in C++?
https://stackoverflow.com/questions/5029840/convert-char-to-int-in-c-and-c
Depends on what you want to do: to read the value as an ascii code, you can write char a = 'a'; int ia = (int)a; /* note that the int cast is not necessary -- int ia …
_________
_________
std::find_if
http://www.cplusplus.com/reference/algorithm/find_if/?kw=find_if
Find element in range. Returns an iterator to the first element in the range [first,last) for which pred returns true. If no such element is found, the function return …
_________
_________
std::string::front
http://www.cplusplus.com/reference/string/string/front/
Returns a reference to the first character of the string.
_________

*/
//Your code should go here:

