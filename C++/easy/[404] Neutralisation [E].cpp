/*
####  Neutralisation  ####

Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:
___
*) When positives and positives interact, they remain positive.
*) When negatives and negatives interact, they remain negative.
*) But when negatives and positives interact, they become neutral, and are shown as the number 0.
___



[Worked Example]

___
neutralise("+-+", "+--") ➞ "+-0"
// Compare the first characters of each string, then the next in turn.
// "+" against a "+" returns another "+".
// "-" against a "-" returns another "-".
// "+" against a "-" returns "0".
// Return the string of characters.
_____



[Examples]

___
neutralise("--++--", "++--++") ➞ "000000"

neutralise("-+-+-+", "-+-+-+") ➞ "-+-+-+"

neutralise("-++-", "-+-+") ➞ "-+00"
_____



[Notes]

The two strings will be the same length.


[conditions] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

