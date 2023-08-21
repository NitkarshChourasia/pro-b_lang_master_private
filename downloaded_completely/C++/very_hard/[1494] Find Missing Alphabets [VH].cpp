/*
####  Find Missing Alphabets  ####

Create a function that takes a string str containing only letters from a to z in lowercase and returns the missing letter(s) in alphabetical order a-z.
___
*) A set of letters is given by abcdefghijklmnopqrstuvwxyz.
*) Two sets of alphabets means two or more alphabets.
___



[Examples]

___
missingAlphabets("abcdefghijklmnopqrstuvwxy") ➞ "z"
// "z" is missing.

missingAlphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy") ➞ "zz"
// Given string has a set of two alphabets so output will be "zz"

missingAlphabets("edabit") ➞ "cfghjklmnopqrsuvwxyz"
_____



[Notes]

If the string contains all letters from a-z, return an empty string "".


[logic] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

