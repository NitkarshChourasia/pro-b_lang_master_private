/*
####  Knights on a Board  ####

Write a function that returns true if the knights are placed on a chessboard such that no knight can capture another knight. Here, 0s represent empty squares and 1s represent knights.


[Examples]

___
CannotCapture(new int[,] {
  { 0, 0, 0, 1, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 0, 0, 0 },
  { 0, 1, 0, 0, 0, 1, 0, 0 },
  { 0, 0, 0, 0, 1, 0, 1, 0 },
  { 0, 1, 0, 0, 0, 1, 0, 0 },
  { 0, 0, 0, 0, 0, 0, 0, 0 },
  { 0, 1, 0, 0, 0, 0, 0, 1 },
  { 0, 0, 0, 0, 1, 0, 0, 0 }
}) ➞ True

CannotCapture(new int[,] {
  {1, 0, 1, 0, 1, 0, 1, 0},
  {0, 1, 0, 1, 0, 1, 0, 1},
  {1, 0, 1, 0, 1, 0, 1, 0},
  {0, 0, 0, 1, 0, 1, 0, 1},
  {1, 0, 0, 0, 1, 0, 1, 0},
  {0, 0, 0, 0, 0, 1, 0, 1},
  {1, 0, 1, 0, 1, 0, 1, 0},
  {1, 0, 0, 1, 0, 0, 0, 1} 
}) ➞ False
_____



[Notes]

___
*) Knights can be present in any of the 64 squares.
*) No other pieces except knights exist.
___



[arrays] [games] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Knight
https://en.wikipedia.org/wiki/Knight_(chess)
Is a piece in the game of chess and is represented by a horse's head and neck. Each player starts with two knights, which are located between the rooks and bishops.
_________

*/
//Your code should go here:

