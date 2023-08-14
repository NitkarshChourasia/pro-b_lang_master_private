"""
####  Knights on a Board  ####

Write a function that returns True if the knights are placed on a chessboard such that no knight can capture another knight. Here, 0s represent empty squares and 1s represent knights.


[Examples]

___
cannot_capture([
  [0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 0]
]) ➞ True

cannot_capture([
  [1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0, 1, 0, 1]
]) ➞ False
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
Creating a 3D List
https://www.geeksforgeeks.org/python-creating-3d-list/
A 3-D List means that we need to make a list that has three parameters to it, i.e., (a x b x c), just like a 3 D array in other languages. In this program we will try t …
_________
_________
Possible Moves of Knight
http://www.chesscorner.com/tutorial/basic/knight/knight.htm
The Knight moves in an L shape in any direction. We can say that it either moves two squares sideways and then one square up or down, or two squares up or down, and the …
_________

"""
#Your code should go here:

