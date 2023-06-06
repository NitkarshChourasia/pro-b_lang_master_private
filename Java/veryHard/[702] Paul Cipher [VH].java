/*
####  Paul Cipher  ####

In Paul Cipher, only alpha characters will be encoded with the following rules:
___
*) All alpha characters will be treated as uppercase letters.
*) The first alpha character will not change (except for switching to upper case).
*) All subsequent alpha characters will be shifted toward "Z" by the alphabetical position of the previous alpha character (wrap back to "A" if "Z" is passed).
___

he1lo would be encoded as follows:
___
paulCipher("he1lo") ➞ "HM1QA"

h -> H (First character to be changed to uppercase)
e -> M (H is the previous alpha character and the 8th letter in the alphabet. E + 8 = M)
1 -> 1 (Keep all characters other than alphabets as it is)
l -> Q (E is the previous alpha character and 5th letter in the alphabets. L + 5 = Q)
o -> A (L is the previous alpha character and 12th letter in the alphabets. O + 12 = A)
_____

Given a string txt, return the encoded message. See the below examples for a better understanding:


[Examples]

___
paulCipher("d33p x4v13r") ➞ "D33T N4T13N"

paulCipher("T3sh 1s my w0rlD.") ➞ "T3MA 1A FL V0ODP."

paulCipher("muBas41r") ➞ "MHWCT41K"

paulCipher("a1rForce") ➞ "A1SXUGUH"

paulCipher("MATT") ➞ "MNUN"
_____



[Notes]

N/A


[algorithms] [cryptography] [functional_programming] [math] 



-------------------------------------------------------------------
[Resources]
_________
How to convert ASCII code (0-255) to its corresponding character?
https://stackoverflow.com/questions/7693994/how-to-convert-ascii-code-0-255-to-its-corresponding-character
How can I convert, in Java, the ASCII code (which is an integer from [0, 255] range) to its corresponding ASCII character?
_________

*/
//Your code should go here:

