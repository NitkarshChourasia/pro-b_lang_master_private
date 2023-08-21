/*
####  Difference Cipher  ####

It's time to send and receive secret messages.
___
*) Create a function that takes a string and returns a coded message.
*) Create a function that takes an array and returns a decoded message.
___

The first letter of the string, or the first element of the array represents the Character Code of that letter. The next elements are the differences between the characters: e.g. A +3 --> C or z -1 --> y.


[Examples]

___
difCiph("Hello") ➞ [72, 29, 7, 0, 3]
// H = 72, the difference between the H and e is 29 (upper- and lowercase).
// The difference between the two l's is obviously 0.

difDiciph([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"

difCiph("Sunshine") ➞ [83, 34, -7, 5, -11, 1, 5, -9]
_____



[Notes]

N/A


[arrays] [cryptography] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
ASCII - Binary Character Table
http://sticksandstones.kstrom.com/appen.html
ASCII is a 7-bit character set containing 128 characters. It contains the numbers from 0-9, the upper and lower case English letters from A to Z, and some special chara …
_________

*/
//Your code should go here:

