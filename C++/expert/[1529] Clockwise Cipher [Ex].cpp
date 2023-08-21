/*
####  Clockwise Cipher  ####

In Clockwise Cipher, encoding is done by placing message characters in the corner cells of a square and moving in a clockwise direction.
Create a function that takes an argument message, and returns the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "Mubashir Hassan"

clockwiseCipher(message) ➞ "Ms ussahr nHaaib"
_____

Step 1: Form a square large enough to fit all the message characters. Given message can fit in a 4 x 4 square.
Step 2: Starting with the top-left corner, place message characters in the corner cells moving in a clockwise direction. After the first cycle is complete, continue placing characters in the cells following the last one in its respective row/column. When the outer cells are filled, continue for the remaining inner squares:

Step 3: Return encoded message Rows-wise:
___
eMessage = "Ms ussahr nHaaib"
_____



[Example for a 5 x 5 Square]

___
[ 1  5  9 13  2]
[16 17 21 18  6]
[12 24 25 22 10]
[ 8 20 23 19 14]
[ 4 15 11  7  3]
_____



[Examples]

___
clockwiseCipher("Mubashir Hassan") ➞ "Ms ussahr nHaaib"

clockwiseCipher("Matt MacPherson") ➞ "M ParsoMc nhteat"

clockwiseCipher("Edabit is amazing") ➞ "Eisadng  tm    i   zbia a"
_____



[Notes]

___
*) Fill up any unused cells with a space character.
*) Message can contain spaces and special characters.
___



[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Vector of Vectors
https://www.geeksforgeeks.org/vector-of-vectors-in-c-stl-with-examples/
Vectors are known as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatical …
_________
_________
Ceil and Floor Functions in C++
https://www.geeksforgeeks.org/ceil-floor-functions-cpp/
In mathematics and computer science, the floor and ceiling functions map a real number to the greatest preceding or the least succeeding integer, respectively.
_________
_________
String Length
https://www.w3schools.com/cpp/cpp_strings_length.asp
To get the length of a string, use the length() function.
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

