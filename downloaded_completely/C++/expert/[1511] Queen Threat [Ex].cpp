/*
####  Queen Threat  ####

Create a function that takes a character from a to h as the column number and an integer from 1 to 8 as the row number which together represent the location of a queen on a normal-sized chess board. Return this two dimensional 8x8 array.
This array must consist of zeroes and ones. The ones are placed in positions where the queen can move in one move and zeroes represent positions on the board where it cannot.


[Examples]

___
checkBoard("a", 1) ➞ [
  [1, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 1, 0, 0],
  [1, 0, 0, 0, 1, 0, 0, 0],
  [1, 0, 0, 1, 0, 0, 0, 0],
  [1, 0, 1, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1]
]

checkBoard("h", 4) ➞ [
  [0, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 1],
  [0, 0, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0, 1, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 1]
]
 
checkBoard("c", 8) ➞ [
  [1, 1, 0, 1, 1, 1, 1, 1],
  [0, 1, 1, 1, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 1, 0],
  [0, 0, 1, 0, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0]
]
_____



[Notes]

The queens' current position is a zero as it is impossible to move to this position during one turn, because the queen is already there.


[arrays] [games] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Understanding Chess Notation
https://www.dummies.com/games/chess/understanding-chess-notation/
Chess notation has an important role in the world of chess because it preserves the game’s history. It allows people to record games for posterity and gives them the ch …
_________
_________
The Queen
http://www.chess-poster.com/english/learn_chess/queen/the_queen.htm
Typical Staunton wood Queen piece used in a game of Chess (Fig. 1). The Queen is the most powerful major piece on the Chessboard after the King.
_________

*/
//Your code should go here:

