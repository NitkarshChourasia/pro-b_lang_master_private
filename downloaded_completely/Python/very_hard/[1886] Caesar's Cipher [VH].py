"""
####  Caesar's Cipher  ####

Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher (check Resources tab for more info) shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
Create a function that takes a string s (text to be encrypted) and an integer k (the rotation factor). It should return an encrypted string.


[Examples]

___
caesar_cipher("middle-Outz", 2) ➞ "okffng-Qwvb"

# m -> o
# i -> k
# d -> f
# d -> f
# l -> n
# e -> g
# -    -
# O -> Q
# u -> w
# t -> v
# z -> b

caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5)
➞ "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"

caesar_cipher("A friend in need is a friend indeed", 20)
➞ "U zlcyhx ch hyyx cm u zlcyhx chxyyx"
_____



[Notes]

All test input will be a valid ASCII string.


[algorithms] [cryptography] [strings] 



-------------------------------------------------------------------
[Resources]
_________
ASCII Table
https://en.wikipedia.org/wiki/File:ASCII-Table.svg
For reference.
_________
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
maketrans() Method
https://www.programiz.com/python-programming/methods/string/maketrans
Returns a mapping table for translation usable for translate() method.
_________
_________
translate() Method
https://www.programiz.com/python-programming/methods/string/translate
Returns a string where each character is mapped to its corresponding character in the translation table.
_________
_________
Common String Operations
https://docs.python.org/3/library/string.html?highlight=string#module-string
The built-in string class provides the ability to do complex variable substitutions and value formatting via the format() method described in PEP 3101. The Formatter cl …
_________
_________
Converting Between ASCII Numbers and Characters
http://code.activestate.com/recipes/65117-converting-between-ascii-numbers-and-characters/
You want to get the ASCII number of a character, or you want to get the character given by an ASCII number. For Unicode characters the builtin functions ord() and unich …
_________

"""
#Your code should go here:

