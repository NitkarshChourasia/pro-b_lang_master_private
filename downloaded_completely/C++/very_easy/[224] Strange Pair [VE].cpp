/*
####  Strange Pair  ####

A pair of strings form a strange pair if both of the following are true:
___
*) The 1st string's first letter = 2nd string's last letter.
*) The 1st string's last letter = 2nd string's first letter.
___

Create a function that returns true if a pair of strings constitutes a strange pair, and false otherwise.


[Examples]

___
isStrangePair("ratio", "orator") ➞ true
// "ratio" ends with "o" and "orator" starts with "o".
// "ratio" starts with "r" and "orator" ends with "r".

isStrangePair("sparkling", "groups") ➞ true

isStrangePair("bush", "hubris") ➞ false

isStrangePair("", "") ➞ true
_____



[Notes]

It should work on a pair of empty strings (they trivially share nothing).


[language_fundamentals] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::string::front
http://www.cplusplus.com/reference/string/string/front/
This method retrieves the first value from a string.
_________
_________
std::string::back
http://www.cplusplus.com/reference/string/string/back/
Returns a reference to the last character of the string. This function shall not be called on empty strings.
_________
_________
How to get the last element of a std::string?
https://stackoverflow.com/questions/4884548/get-the-last-element-of-a-stdstring
I was wondering if there's an abbreviation or a more elegant way of getting the last character of a string like in: char lastChar = myString.at( myString.length() - 1 …
_________
_________
std::string
http://www.cplusplus.com/reference/string/string/
Strings are objects that represent sequences of characters.
_________

*/
//Your code should go here:

