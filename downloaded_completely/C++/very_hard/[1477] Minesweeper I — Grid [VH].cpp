/*
####  Minesweeper I — Grid  ####

This challenge is based on the game Minesweeper.
Create a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot. Return an array where each dash is replaced by a digit indicating the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally).


[Examples]

___
numGrid([
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) ➞ [
  ["0", "0", "0", "0", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "1", "#", "1", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "0", "0", "0"],
]

numGrid([
  ["-", "-", "-", "-", "#"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["#", "-", "-", "-", "-"]
]) ➞ [
  ["0", "0", "0", "1", "#"],
  ["0", "1", "1", "2", "1"],
  ["0", "1", "#", "1", "0"],
  ["1", "2", "1", "1", "0"],
  ["#", "1", "0", "0", "0"]
]

numGrid([
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) ➞ [
  ["1", "1", "2", "#", "#"],
  ["1", "#", "3", "3", "2"],
  ["2", "4", "#", "2", "0"],
  ["1", "#", "#", "2", "0"],
  ["1", "2", "2", "1", "0"],
]
_____



[Notes]

N/A


[arrays] [games] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Implementation of Minesweeper Game
https://www.geeksforgeeks.org/cpp-implementation-minesweeper-game/
We play on a square board and we have to click on the board on the cells which do not have a mine. And obviously we don’t know where mines are. If a cell where a mine i …
_________

*/
//Your code should go here:

