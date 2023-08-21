/*
####  Nico Cipher  ####

In Nico Cipher, encoding is done by creating a numeric key and assigning each letter position of the message with the provided key.
Create a function that takes two arguments, key and message, and returns the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "mubashirhassan"
key = "crazy"

nicoCipher(message, key) ➞ "bmusarhiahass n"
_____

Step 1: Assign numbers to sorted letters from the key:
___
"crazy" = 23154
_____

Step 2: Assign numbers to the letters of the given message:
___
2 3 1 5 4
---------
m u b a s
h i r h a
s s a n
_____

Step 3: Sort columns as per assigned numbers:
___
1 2 3 4 5
---------
b m u s a
r h i a h
a s s   n
_____

Step 4: Return encoded message Rows-wise:
___
eMessage = "bmusarhiahass n"
_____



[Examples]

___
nicoCipher("mubashirhassan", "crazy") ➞ "bmusarhiahass n"

nicoCipher("edabitisamazing", "matt") ➞ "deabtiismaaznig "

nicoCipher("iloveher", "612345") ➞ "lovehir    e"
_____



[Notes]

Keys will have alphabets or numbers only.


[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________
_________
tolower() Method
https://www.programiz.com/cpp-programming/library-function/cctype/tolower
Converts a given character to lowercase.
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

