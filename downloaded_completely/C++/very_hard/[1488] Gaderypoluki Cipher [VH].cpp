/*
####  Gaderypoluki Cipher  ####

Create a function that takes an encryption key (a string with an even number of characters) and a message to encrypt. Group the letters of the key by two:
___
"gaderypoluki" -> "ga de ry po lu ki"
_____

Now take the message for encryption. If the message character appears in the key, replace it with an adjacent character in the grouped version of the key. If the message character does not appear in the key, leave it as is. If the letter in the key occurs more than once, the first result is used. Create a function that takes an encryption key (a string with an even number of characters) and a message to encrypt. Group the letters of the key by two:
___
"gaderypoluki" -> "ga de ry po lu ki"
_____

Now take the message for encryption. If the message character appears in the key, replace it with an adjacent character in the grouped version of the key. If the message character does not appear in the key, leave it as is. If the letter in the key occurs more than once, the first result is used. For example: use the above key, if the letter "a" appeared in the message, it would be replaced with "g" since "g" in the adjacent letter.
Return the encrypted message.


[Examples]

___
encrypt("ab c", "abc ab") ➞ "ba cba"

encrypt("otorhinolaryngological", "My name is Paul") ➞ "Mr olme hs Plua"

encrypt("gaderypoluki", "This is an encrypted message") ➞ "Thks ks gn dncyrotde mdssgad"
_____



[Notes]

N/A
Return the encrypted message.


[Examples]

___
encrypt("ab c", "abc ab") ➞ "ba cba"

encrypt("otorhinolaryngological", "My name is Paul") ➞ "Mr olme hs Plua"

encrypt("gaderypoluki", "This is an encrypted message") ➞ "Thks ks gn dncyrotde mdssgad"
_____



[Notes]

N/A


[algorithms] [cryptography] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string.
_________

*/
//Your code should go here:

