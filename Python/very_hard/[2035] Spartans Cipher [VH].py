"""
####  Spartans Cipher  ####

In Spartans Cipher, encoding is done by writing the text horizontally, across the strap in the plaintext word of a message. In ancient times, Spartans and Greeks invented an interesting way of encryption called Scytale.
The ancient Greeks, and the Spartans in particular, are said to have used this cipher to communicate during military campaigns.
Create a function that takes two arguments, a number of slides n_Slide and a string message, and returns the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "Mubashir Scytale Code"
n_Slide = 6

spartans_cipher(message, n_Slide) ➞ "Ms t euhSaC biclo aryed"
_____

Step 1: Imagine this Scytale:

Step 2: You can write the given message on a 6 slide Scytale like this:
___
| M | u | b | a |
| s | h | i | r |
|   | S | c | y |
| t | a | l | e |
|   | C | o | d |
| e |   |   |   |
_____

Step 3: Encode the message column-wise:
___
"Ms t euhSaC biclo aryed "
_____

Step 4: Trim all spaces at the end and return the final encoded message:
___
"Ms t euhSaC biclo aryed"
_____

See the below examples for a better understanding:


[Examples]

___
spartans_cipher("Mubashir Scytale Code", 6) ➞ "Ms t euhSaC biclo aryed"

spartans_cipher("Matt and Edabit are amazing", 8) ➞ "M  baai aaEirmn tndteag tda  z"

spartans_cipher("", 99) ➞ ""
_____



[Notes]

Decode your encrypted message with Evgeny SH here.


[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Scytale
https://en.wikipedia.org/wiki/Scytale
A tool used to perform a transposition cipher, consisting of a cylinder with a strip of parchment wound around it on which is written a message. The ancient Greeks, and …
_________
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
String ljust() Method
https://www.programiz.com/python-programming/methods/string/ljust
Returns a left-justified string of a given minimum width.
_________
_________
String strip() Method
https://www.w3schools.com/python/ref_string_strip.asp
Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove).
_________

"""
#Your code should go here:

