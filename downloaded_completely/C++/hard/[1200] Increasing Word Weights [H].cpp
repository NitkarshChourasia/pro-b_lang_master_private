/*
####  Increasing Word Weights  ####

The weight of an English word can be calculated by summing the ASCII code point for each character in the word, excluding any punctuation:
___
"Wouldn't" = 87 + 111 + 117 + 108 + 100 + 110 + 116 = 749
_____

Write a function that takes a sentence as a string, returning true if all word weights increase for each word in the sentence, and false if any word weight decreases or remains the same.


[Examples]

___
increasingWordWeights("Why not try?") ➞ true
// 312 -> 337 -> 351 (weights increase)

increasingWordWeights("All other roads.") ➞ false
// 281 -> 546 -> 537 (537 is less than 546)
_____



[Notes]

N/A


[arrays] [language_fundamentals] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
ASCII Binary Character Table
http://sticksandstones.kstrom.com/appen.html
ASCII binary character table.
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

