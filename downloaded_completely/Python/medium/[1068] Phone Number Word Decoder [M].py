"""
####  Phone Number Word Decoder  ####

Create a program that converts a phone number with letters to one with only numbers.



[Examples]

___
text_to_num("123-647-EYES") ➞ "123-647-3937"

text_to_num("(325)444-TEST") ➞ "(325)444-8378"

text_to_num("653-TRY-THIS") ➞ "653-879-8447"

text_to_num("435-224-7613") ➞ "435-224-7613"
_____



[Notes]

___
*) All inputs will be formatted as a string representing a proper phone number in the format XXX-XXX-XXXX or (XXX)XXX-XXXX, using numbers and capital letters.
*) Check the Resources tab for more info on telephone keypads.
___



[formatting] [language_fundamentals] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
maketrans() and translate()
https://www.geeksforgeeks.org/python-maketrans-translate-functions/
To translate the characters in the string translate() is used to make the translations. This function uses the translation mapping specified using the maketrans().
_________
_________
Telephone Keypad
https://en.wikipedia.org/wiki/Telephone_keypad
A telephone keypad is the keypad installed on a push-button telephone or similar telecommunication device for dialing a telephone number. It was standardized when the …
_________

"""
#Your code should go here:

