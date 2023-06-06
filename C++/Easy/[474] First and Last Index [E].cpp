/*
####  First and Last Index  ####

Given a word, write a function that returns the first index and the last index of a character.


[Examples]

___
charIndex("hello", "l") ➞ [2, 3]
// The first "l" has index 2, the last "l" has index 3.

charIndex("circumlocution", "c") ➞ [0, 8]
// The first "c" has index 0, the last "c" has index 8.

charIndex("happy", "h") ➞ [0, 0]
// Only one "h" exists, so the first and last index is 0.

charIndex("happy", "e") ➞ [-1, -1]
// "e" does not exist in "happy", so we return [-1, -1]
_____



[Notes]

___
*) If the character does not exist in the word, return [-1, -1].
*) If only one instance of the character exists, the first and last index will be the same.
*) Check the Resources tab for hints.
___



[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
std::string::find_last_of
http://www.cplusplus.com/reference/string/string/find_last_of/
Searches the string for the last character that matches any of the characters specified in its arguments.
_________
_________
std::string::find_first_of
http://www.cplusplus.com/reference/string/string/find_first_of/
Searches the string for the first character that matches any of the characters specified in its arguments.
_________
_________
std::string::rfind
http://www.cplusplus.com/reference/string/string/rfind/
Searches the string for the last occurrence of the sequence specified by its arguments.
_________
_________
std::vector::push_back
http://www.cplusplus.com/reference/vector/vector/push_back/
Adds an element to an array.
_________

*/
//Your code should go here:

