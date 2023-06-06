"""
####  Block the Square in Tic Tac Toe  ####

Create a function that returns a number which can block the player from reaching 3 in a row in a game of Tic Tac Toe. The number given as an argument will correspond to a grid of Tic Tac Toe: topleft is 0, topright is 2, bottomleft is 6, and bottomright is 8.
___
*) Create a function that takes two numbers a, b and returns another number.
*) This number should be the final one in a line to block the player from winning.
___



[Examples]

___
block_player(0, 3) ➞ 6

block_player(0, 4) ➞ 8

block_player(3, 5) ➞ 4
_____



[Notes]

The values given will always have two filled squares in a line.


[algorithms] [games] [logic] 



-------------------------------------------------------------------
[Resources]
_________
Tic-tac-toe
https://en.wikipedia.org/wiki/Tic-tac-toe
Who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.
_________
_________
Tic Tac Toe Winning Conditions
https://stackoverflow.com/questions/40559066/python-tic-tac-toe-winning-conditons
Utilizing the magic square method to easily determine whether a given play wins at Tic Tac Toe; reorganizing the board means that any rows, columns or diagonals that su …
_________

"""
#Your code should go here:

