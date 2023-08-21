/*
####  Super Reduced String  ####

Steve has a string of lowercase characters in range ascii[["a".."z"]]. He wants to reduce the string to its shortest length by doing a series of operations. In each operation, he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.
Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, return "Empty String".


[Case]

___
superReducedString("aaabccddd") ➞ "abd"
_____

Explanation:
___
"aaabccddd" -> "abccddd" -> "abddd" -> "abd"
_____



[Examples]

___
superReducedString("cccxllyyy") ➞ "cxy"

superReducedString("aa") ➞ "Empty String"

superReducedString("baab") ➞ "Empty String"

superReducedString("fghiiijkllmnnno") ➞ "fghijkmno"

superReducedString("chklssstt") ➞ "chkls"
_____



[Notes]

N/A


[algorithms] [regex] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

