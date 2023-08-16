/*
####  Nico Cipher  ####

In Nico Cipher, encoding is done by creating a numeric key and assigning each letter position of the message with the provided key.
Create a function that takes two arguments, key and message, and returns the encoded message.
There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
___
message = "mubashirhassan"
key = "crazy"

nicoCipher(message, key) ➞ "bmusarhiahass n"
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
NicoCipher("mubashirhassan", "crazy") ➞ "bmusarhiahass n"

NicoCipher("edabitisamazing", "matt") ➞ "deabtiismaaznig "

NicoCipher("iloveher", "612345") ➞ "lovehir    e"
_____



[Notes]

Keys will have alphabets or numbers only.


[algorithms] [cryptography] [logic] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Parallel Arrays
https://www.geeksforgeeks.org/parallel-array/
Also known as structure an array (SoA), multiple arrays of the same size such that i-th element of each array is closely related and all i-th elements together represen …
_________

*/
//Your code should go here:

