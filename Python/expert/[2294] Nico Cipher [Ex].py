"""
####  Nico Cipher  ####

In Nico Cipher, encoding is done by creating a numeric key and assigning each letter position of the message with the provided key.
Create a function that takes two arguments, key and message, and returns the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "mubashirhassan"
key = "crazy"

nico_cipher(message, key) ➞ "bmusarhiahass n"
_____

Step 1: Assign numbers to sorted letters from the key:
___
"crazy" = 23154
_____

Step 2: Assign numbers to the letters of the given message:
___
2 3 1 5 4
---------
m u b a s
h i r h a
s s a n
_____

Step 3: Sort columns as per assigned numbers:
___
1 2 3 4 5
---------
b m u s a
r h i a h
a s s   n
_____

Step 4: Return encoded message Rows-wise:
___
eMessage = "bmusarhiahass n"
_____



[Examples]

___
nico_cipher("mubashirhassan", "crazy") ➞ "bmusarhiahass n"

nico_cipher("edabitisamazing", "matt") ➞ "deabtiismaaznig "

nico_cipher("iloveher", "612345") ➞ "lovehir    e"
_____



[Notes]

Keys will have alphabets or numbers only.


[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
String join() Method
https://www.programiz.com/python-programming/methods/string/join
Returns a string by joining all the elements of an iterable, separated by a string separator.
_________
_________
len() Method
https://www.w3schools.com/python/ref_func_len.asp
Returns the number of items in an object.
_________
_________
Itertools.zip_longest()
https://www.geeksforgeeks.org/python-itertools-zip_longest/
Python’s Itertool is a module that provides various functions that work on iterators to produce complex iterators. This module works as a fast, memory-efficient tool th …
_________
_________
zip() Method
https://www.programiz.com/python-programming/methods/built-in/zip
Takes iterables (can be zero or more), aggregates them in a tuple, and return it.
_________
_________
String lower() Method
https://www.programiz.com/python-programming/methods/string/lower
Converts all uppercase characters in a string into lowercase characters and returns it.
_________

"""
#Your code should go here:

