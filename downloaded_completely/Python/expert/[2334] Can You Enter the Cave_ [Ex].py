"""
####  Can You Enter the Cave?  ####

You are playing a video game. Your screen can be represented as a 2D array, where 0s represent walkeable areas and 1s represent unwalkeable areas. You are currently searching for the entrance to a cave that is located on the right side of the screen. Your character starts anywhere in the leftmost column.
Create a function that determines if you can enter the cave. You can only move left, right, up, or down (not allowed to move diagonally).
To illustrate:
___
[
  [0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 0]
]
_____

You found the entrance! Function should output True.
___
[
  [0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 1, 1, 1, 1, 0]
]
_____

Nope, keep looking. Function should output False.


[Examples]

___
can_enter_cave([
  [0, 1, 1, 1, 0, 1, 1, 0],
  [0, 0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0],
  [0, 1, 1, 1, 1, 1, 1, 0]
]) ➞ False

# You cannot walk diagonally!


can_enter_cave([
  [0, 1, 1, 1, 0, 1, 1, 0],
  [0, 0, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 1, 1, 1, 1, 0]
]) ➞ True


can_enter_cave([
  [0, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 0],
  [0, 1, 1, 0, 0, 1, 1, 0]
]) ➞ False
_____



[Notes]

___
*) You are seeing the game screen from a birds-eye view.
*) Another way of thinking about it: You can enter the cave if you can move from the left side of the screen to the right side by only walking up, down or right.
*) The entrance is not necessarily the first square, you may have to search for it in the left hand column.
___



[arrays] [functional_programming] [games] 



-------------------------------------------------------------------
[Resources]
_________
Minimum Cost Path
https://algorithms.tutorialhorizon.com/dynamic-programming-minimum-cost-path-problem/
Objective: Given a 2D-matrix where each cell has a cost to travel. You have to write an algorithm to find a path from left-top corner to bottom-right corner with minimu …
_________
_________
Pathfinding
https://en.wikipedia.org/wiki/Pathfinding
Is the plotting, by a computer application, of the shortest route between two points. It is a more practical variant on solving mazes. This field of research is based h …
_________

"""
#Your code should go here:

