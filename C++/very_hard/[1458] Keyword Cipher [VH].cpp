/*
####  Keyword Cipher  ####

A Keyword Cipher is a monoalphabetic cipher which uses a keyword to provide encryption on given string of message.
Create a function that takes two arguments: a string message and a string key, and returns an encoded message.
For the encryption key, the keyword is placed at the beginning, followed by the rest of the characters in the alphabet in order (in other words, with the keyword characters removed):
___
A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z
K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z
_____

The encrypted message substitutes each plaintext character with the encryption key character in the corresponding position.
Return the given message encrypted against the key:
___
eMessage = "KEYABC"
// A = K, B = E, C = Y, H = A, I = B, J = C
_____



[Examples]

___
keywordCipher("keyword", "abchij") ➞ "keyabc"

keywordCipher("purplepineapple", "abc") ➞ "pur"

keywordCipher("mubashir", "edabit") ➞ "samucq"
_____



[Notes]

___
*) Don't forget to remove duplicates after concatenating string with keyword.
*) Non-alphabetic characters must be left as they are.
___



[cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::erase
http://www.cplusplus.com/reference/string/string/erase/
The others return an iterator referring to the character that now occupies the position of the first character erased, or string::end if no such character exists.
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments. When pos is specified, the search only includes characters at or after positio …
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

