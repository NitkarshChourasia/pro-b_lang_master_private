/*
####  Hamming Code  ####

The Hamming Code is used to correct errors in data transmissions. Create a function that takes a string containing the message and returns an encoded message using hamming code.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
hammingCode("hey") ➞
"000111111000111000000000000111111000000111000111000111111111111000000111"
_____

Step 1: Convert every character to its ASCII value:
___
h, e, y = 104, 101, 121
_____

Step 2: Convert ASCII values to 8-bit binary:
___
104, 101, 121 = 01101000, 01100101, 01111001
_____

Step 3: Triple every bit:
___
01101000, 01100101, 01111001 =

000111111000111000000000, 000111111000000111000111, 000111111111111000000111
_____

Step 4: Concatenate the result:
___
"000111111000111000000000000111111000000111000111000111111111111000000111"
_____

See the below examples for a better understanding:


[Examples]

___
hammingCode("hey") ➞
"000111111000111000000000000111111000000111000111000111111111111000000111"

hammingCode("mubashir") ➞
"000111111000111111000111000111111111000111000111000111111000000000111000000111111000000000000111000111111111000000111111000111111000111000000000000111111000111000000111000111111111000000111000"

hammingCode("matt") ➞
"000111111000111111000111000111111000000000000111000111111111000111000000000111111111000111000000"
_____



[Notes]

N/A


[cryptography] [logic] [numbers] [strings] 



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
ASCII - Binary Character Table
http://sticksandstones.kstrom.com/appen.html
ASCII - Binary Character Table
_________
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________

*/
//Your code should go here:

