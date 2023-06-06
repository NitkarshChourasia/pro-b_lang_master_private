/*
####  Parity Bit Validation  ####

Parity bits are used as very simple checksum to ensure that binary data isn't corrupted during transit. Here's how they work:
___
*) If a binary string has an odd number of 1s, the parity bit is a 1.
*) If a binary string has an even number of 1s, the parity bit is a 0.
*) The parity bit is appended to the end of the binary string.
___

Create a function that validates whether a binary string is valid, using parity bits.


[Worked Example]

___
validateBinary("10110010") ➞ true

// The last digit is the parity bit.
// 0 is the last digit.
// 0 means that there should be an even number of 1s.
// There are four 1s.
// Return True.
_____



[Examples]

___
validateBinary("00101101") ➞ true

validateBinary("11000000") ➞ true

validateBinary("11000001") ➞ false
_____



[Notes]

___
*) All inputs will be a byte long (8 characters).
*) You can find another parity bit involved challenge here!
___



[numbers] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________
_________
std::string::size
http://www.cplusplus.com/reference/string/string/size/
Returns the length of the string, in terms of bytes. This is the number of actual bytes that conform the contents of the string, which is not necessarily equal to its …
_________
_________
Count Character Occurrences in a String
https://stackoverflow.com/questions/3867890/count-character-occurrences-in-a-string-in-c
How can I count the number of "_" in a string like "bla_bla_blabla_bla"?
_________
_________
Boolean Operators
http://www.cplusplus.com/doc/boolean/
A bit is the minimum amount of information that we can imagine, since it only stores either value 1 or 0, which represents either YES or NO, activated or deactivated, t …
_________

*/
//Your code should go here:

