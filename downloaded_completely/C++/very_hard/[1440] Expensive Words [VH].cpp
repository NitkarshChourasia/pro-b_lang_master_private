/*
####  Expensive Words  ####

Each letter in a sentence is worth its position in the alphabet (i.e. a = 1, b = 2, c = 3, etc...). However, if a word is all in UPPERCASE, the value of that word is doubled.
Create a function which returns the value of a sentence.
___
getSentenceValue("abc ABC Abc") ➞ 24
// a = 1, b = 2, c = 3

// abc = 1 + 2 + 3 = 6
// ABC = (1+2+3) * 2 = 12 (ALL letters are in uppercase)
// Abc = 1 + 2 + 3 = 6 (NOT ALL letters are in uppercase)

// 6 + 12 + 6 = 24
_____



[Examples]

___
getSentenceValue("HELLO world") ➞ 176

getSentenceValue("Edabit is LEGENDARY") ➞ 251

getSentenceValue("Her seaside sea-shelling business is really booming!") ➞ 488
_____



[Notes]

___
*) Ignore spaces and punctuation.
*) Remember that the value of a word isn't doubled unless all the letters in it are uppercase.
___



[algorithms] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

