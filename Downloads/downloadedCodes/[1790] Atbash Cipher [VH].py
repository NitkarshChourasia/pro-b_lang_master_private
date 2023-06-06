"""
####  Atbash Cipher  ####

The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
Create a function that takes a string and applies the Atbash cipher to it.


[Examples]

___
atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
_____



[Notes]

___
*) Capitalisation should be retained.
*) Non-alphabetic characters should not be altered.
___



[cryptography] [formatting] [strings] 



-------------------------------------------------------------------
[Resources]
_________
isupper(), islower(), lower(), upper()
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
In Python, isupper() is a built-in method used for string handling. The isupper() methods returns “True” if all characters in the string are uppercase, Otherwise, It re …
_________
_________
isalpha() Method
https://www.w3schools.com/python/ref_string_isalpha.asp
Returns True if all the characters are alphabet letters (a-z).
_________
_________
Atbash Cipher
http://practicalcryptography.com/ciphers/atbash-cipher-cipher/
The Atbash cipher is a substitution cipher with a specific key where the letters of the alphabet are reversed. I.e. all 'A's are replaced with 'Z's, all 'B's are replac …
_________
_________
Atbash Cipher
http://rumkin.com/tools/cipher/atbash.php
Is a very common, simple cipher. It was for the Hebrew alphabet, but modified here to work with the English alphabet. Basically, when encoded, an "A" becomes a "Z", "B" …
_________
_________
index() Method
https://www.programiz.com/python-programming/methods/list/index
Returns the index of the specified element in the list.
_________

"""
#Your code should go here:

