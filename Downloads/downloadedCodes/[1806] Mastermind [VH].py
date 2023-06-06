"""
####  Mastermind  ####

The classic game of Mastermind is played on a tray on which the Mastermind conceals a code and the Guesser has 10 tries to guess it. The code is a sequence of 4 (or 6, sometimes more) pegs of different colors. Each guess is a corresponding sequence of 4 (or more) pegs of different colors. A guess is "correct" when the color of every peg in the guess exactly matches the corresponding peg in the Mastermind's code.
After each guess by the Guesser, the Mastermind will give a score comprising black & white pegs, not arranged in any order:
___
*) Black peg == guess peg matches the color of a code peg in the same position.
*) White peg == guess peg matches the color of a code peg in another position.
___

Create a function that takes two strings, code and guess as arguments, and returns the score in a dictionary.
___
*) The code and guess are strings of numeric digits
*) The color of the pegs are represented by numeric digits
*) no "peg" may be double-scored
___



[Examples]

___
guess_score("1423", "5678") ➞ {"black": 0, "white": 0}

guess_score("1423", "2222") ➞ {"black": 1, "white": 0}

guess_score("1423", "1234") ➞ {"black": 1, "white": 3}

guess_score("1423", "2211") ➞ {"black": 0, "white": 2}
_____



[Notes]

___
*) The code and guess sequences will have the same length.
*) The "pegs" consists of only digits from 0-9.
___



[algorithms] [games] [logic] 



-------------------------------------------------------------------
[Resources]
_________
How to replace a character from a certain index?
https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
How can I replace a character in a string from a certain index? For example, I want to get the middle character from a string, like abc, and if the character is not equ …
_________
_________
Dictionaries
https://realpython.com/python-dicts/
In this Python dictionaries tutorial you'll cover the basic characteristics and learn how to access and manage dictionary data. Once you have finished this tutorial, yo …
_________
_________
Using the Python zip() Function for Parallel Iteration
https://realpython.com/python-zip-function/
In this step-by-step tutorial, you'll learn how to use the Python zip() function to solve common programming problems. You'll learn how to traverse multiple iterables i …
_________
_________
find() Method
https://www.programiz.com/python-programming/methods/string/find
Returns the index of first occurrence of the substring (if found). If not found, it returns -1.
_________

"""
#Your code should go here:

