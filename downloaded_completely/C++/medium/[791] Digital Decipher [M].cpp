/*
####  Digital Decipher  ####

In Digital Decipher, decoding is done by the simple subtraction of numbers in the key and the corresponding characters on a given array. You may want to solve this challenge before proceeding further.
Create a function that takes two arguments; a positive integer and an array of integers and returns a decoded message as string.
Assign a unique number to each letter of the alphabet.
___
 a  b  c  d  e  f  g  h  i  j  k  l  m
 1  2  3  4  5  6  7  8  9  10 11 12 13
 n  o  p  q  r  s  t  u  v  w  x  y  z
 14 15 16 17 18 19 20 21 22 23 24 25 26
_____

There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
eMessage = [20, 12, 18, 30, 21]
key = 1939

digitalDecipher(eMessage, key) ➞ "scout"
_____

Subtract each key digit from eMessage consecutive digits:
___
  20 12 18 30 21
-  1  9  3  9  1
 ---------------
  19  3 15 21 20
_____

Write the corresponding number against each character:
___
 s  c  o  u  t
19  3 15 21 20
_____

See the below example for a better understanding:
___
eMessage = [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
key = 1939

digitalDecipher(eMessage, key) ➞ "masterpiece"

  14 10 22 29  6 27 19 18  6  12 8
-  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  13  1 19 20  5 18 16  9  5  3  5
   m  a  s  t  e  r  p  i  e  c  e
_____



[Examples]

___
digitalDecipher([20, 12, 18, 30, 21], 1939) ➞ "scout"

digitalDecipher([14, 30, 11, 1, 20, 17, 18, 18], 1990) ➞ "mubashir"

digitalDecipher([6, 4, 1, 3, 9, 20], 100) ➞ "edabit"
_____



[Notes]

N/A


[algorithms] [cryptography] [logic] 



-------------------------------------------------------------------
[Resources]
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Returns a string with the representation of val. The format used is the same that printf would print for the corresponding type.
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

*/
//Your code should go here:

