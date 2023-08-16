"""
####  Validate the Tic-Tac-Toe Game State  ####

The function is given a list of three strings representing a board. The characters can be "X", "O", " ". The first player writes "X" at first turn. If a player has three marks in a row, column or a diagonal, the game stops. Given the board evaluate if this state can be achieved in line with the rules, return True / False.


[Examples]

___
validate_tic_tac_toe(["X  ", "   ", "   "]) ➞ True
# X goes first.

validate_tic_tac_toe(["O  ", "   ", "   "]) ➞ False
# O cannot go first.

validate_tic_tac_toe(["X X", " O ", "   "]) ➞ True
# Two X and one O is a possible state.

validate_tic_tac_toe(["XOX", " X ", "   "]) ➞ False
# Three X and one O is not a possible state.
# Players have to go one after another.
_____



[Notes]

N/A


[algorithms] [games] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Play Tic Tac Toe
https://playtictactoe.org/
Play tic tac toe online.
_________

"""
#Your code should go here:

