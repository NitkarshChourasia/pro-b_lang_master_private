"""
####  Simple Minesweeper  ####

Given a 2D array of mines, replace the question mark with the number of mines that immediately surround it. This includes the diagonals, meaning it is possible for it to be surrounded by 8 mines maximum.
The key is as follows:
___
*) An empty space: "-"
*) A mine: "#"
*) Number showing number of mines surrounding it: "?"
___



[Examples]

___
minesweeper([
  ["-", "#", "-"],
  ["-", "?", "-"],
  ["-", "-", "-"]
]) ➞ [
  ["-", "#", "-"],
  ["-", "1", "-"],
  ["-", "-", "-"]
]

minesweeper([
  ["-", "#", "-"],
  ["#", "-", "?"],
  ["#", "#", "-"]
]) ➞ [
  ["-", "#", "-"],
  ["#", "-", "2"],
  ["#", "#", "-"]
]

minesweeper([
  ["-", "#", "#"],
  ["?", "#", ""],
  ["#", "?", "-"]
]) ➞ [
  ["-", "#", "#"],
  ["3", "#", ""],
  ["#", "2", "-"]
]

minesweeper([
  ["-", "-", "#"],
  ["?", "-", "-"],
  ["-", "-", "-"]
]) ➞ [
  ["-", "-", "#"],
  ["0", "-", "-"],
  ["-", "-", "-"]
]
_____



[Notes]

___
*) You will only be given 3x3 grids.
*) The question mark is not limited to the centre (there may be multiple question marks).
___



[arrays] [games] 



-------------------------------------------------------------------
[Resources]
_________
While Loops
https://www.w3schools.com/python/python_while_loops.asp
Requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
_________
_________
enumerate() Method
https://www.tutorialspoint.com/enumerate-in-python
When using the iterators, we need to keep track of the number of items in the iterator. This is achieved by an in-built method called en ...
_________

"""
#Your code should go here:

