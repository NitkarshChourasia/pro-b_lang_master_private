/*
####  Validate the Tic-Tac-Toe Game State  ####

The function is given a list of three strings representing a board. The characters can be "X", "O", " ". The first player writes "X" at first turn. If a player has three marks in a row, column or a diagonal, the game stops. Given the board evaluate if this state can be achieved in line with the rules, return true / false.


[Examples]

___
validateTicTacToe(["X  ", "   ", "   "]) ➞ true
// X goes first.

validateTicTacToe(["O  ", "   ", "   "]) ➞ false
// O cannot go first.

validate_tic_tac_toe(["X X", " O ", "   "]) ➞ true
// Two X and one O is a possible state.

validateTicTacToe(["XOX", " X ", "   "]) ➞ false
// Three X and one O is not a possible state.
// Players have to go one after another.
_____



[Notes]

N/A


[algorithms] [games] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Tic Tac Toe
https://en.wikipedia.org/wiki/Tic-tac-toe
Is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their mar …
_________

*/
//Your code should go here:

