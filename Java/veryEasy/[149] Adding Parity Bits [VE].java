/*
####  Adding Parity Bits  ####

Parity bits are used as a very simple checksum to ensure that binary data isn't corrupted during transit. Here's how they work:
___
*) If a binary string has an odd number of 1's, the parity bit is a 1.
*) If a binary string has an even number of 1's, the parity bit is a 0.
*) The parity bit is appended to the end of the binary string.
___

Create a function that adds the correct parity bit to a binary string.


[Examples]

___
addParityBit("1011011") ➞ "10110111"

// There are five 1's.
// Since five is odd, the parity bit should be a 1.
// Add the parity bit to the end of the string.
// Return the result.

addParityBit("0110000") ➞ "01100000"

addParityBit("0101101") ➞ "01011010"

addParityBit("1111111") ➞ "11111111"
_____



[Notes]

All inputs will be 7-bits long (so that the parity bit makes it a full byte).


[logic] [numbers] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to Split a String in Java
https://stackoverflow.com/questions/3481828/how-to-split-a-string-in-java
I have a string, "004-034556", that I want to split into two strings. That means the first string will contain the characters before '-', and the second string will con …
_________
_________
String split() Method
https://www.geeksforgeeks.org/split-string-java-examples/
Breaks a given string around matches of the given regular expression.
_________
_________
Count Occurrences of a Char in a String
https://www.baeldung.com/java-count-chars
Learn how to count characters with the core Java library and with libraries and frameworks such as Spring and Guava.
_________

*/
//Your code should go here:

