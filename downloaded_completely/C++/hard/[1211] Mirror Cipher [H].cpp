/*
####  Mirror Cipher  ####

In Mirror Cipher, encoding is done by switching message characters with its mirror opposite character of the key.
Create a function that takes two arguments; a message and an optional key, and return the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "Mubashir Hassan"
key = "edabitisamazing"

mirrorCipher(message, key) ➞ "tuzishar hissid"
_____

Step 1: Replace all characters of the given message with mirror character in the key:
___
M = t
// "t" is the mirror character of "m".
// (five characters from the left and right end respectively)

u = u
// "u" is not part of the key.

b = z
// "z" is the mirror character of "b".

a = i, and so on ...
_____

Step 2: Return encoded message in lower case:
___
"tuzishar hissid"
_____

If optional key is not given, consider the whole alphabet as a default (i.e. key = "abc..z").


[Examples]

___
mirrorCipher("Mubashir Hassan", "edabitisamazing") ➞ "tuzishar hissid"

mirrorCipher("Matt MacPherson") ➞ "nzgg nzxksvihlm"

mirrorCipher("Airforce is best", "pilot") ➞ "aorfirce os besp"
_____



[Notes]

Ignore case of message and key, (e.g. "M" = "m").


[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string.
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
std::string::replace
https://www.cplusplus.com/reference/string/string/replace/
Replaces the portion of the string that begins at character pos and spans len characters (or the part of the string in the range between [i1,i2)) by new contents:
_________

*/
//Your code should go here:

