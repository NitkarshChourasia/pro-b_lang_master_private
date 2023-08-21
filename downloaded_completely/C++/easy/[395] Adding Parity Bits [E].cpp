/*
####  Adding Parity Bits  ####

Parity bits are used as a very simple checksum to ensure that binary data isn't corrupted during transit. Here's how they work:
___
*) If a binary string has an odd number of 1's, the parity bit is a 1.
*) If a binary string has an even number of 1's, the parity bit is a 0.
*) The parity bit is appended to the end of the binary string.
___

Create a function that adds the correct parity bit to a binary string.


[Worked Example]

___
addParityBit("1011011") ➞ "10110111"

// There are five 1's.
// Since five is odd, the parity bit should be a 1.
// Add the parity bit to the end of the string.
// Return the result.
_____



[Examples]

___
addParityBit("0010110") ➞ "00101101"

addParityBit("1100000") ➞ "11000000"
_____



[Notes]

All inputs will be 7-bits long (so that the parity bit makes it a full byte).


[logic] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
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

*/
//Your code should go here:

