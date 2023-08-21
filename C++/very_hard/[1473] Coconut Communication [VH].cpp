/*
####  Coconut Communication  ####

___
*) "coconuts" has 8 letters.
*) A byte in binary has 8 bits.
*) A byte can represent a character.
___

We can use the word "coconuts" to communicate with each other in binary if we use upper case letters as 1s and lower case letters as 0s.
Create a function that translates a word in plain text, into Coconut.


[Worked Example]

___
The binary for "coconuts" is
01100011 01101111 01100011 01101111 01101110 01110101 01110100 01110011
c         o        c       o       n        u        t       s

Since 0s are lowercase and 1s are uppercase, we can map the binary like this.
cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS

coconut_translator("coconuts") ➞ "cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS"
_____



[Examples]

___
coconutTranslator("Hi") ➞ "cOcoNuts cOCoNutS"

coconutTranslator("edabit") ➞ "cOConUtS cOConUts cOConutS cOConuTs cOCoNutS cOCOnUts"

coconutTranslator("123") ➞ "coCOnutS coCOnuTs coCOnuTS"
_____



[Notes]

___
*) All inputs will be strings.
*) Make sure to separate the coconuts with spaces.
___



[cryptography] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
ASCII - Binary Character Table
http://sticksandstones.kstrom.com/appen.html
ASCII - Binary Character Table
_________
_________
Character to Binary Conversion
https://stackoverflow.com/questions/19844122/character-to-binary-conversion-in-c-two-characters-at-a-time-to-get-16-bit-bin/19844576
Hello i want to convert two characters at a time in a string to binary? how can i do that by applying simple arithmetic (that is by making my own function?) For exampl …
_________

*/
//Your code should go here:

