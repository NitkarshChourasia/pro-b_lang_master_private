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
PaulCipher("he1lo") ➞ "HM1QA"

h -> H (First character to be changed to uppercase)
e -> M (H is the previous alpha character and 8th letter in the alphabets. E + 8 = M)
1 -> 1 (Keep all characters other than alphabets as it is)
l -> Q (E is the previous alpha character and 5th letter in the alphabets. L + 5 = Q)
o -> A (L is the previous alpha character and 12th letter in the alphabets. O + 12 = A)
_____

Given a string txt, return the encoded message. See the below examples for a better understanding:


[Examples]

___
PaulCipher("muBas41r") ➞ "MHWCT41K"

PaulCipher("a1rForce") ➞ "A1SXUGUH"

PaulCipher("MATT") ➞ "MNUN"
_____



[Notes]

N/A


[algorithms] [cryptography] [functional_programming] [math] 



-------------------------------------------------------------------
[Resources]
_________
Paul Rubin Cipher
http://cipherfoundation.org/modern-ciphers/paul-rubin-cipher/
Paul Emanuel Rubin was an 18-year-old chemistry student from Brooklyn NY whose body was found near Philadelphia International Airport on 20th January 1953: he had died …
_________

*/
//Your code should go here:

