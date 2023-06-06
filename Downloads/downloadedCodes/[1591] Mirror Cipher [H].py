"""
####  Mirror Cipher  ####

In Mirror Cipher, encoding is done by switching message characters with its mirror opposite character of the key.
Create a function that takes two arguments; a message and an optional key, and return the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "Mubashir Hassan"
key = "edabitisamazing"

mirror_cipher(message, key) ➞ "tuzishar hissid"
_____

Step 1: Replace all characters of the given message with mirror character in the key:
___
M = t
# "t" is the mirror character of "m".
# (five characters from the left and right end respectively)

u = u
# "u" is not part of the key.

b = z
# "z" is the mirror character of "b".

a = i, and so on ...
_____

Step 2: Return encoded message in lower case:
___
"tuzishar hissid"
_____

If optional key is not given, consider the whole alphabet as a default (i.e. key = "abc..z").


[Examples]

___
mirror_cipher("Mubashir Hassan", "edabitisamazing") ➞ "tuzishar hissid"

mirror_cipher("Matt MacPherson") ➞ "nzgg nzxksvihlm"

mirror_cipher("Airforce is best", "pilot") ➞ "aorfirce os besp"
_____



[Notes]

Ignore case of message and key, (e.g. "M" = "m").


[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String lower() Method
https://www.programiz.com/python-programming/methods/string/lower
Converts all uppercase characters in a string into lowercase characters and returns it.
_________
_________
String translate() Method
https://www.programiz.com/python-programming/methods/string/translate#:~:text=Join-,Python%20String%20translate(),as%20per%20the%20mapping%20table.
Returns a string where each character is mapped to its corresponding character in the translation table.
_________
_________
String maketrans() Method
https://www.w3schools.com/python/ref_string_maketrans.asp
Returns a mapping table that can be used with the translate() method to replace specified characters.
_________

"""
#Your code should go here:

