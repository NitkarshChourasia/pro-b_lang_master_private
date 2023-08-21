/*
####  Neighboring Letters  ####

Create a function that takes a string and checks if every single character is preceded and followed by a character adjacent to it in the english alphabet.
Example: "b" should be preceded and followed by ether "a" or "c" (abc || cba || aba || cbc == true but abf || zbc == false).


[Examples]

___
neighboring("aba") ➞ true

neighboring("abcdedcba") ➞ true

neighboring("efghihfe") ➞ false

neighboring("abc") ➞ true

neighboring("qrstuv") ➞ true

neighboring("mnopqrstsrqponm") ➞ true
_____



[Notes]

All test cases will consist of lower case letters only.


[formatting] [higher_order_functions] [language_fundamentals] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

