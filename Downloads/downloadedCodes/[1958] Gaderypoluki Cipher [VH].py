"""
####  Gaderypoluki Cipher  ####

Create a function that takes an encryption key (a string with an even number of characters) and a message to encrypt. Group the letters of the key by two:
___
"gaderypoluki" -> "ga de ry po lu ki"
_____

Now take the message for encryption. If the message character appears in the key, replace it with an adjacent character in the grouped version of the key. If the message character does not appear in the key, leave it as is. If the letter in the key occurs more than once, the first result is used. For example: use the above key, if the letter "a" appeared in the message, it would be replaced with "g" since "g" in the adjacent letter.
Return the encrypted message.


[Examples]

___
encrypt("ab c", "abc ab") ➞ "ba cba"

encrypt("otorhinolaryngological", "My name is Paul") ➞ "Mr olme hs Plua"

encrypt("gaderypoluki", "This is an encrypted message") ➞ "Thks ks gn dncyrotde mdssgad"
_____



[Notes]

N/A


[algorithms] [cryptography] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Dictionaries in Python
https://realpython.com/python-dicts/
In this Python dictionaries tutorial you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, yo …
_________
_________
Using the Python zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________
_________
Splitting, Concatenating, and Joining Strings in Python
https://realpython.com/courses/splitting-concatenating-and-joining-strings-python/
In this course you'll some of the most fundamental string operations: splitting, concatenating, and joining. Not only will you learn how to use these tools, but you’ll …
_________

"""
#Your code should go here:

