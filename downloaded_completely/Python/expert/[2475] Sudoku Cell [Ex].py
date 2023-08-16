"""
####  Sudoku Cell  ####

A Sudoku puzzle contains 81 "cells" of numbers in a 9 x 9 grid. One helpful approach to solving a Sudoku puzzle is to make a class that represents each cell in the puzzle along with three different formats of the Sudoku puzzle representing each region type:
___
*) row
*) column
*) box
___

Keep in mind that the definition for a cell's region is as follows:
___
*) Each cell has a "region" which contains all values in the cell's row, column, and box excluding the cell itself.
___



[Task I]

Create a class Cell with the following attributes:
___
*) val: The value of the cell.
*) rLocation: The location of the cell in rowData with the format (r0, r1).
___

The class should have the following methods:
___
*) convIndices(): convert the row indices into column and box index formats.
*) getRegions(regionData): get the cell's region.
___



[Task II]

Create a function getRegionData(puzzle):
___
*) The function should return a list containing three different regional representations of the puzzle (as described below).
*) The function should create and store Cell instances in each nested list.
___



[Puzzle Format]

The Sudoku puzzle will be formatted in a 9 x 9 list where each nested list is a row in the puzzle:
___
puzzle = [
  [0, 0, 0, 0, 0, 0, 9, 0, 6],
  [3, 0, 2, 0, 6, 0, 0, 0, 0],
  [8, 0, 0, 7, 0, 3, 0, 0, 5],
  [0, 0, 3, 9, 0, 6, 0, 0, 0],
  [6, 0, 0, 0, 5, 0, 0, 0, 0],
  [0, 0, 4, 8, 0, 1, 0, 0, 0],
  [7, 0, 0, 4, 0, 8, 0, 0, 2],
  [5, 0, 8, 0, 9, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 7, 0, 1]
]
_____

Note: Zeros represent unsolved cells.


[The getRegionData(puzzle) Function]

This function should return a list containing the three lists representing different region types of the puzzle. For these purposes, these lists will be referred to as:
___
*) rowData: same format as puzzle.
*) colData: 2D list of columns.
*) boxData: 2D list of boxes ordered as shown below.
___


Note: Each box contains another 3 x 3 box ordered like its container. The numbers shown above represent indices that correspond to the following list structure:
___
*) [[0], ... , [8]] where each nested list is [0, ... , 8]
___



[The convIndices() Method]

This method should be called on initialization and create two new attributes:
___
*) cLocation: the location of the cell in colData with the format (c0, c1)
*) bLocation: the location of the cell in boxData with the format (b0, b1)
___

Hint: rowData[r0][r1] = colData[c0][c1] = boxData[b0][b1]


[Example #1]

___
cell = Cell(_, (1, 2))

cell.rLocation
(1, 2)

cell.cLocation
(2, 1)

cell.bLocation
(0, 5)
_____



[The getRegions(regionData) Method]

This method should take in regionData and create one new attribute:
___
*) regions: a 2D list containing the row, column, and box region for the cell.
___

Note: Each cell's region should contain Cell instances excluding the cell.


[Example #2]

___
regionData = getRegionData(puzzle)
cell.getRegions(regionData)

cell.regions
[[row region], [col region], [box region]]
_____



[Notes]

N/A


[algorithms] [arrays] [classes] [higher_order_functions] 



-------------------------------------------------------------------
[Resources]
_________
Python Classes and Objects
https://www.w3schools.com/python/python_classes.asp
Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor, o …
_________
_________
Sudoku
https://en.wikipedia.org/wiki/Sudoku
A logic-based combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids th …
_________

"""
#Your code should go here:

