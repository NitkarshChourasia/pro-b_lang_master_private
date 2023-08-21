/*
####  Longest Abecedarian Word  ####

An abecedarian word is a word where all of its letters are arranged in alphabetical order. Examples of these words include:
___
*) Empty
*) Forty
*) Almost
___

Given an array of words, create a function which returns the longest abecedarian word. If no word in an array matches the criterea, return an empty string.


[Examples]

___
longestAbecedarian(["ace", "spades", "hearts", "clubs"]) ➞ "ace"

longestAbecedarian(["forty", "choppy", "ghost"]) ➞ "choppy"

longestAbecedarian(["one", "two", "three"]) ➞ ""
_____



[Notes]

___
*) All words will be given in lowercase.
*) If two abecedarian words have the same length, return the word which appeared first in the array.
___



[arrays] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________

*/
//Your code should go here:

