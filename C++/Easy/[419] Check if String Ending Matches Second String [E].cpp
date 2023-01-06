/*
####  Check if String Ending Matches Second String  ####

Create a function that takes two strings and returns true if the first string ends with the second string; otherwise return false.


[Examples]

___
checkEnding("abc", "bc") ➞ true

checkEnding("abc", "d") ➞ false

checkEnding("samurai", "zi") ➞ false

checkEnding("feminine", "nine") ➞ true

checkEnding("convention", "tio") ➞ false
_____



[Notes]

All test cases are valid one word strings.


[strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::basic_string::compare
http://en.cppreference.com/w/cpp/string/basic_string/compare
Compare two strings.
_________
_________
string::back
http://www.cplusplus.com/reference/string/string/back/
Returns a reference to the last character of the string.
_________
_________
string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments.
_________
_________
<string>.substr(pos, count)
https://en.cppreference.com/w/cpp/string/basic_string/substr
Returns a substring [pos, pos+count). If the requested substring extends past the end of the string, or if count == npos, the returned substring is [pos, size()).
_________

*/
//Your code should go here:

