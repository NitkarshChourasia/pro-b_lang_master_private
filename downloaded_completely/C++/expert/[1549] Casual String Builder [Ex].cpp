/*
####  Casual String Builder  ####

The function is given a string with some square brackets in it. You need to build the outcome string using the rule: k[substring] is replaced by the substring inside the square brackets being repeated exactly k times.


[Examples]

___
stringBuilder("3[a]2[bc]") ➞ "aaabcbc"

stringBuilder("3[a2[c]]") ➞ "accaccacc"

stringBuilder("2[abc]3[cd]ef") ➞ "abcabccdcdcdef"
_____



[Notes]

k is a positive integer.


[conditions] [formatting] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after position …
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i. …
_________

*/
//Your code should go here:

