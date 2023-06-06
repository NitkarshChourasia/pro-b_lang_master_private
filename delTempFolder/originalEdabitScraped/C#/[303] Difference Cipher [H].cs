/*
####  Difference Cipher  ####

It's time to send and receive secret messages.
Create two functions that take a string and an array and returns a coded or decoded message.
The first letter of the string, or the first element of the array represents the Character Code of that letter. The next elements are the differences between the characters: e.g. A +3 --> C or z -1 --> y.


[Examples]

___
Encrypt("Hello") ➞ [72, 29, 7, 0, 3]
// H = 72, the difference between the H and e is 29 (upper- and lowercase).
// The difference between the two l's is obviously 0.

Decrypt([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"

Encrypt("Sunshine") ➞ [83, 34, -7, 5, -11, 1, 5, -9]
_____



[Notes]

___
*) The input of the encrypt function will always be a string.
*) The input of the decrypt function will always be an array with numbers.
___



[arrays] [cryptography] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
ASCII
https://en.wikipedia.org/wiki/ASCII
Is a character encoding standard for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices. Most modern cha …
_________

*/
//Your code should go here:

