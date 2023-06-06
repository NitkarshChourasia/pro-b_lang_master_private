/*
####  Digital Cipher  ####

In Digital Cipher, encoding is done by the simple addition of numbers in the key and the corresponding characters on a string input.
Create a function that takes two arguments; a positive integer and a string and returns an encoded array of integers as message.
Assign a unique number to each letter of the alphabet.
___
 a  b  c  d  e  f  g  h  i  j  k  l  m
 1  2  3  4  5  6  7  8  9  10 11 12 13
 n  o  p  q  r  s  t  u  v  w  x  y  z
 14 15 16 17 18 19 20 21 22 23 24 25 26
_____

There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "scout"
key = 1939

digitalCipher(message, key) ➞ [20, 12, 18, 30, 21]
_____

Write the corresponding number against each character:
___
 s  c  o  u  t
19  3 15 21 20
_____

Add to each obtained digit consecutive digits from the key:
___
   s  c  o  u  t
  19  3 15 21 20
 + 1  9  3  9  1
 ---------------
  20 12 18 30 21
_____

See the below example for a better understanding:
___
message = "masterpiece"
key = 1939

digitalCipher(message, key) ➞ [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]

   m  a  s  t  e  r  p  i  e  c  e
  13  1 19 20  5 18 16  9  5  3  5
+  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  14 10 22 29  6 27 19 18  6  12 8
_____



[Examples]

___
digitalCipher("scout", 1939) ➞ [20, 12, 18, 30, 21]

digitalCipher("mubashir", 1990) ➞ [14, 30, 11, 1, 20, 17, 18, 18]

digitalCipher("edabit", 100) ➞ [6, 4, 1, 3, 9, 20]
_____



[Notes]

Liked this challenge ? Let's decode your encrypted version here!!!


[algorithms] [cryptography] [logic] 



-------------------------------------------------------------------
[Resources]
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Returns a string with the representation of val.
_________
_________
std::stoi
http://www.cplusplus.com/reference/string/stoi/
Parses str interpreting its content as an integral number of the specified base, which is returned as an int value. If idx is not a null pointer, the function also set …
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

*/
//Your code should go here:

