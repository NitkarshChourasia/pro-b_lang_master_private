/*
####  Knights On A Board  ####

Write a function that returns true if the knights are placed on a chessboard such that no knight can capture another knight. Here, 0's represent empty squares and 1's represent knights.


[Examples]

___
cannotCapture([
  [0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 0]
]) ➞ true

cannotCapture([
  [1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0, 1, 0, 1]
]) ➞ false

cannotCapture([
  [0, 0, 0, 0, 1, 0, 0, 0], 
  [0, 0, 0, 0, 0, 1, 0, 0], 
  [0, 0, 0, 1, 0, 0, 0, 0], 
  [1, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 1, 0, 0, 0], 
  [0, 0, 0, 0, 0, 1, 0, 0], 
  [0, 0, 0, 0, 0, 1, 0, 0], 
  [1, 0, 0, 0, 0, 0, 0, 0]
]) ➞ false
_____



[Notes]

___
*) Knights can be present in any of the 64 squares.
*) No other pieces exist but knights.
___



[arrays] [games] [validation] 



-------------------------------------------------------------------
[Resources]
_________
The Knight
http://www.chesscorner.com/tutorial/basic/knight/knight.htm
Moves in an L shape in any direction. We can say that it either moves two squares sideways and then one square up or down, or two squares up or down, and then one squar …
_________

*/
//Your code should go here:

