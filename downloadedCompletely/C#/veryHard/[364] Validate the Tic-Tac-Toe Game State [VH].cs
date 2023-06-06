/*
####  Validate the Tic-Tac-Toe Game State  ####

The function is given an array of three strings representing a board. The characters can be "X", "O", " ". The first player writes "X" at first turn. If a player has three marks in a row, column or a diagonal, the game stops. Given the board evaluate if this state can be achieved in line with the rules, return true or false.


[Examples]

___
ValidateTicTacToe(string[] { "X  ", "   ", "   " }) ➞ true
// X goes first.

ValidateTicTacToe(string[] { "O  ", "   ", "   " }) ➞ false
// O cannot go first.

ValidateTicTacToe(string[] { "X X", " O ", "   " }) ➞ true
// Two X and one O is a possible state.

ValidateTicTacToe(string[] { "XOX", " X ", "   " }) ➞ false
// Three X and one O is not a possible state.
// Players have to go one after another.
_____



[Notes]

N/A


[algorithms] [games] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
For Loop
https://www.w3schools.com/cs/cs_for_loop.php
When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop.
_________

*/
//Your code should go here:

