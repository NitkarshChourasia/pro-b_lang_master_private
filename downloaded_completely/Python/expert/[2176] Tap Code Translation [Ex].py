"""
####  Tap Code Translation  ####

Tap code is a way to communicate messages via a series of taps (or knocks) for each letter in the message. Letters are arranged in a 5x5 polybius square, with the letter "K" being moved to the space with "C".
___
   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
_____

Each letter is translated by tapping out the row and column number that the letter appears in, leaving a short pause in-between. If we use "." for each tap, and a single space to denote the pause:
___
text = "break"

"B" = (1, 2) = ". .."
"R" = (4, 2) = ".... .."
"E" = (1, 5) = ". ....."
"A" = (1, 1) = ". ."
"K" = (1, 3) = ". ..."
_____

Another space is added between the groups of taps for each letter to give the final code:
___
"break" = ". .. .... .. . ..... . . . ..."
_____

Write a function that returns the tap code if given a word, or returns the translated word (in lower case) if given the tap code. When translating from tap-code, default to the letter "c" if the tap-code ". ..." is found.


[Examples]

___
tap_code("break") ➞ ". .. .... .. . ..... . . . ..."

tap_code(".... ... ... ..... . ..... ... ... .... ....") ➞ "spent"
_____



[Notes]

For more information on tap code, please see the resources section. The code was widely used in WW2 as a way for prisoners to communicate.


[cryptography] [math] 



-------------------------------------------------------------------
[Resources]
_________
Using the Python zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________
_________
Tap Code
https://en.wikipedia.org/wiki/Tap_code
A way to encode text messages on a letter-by-letter basis in a very simple way. The message is transmitted using a series of tap sounds, hence its name. The tap code ha …
_________
_________
How to Iterate Through a Dictionary
https://realpython.com/iterate-through-dictionary-python/
In this step-by-step tutorial, you'll take a deep dive into how to iterate through a dictionary in Python. Dictionaries are a fundamental data structure, and you'll be …
_________

"""
#Your code should go here:

