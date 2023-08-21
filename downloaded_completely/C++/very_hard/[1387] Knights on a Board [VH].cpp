/*
####  Knights on a Board  ####

Write a function that returns true if the knights are placed on a chessboard such that no knight can capture another knight. Here, 0s represent empty squares and 1s represent knights.


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
Vector of Vectors
https://www.geeksforgeeks.org/vector-of-vectors-in-c-stl-with-examples/
Vectors are known as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatical …
_________
_________
The Knight
http://www.chesscorner.com/tutorial/basic/knight/knight.htm
Moves in an L shape in any direction. We can say that it either moves two squares sideways and then one square up or down, or two squares up or down, and then one squar …
_________

*/
//Your code should go here:

