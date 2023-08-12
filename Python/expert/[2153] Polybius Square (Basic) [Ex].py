"""
####  Polybius Square (Basic)  ####

The Polybius Square cipher is a simple substitution cipher that makes use of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and "J" typically sharing a slot (as there are 26 letters and only 25 slots).

To encipher a message, each letter is merely replaced by its row and column numbers in the grid.
Create a function that takes a plaintext or ciphertext message, and returns the corresponding ciphertext or plaintext.


[Examples]

___
polybius("Hi") ➞ "2324"

polybius("2324  4423154215") ➞ "hi there"

polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"
_____



[Notes]

As "I" and "J" share a slot, both are enciphered into 24, but deciphered only into "I" (see third and fourth test).


[arrays] [cryptography] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Dictionary
https://www.programiz.com/python-programming/dictionary
In this tutorial, you'll learn everything about Python dictionaries; how they are created, accessing, adding, removing elements from them and various built-in methods.
_________
_________
How to Iterate Through a Dictionary
https://realpython.com/iterate-through-dictionary-python/
In this step-by-step tutorial, you'll take a deep dive into how to iterate through a dictionary in Python. Dictionaries are a fundamental data structure, and you'll be …
_________
_________
Polubius Square Cypher
https://crypto.interactive-maths.com/polybius-square.html#:~:text=The%20Polybius%20Square%20is%20an,have%20one%20too%20many%20letters.
Is an ancient Greek invention, discovered by a scholar named Polybius. For the Greek alphabet of 24 letters, it consisted of a 5 by 5 grid where each square of the grid …
_________

"""
#Your code should go here:

