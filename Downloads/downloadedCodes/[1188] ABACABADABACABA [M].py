"""
####  ABACABADABACABA  ####

Create a function that follows the "ABACABADABACABA" rule up to a certain letter.
The abacabadabacaba pattern is where you start with the first letter (a), and with each new letter, you add the letter in the middle and the others at the start and end.
For instance:
___
A ➞ **A**
B ➞ A**B**A
C ➞ ABA**C**ABA
D ➞ ABACABA**D**ABACABA
E ➞ ABACABADABACABA**E**ABACABADABACABA
F ➞ ABACABADABACABAEABACABADABACABA**F**ABACABADABACABAEABACABADABACABA

# And so on ...
_____



[Examples]

___
ABA("A") ➞ "A"

ABA("B") ➞ "ABA"

ABA("E") ➞ "ABACABADABACABAEABACABADABACABA"
_____



[Notes]

N/A


[algorithms] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Generate the Abacaba Sequence
https://codegolf.stackexchange.com/questions/68978/generate-the-abacaba-sequence
This challenge is about printing the abacaba sequence of a specific depth. Here is a diagram of the first 5 sequences (a(N) is the abacaba sequence of depth N, upper/lo …
_________
_________
chr() and ord() Functions
https://www.askpython.com/python/built-in-methods/python-chr-and-ord-methods#:~:text=globals()%20function-,Python%20chr()%20and%20ord(),how%20they%20can%20be%20used.
Python’s built-in function chr() is used for converting an Integer to a Character, while the function ord() is used to do the reverse, i.e, convert a Character to an In …
_________

"""
#Your code should go here:

