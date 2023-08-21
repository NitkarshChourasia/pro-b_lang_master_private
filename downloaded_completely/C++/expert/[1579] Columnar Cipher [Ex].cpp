/*
####  Columnar Cipher  ####

The columnar cipher is a transposition cipher that works like this.
Start with a secret message:
___
msg = "Meet me by the lake at midnight. Bring shovel."
_____

Transform uppercase letters into lowercase and remove punctuation and spaces:
___
msg = "meetmebythelakeatmidnightbringshovel"
_____

Then, pick a keyword made out of distinct letters:
___
keyword = "python"
_____

Break up the message into chunks of the same length as the keyword, and write them in rows under the keyword. Then, number the columns based on the alphabetised order of the letters in the keyword:

Read off the enciphered message (ciphertext) from the columns, in the order specified by the numbers:
___
ciphertext = "thaiivelmhglmetgnembaitsetenroeykdbh"
_____

If the message length is not a multiple of the keyword length, fill in each blank space with "x". For example:
___
msg = "Meet me at midnight."

keyword = "python"
_____


Create a function that takes a string and a keyword. Return the ciphertext if the string is in plaintext (i.e. broken up into normal English words and punctuated), or the deciphered message if the string is in ciphertext. The resulting deciphered message will not have spaces.


[Examples]

___
cipher("Meet me by the lake at midnight. Bring shovel.", "python")
➞ "thaiivelmhglmetgnembaitsetenroeykdbh"

cipher("meeanbsleyamgioxebltirhxttkihnvxmhedtgex", "monty")
➞ "meetmebythelakeatmidnightbringshovelxxxx"

cipher("Mission Delta Kilo Sierra has been compromised. Kill Steve. Evacuate", "cake")
➞ "ioliiabcrsiteuxmieksrsnpiksecesdaoraemmdlvatxsntleheooelevax"
_____



[Notes]

N/A


[arrays] [cryptography] [loops] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Columnar Transposition Cipher
https://crypto.interactive-maths.com/columnar-transposition-cipher.html#:~:text=Columnar%20Transposition%20involves%20writing%20the,looks%20like%20the%20grid%20below
Columnar Transposition involves writing the plaintext out in rows, and then reading the ciphertext off in columns. In its simplest form, it is the Route Cipher where th …
_________
_________
Columnar Transposition Cipher
https://www.boxentriq.com/code-breaking/columnar-transposition-cipher
Tool to decode columnar transposition ciphers. In a columnar transposition cipher, the message is written in a grid of equal length rows, and then read out column by co …
_________

*/
//Your code should go here:

