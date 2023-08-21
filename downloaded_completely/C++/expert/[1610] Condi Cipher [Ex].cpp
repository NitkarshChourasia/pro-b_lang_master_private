/*
####  Condi Cipher  ####

In Condi Cipher, encoding is done by shifting a string of messages in correspondence with a given key in the plaintext.
Create a function that takes three arguments, key, shift and message, and returns the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "on.,"
shift = 10
key = "cryptogram"

condiCipher(message, key, shift) ➞ "jx.,"
_____

Step 1: Remove duplicate alphabets of the key. Rearrange alphabets from A-Z, such that the keyword appears first, followed by the rest of the alphabets in the usual order.
___
c r y p t o g a m b d e f h i j k l n q s u v w x z
_____

Step 2: Starting from 1, assign numbers to the letters:
___
1  2  3  4  5  6  7  8  9  10 11 12 13
c  r  y  p  t  o  g  a  m  b  d  e  f 
14 15 16 17 18 19 20 21 22 23 24 25 26
h  i  j  k  l  n  q  s  u  v  w  x  z
_____

Step 3: Replace each alphabet of the message with the letter in the modified key shifter by a constant positive number shift (wrapping is required if the shift is greater than key size):
___
   'o' = 'j'
// 'j' is 10 places right to 'o'
_____

Step 4: Use the position of the previous letter as the number of places to move to encode the next plaintext number. If you have just encoded an 'o' (position 6), and you now want to encode 'n', then you have to move 6 places to the right from 'n' which brings you to 'x'.
___
   'n' = 'x'
// 'x' is 6 places right to 'n'
// keep other characters in same order

eMessage = "jx.,"
_____

See the below examples for a better understanding:


[Examples]

___
condiCipher("on.,", "cryptogam", 10) ➞ "jx.,"

condiCipher("mubashir", "airforce", 6) ➞ "ugrdtfko"

condiCipher("matt", "edabit", 2) ➞ "opgk"
_____



[Notes]

N/A


[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::string::erase
http://www.cplusplus.com/reference/string/string/erase/
Erases part of the string, reducing its length.
_________
_________
std::string::find
http://www.cplusplus.com/reference/string/string/find/
Searches the string for the first occurrence of the sequence specified by its arguments.
_________
_________
std::string::length
http://www.cplusplus.com/reference/string/string/length/
Returns the length of the string, in terms of bytes. This is the number of actual bytes that conform the contents of the string, which is not necessarily equal to its s …
_________
_________
std::string::insert
http://www.cplusplus.com/reference/string/string/insert/
Inserts additional characters into the string right before the character indicated by pos (or p).
_________
_________
String Concatenation
https://www.w3schools.com/cpp/cpp_strings_concat.asp
The + operator can be used between strings to add them together to make a new string. This is called concatenation.
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Get character in string Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a ch …
_________

*/
//Your code should go here:

