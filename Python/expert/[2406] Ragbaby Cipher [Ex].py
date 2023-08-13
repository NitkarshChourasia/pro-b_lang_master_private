"""
####  Ragbaby Cipher  ####

In Ragbaby Cipher, encoding is done by a string of keys and their position in the plaintext word of a message.
Create a function that takes two arguments, key and message, and returns the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "This is an example."
key = "cipher"

ragbaby_cipher(message, key) ➞ "Urew pu bq rzfsbtj."
_____

Step 1: Remove duplicate alphabets of the key. Rearrange alphabets from A-Z, such that the keyword appears first, followed by the rest of the alphabets in the usual order.
___
c i p h e r a b d f g j k l m n o q s t u v w x y z
_____

Step 2: Word-by-word, assign numbers to the letters of the given message:
___
T h i s   i s   a n   e x a m p l e .
1 2 3 4   1 2   1 2   1 2 3 4 5 6 7
_____

Step 3: Replace each alphabet of the word with the letter in the keyed alphabet the corresponding number of places to the right of it (wrapping if necessary). Keep all characters other than alphabets in the same order and without any change.
___
eMessage = "Urew pu bq rzfsbtj."
# 'u' is 1 place right to 't'
# 'r' is 2 places right to 'h'
# 'e' is 3 places right to 'i' and so on.
# keep the '.' in the same position.
_____

See the below examples for a better understanding:


[Examples]

___
ragbaby_cipher("This is an example.", "cipher") ➞ "Urew pu bq rzfsbtj."

ragbaby_cipher("mubashir", "edabit") ➞ "nwccyoke"

ragbaby_cipher("mattttt", "eedddabit") ➞ "nighjkl"
_____



[Notes]

___
*) Keys will have lowercase letters only but encoded messages should keep the order of uppercase and lowercase as the original message.
*) The assigning of numbers to letters resets with every non-letter character.
___



[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
islower() Method
https://www.w3schools.com/python/ref_string_islower.asp
Check if all the characters in the text are in lower case.
_________
_________
lower() Method
https://www.w3schools.com/python/ref_string_lower.asp
Returns a string where all characters are lower case.
_________
_________
upper() Method
https://www.w3schools.com/python/ref_string_upper.asp
Returns a string where all characters are in upper case.
_________
_________
isupper() Method
https://www.w3schools.com/python/ref_string_isupper.asp
Returns True if all the characters are in upper case, otherwise False.
_________
_________
isalpha()
https://www.programiz.com/python-programming/methods/string/isalpha
Returns True if all characters in the string are alphabets. If not, it returns False.
_________

"""
#Your code should go here:

