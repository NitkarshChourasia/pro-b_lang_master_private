"""
####  Paul Cipher  ####

In Paul Cipher, only alpha characters will be encoded with the following rules:
___
*) All alpha characters will be treated as uppercase letters.
*) The first alpha character will not change (except for switching to upper case).
*) All subsequent alpha characters will be shifted toward "Z" by the alphabetical position of the previous alpha character (wrap back to "A" if "Z" is passed).
___

he1lo would be encoded as follows:
___
paul_cipher("he1lo") ➞ "HM1QA"

h -> H (First character to be changed to uppercase)
e -> M (H is the previous alpha character and 8th letter in the alphabets. E + 8 = M)
1 -> 1 (Keep all characters other than alphabets as it is)
l -> Q (E is the previous alpha character and 5th letter in the alphabets. L + 5 = Q)
o -> A (L is the previous alpha character and 12th letter in the alphabets. O + 12 = A)
_____

Given a string txt, return the encoded message. See the below examples for a better understanding:


[Examples]

___
paul_cipher("muBas41r") ➞ "MHWCT41K"

paul_cipher("a1rForce") ➞ "A1SXUGUH"

paul_cipher("MATT") ➞ "MNUN"
_____



[Notes]

N/A


[algorithms] [cryptography] [functional_programming] [math] 



-------------------------------------------------------------------
[Resources]
_________
String isupper() Method
https://www.programiz.com/python-programming/methods/string/isupper
Returns whether or not all characters in a string are uppercased or not.
_________
_________
String upper() Method
https://www.programiz.com/python-programming/methods/string/upper
Converts all lowercase characters in a string into uppercase characters and returns it.
_________
_________
ord() Method
https://www.programiz.com/python-programming/methods/built-in/ord
Returns an integer representing the Unicode character.
_________
_________
String islower() Method
https://www.programiz.com/python-programming/methods/string/islower
Returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.
_________
_________
String isdigit() Method
https://www.programiz.com/python-programming/methods/string/isdigit
Returns True if all characters in a string are digits. If not, it returns False.
_________

"""
#Your code should go here:

