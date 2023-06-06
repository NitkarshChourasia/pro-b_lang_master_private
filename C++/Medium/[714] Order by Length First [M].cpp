/*
####  Order by Length First  ####

Graded lexicographic order (grlex order for short) is a way of ordering words that:

For example, in grlex order:
___
*) "tray" < "trapped" since "tray" has length 4 while "trapped" has length 7.
*) "trap" < "tray" since both have length 4, but "trap" comes before "tray" in the dictionary.
___

Given an array of words, return that array in grlex order.


[Examples]

___
makeGrlex(["small", "big"]) ➞ ["big", "small"]

makeGrlex(["cat", "ran", "for", "the", "rat"]) ➞ ["cat", "for", "ran", "rat", "the"]

makeGrlex(["this", "is", "a", "small", "test"]) ➞ ["a", "is", "test", "this", "small"]
_____



[Notes]

N/A


[conditions] [math] [sorting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

