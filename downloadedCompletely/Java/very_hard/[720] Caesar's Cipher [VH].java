/*
####  Caesar's Cipher  ####

Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher (check Resources tab for more info) shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
Create a function that takes a string s (text to be encrypted) and an integer k (the rotation factor). It should return an encrypted string.


[Examples]

___
caesarCipher("middle-Outz", 2) ➞ "okffng-Qwvb"

// m -> o
// i -> k
// d -> f
// d -> f
// l -> n
// e -> g
// -    -
// O -> Q
// u -> w
// t -> v
// z -> b

caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 5)
➞ "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"

caesarCipher("A friend in need is a friend indeed", 20)
➞ "U zlcyhx ch hyyx cm u zlcyhx chxyyx"
_____



[Notes]

All test input will be a valid ASCII string.


[algorithms] [cryptography] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Caesars Cipher
https://en.wikipedia.org/wiki/Caesar_cipher
One of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some …
_________
_________
Caesar Cipher
https://www.dcode.fr/caesar-cipher
Tool to decrypt/encrypt with Caesar. Caesar cipher (or Caesar code) is a shift cipher, one of the most easy and most famous encryption systems. It uses the substitution …
_________
_________
ASCII Table
https://en.wikipedia.org/wiki/File:ASCII-Table.svg
A list of all the useful characters in the ASCII table. Goes up to 0x7F.
_________
_________
Caesar's Cipher Java Coding Challenge
https://youtu.be/4woytkup98Q
Caesar's Cipher Java coding challenge.
_________

*/
//Your code should go here:

