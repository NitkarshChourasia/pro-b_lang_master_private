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
e -> M (H is the previous alpha character and 8th letter in the alphabets. E + 8 = M)
1 -> 1 (Keep all characters other than alphabets as it is)
l -> Q (E is the previous alpha character and 5th letter in the alphabets. L + 5 = Q)
o -> A (L is the previous alpha character and 12th letter in the alphabets. O + 12 = A)
_____

Given a string txt, return the encoded message. See the below examples for a better understanding:


[Examples]

___
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
isdigit()
https://www.programiz.com/cpp-programming/library-function/cctype/isdigit
Checks if the given character is a digit or not.
_________
_________
islower()
https://www.programiz.com/cpp-programming/library-function/cctype/islower
Checks if the given character is a lowercase character or not.
_________
_________
toupper()
https://www.programiz.com/cpp-programming/library-function/cctype/toupper
Converts a given character to uppercase.
_________
_________
isupper()
https://www.programiz.com/cpp-programming/library-function/cctype/isupper
Checks if ch is in uppercase as classified by the current C locale. By default, the characters from A to Z (ascii value 65 to 90) are uppercase characters.
_________
_________
std::string::substr
http://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object. The substring is the portion of the object that starts at …
_________

*/
//Your code should go here:

