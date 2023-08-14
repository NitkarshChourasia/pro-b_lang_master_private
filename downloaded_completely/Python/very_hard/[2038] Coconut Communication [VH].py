"""
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
coconut_translator("Hi") ➞ "cOcoNuts cOCoNutS"

coconut_translator("edabit") ➞ "cOConUtS cOConUts cOConutS cOConuTs cOCoNutS cOCOnUts"

coconut_translator("123") ➞ "coCOnutS coCOnuTs coCOnuTS"
_____



[Notes]

___
*) All inputs will be strings.
*) Make sure to separate the coconuts with spaces.
___



[loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
How to Convert a String to Binary in Python
https://www.kite.com/python/answers/how-to-convert-a-string-to-binary-in-python
Converting a string to binary results in a list of binary values representing the original characters. For example, the string "abc" has the binary representation ["0b1 …
_________
_________
Convert Binary to String Using Python
https://www.geeksforgeeks.org/convert-binary-to-string-using-python/
The naive approach is to convert the given binary data in decimal by taking the sum of binary digits (dn) times their power of 2*(2^n). The binary data is divided into …
_________
_________
String zfill() Method
https://www.programiz.com/python-programming/methods/string/zfill
Returns a copy of the string with '0' characters padded to the left.
_________
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________

"""
#Your code should go here:

