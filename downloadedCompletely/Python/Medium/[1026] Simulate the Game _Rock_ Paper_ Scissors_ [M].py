"""
####  Simulate the Game "Rock, Paper, Scissors"  ####

Create a function which simulates the game "rock, paper, scissors". The function takes the input of both players (rock, paper or scissors), first parameter from first player, second from second player. The function returns the result as such:
___
*) "Player 1 wins"
*) "Player 2 wins"
*) "TIE" (if both inputs are the same)
___

The rules of rock, paper, scissors, if not known:
___
*) Both players have to say either "rock", "paper" or "scissors" at the same time.
*) Rock beats scissors, paper beats rock, scissors beat paper.
___



[Examples]

___
rps("rock", "paper") ➞ "Player 2 wins"

rps("paper", "rock") ➞ "Player 1 wins"

rps("paper", "scissors") ➞ "Player 2 wins"

rps("scissors", "scissors") ➞ "TIE"

rps("scissors", "paper") ➞ "Player 1 wins"
_____



[Notes]

Try to use a numpy array as a lookup table instead of if-constructions.


[data_structures] [games] 



-------------------------------------------------------------------
[Resources]
_________
Python Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and  they have keys and values.
_________
_________
Python NumPy Array Tutorial
https://likegeeks.com/numpy-array-tutorial/
In this tutorial, you'll learn how to perform many Python NumPy array operations such as adding, deleting, sorting, and extracting values, row, and columns.
_________
_________
Using Numpy Arrays As Lookup Tables
https://www.faqcode4u.com/faq/458780/using-numpy-arrays-as-lookup-tables
I have a 2D array of Numpy data read from a .csv file. Each row represents a data point with the final column containing a a 'key' which corresponds uniquely to 'key' i …
_________

"""
#Your code should go here:

