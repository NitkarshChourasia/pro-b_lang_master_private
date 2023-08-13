"""
####  OOP Minesweeper  ####

In this challenge we're going to build a board for a Minesweeper game using OOP. Create two classes: Game and Cell.
Game should take in 3 arguments: number of rows, number of columns and total number of mines, set the default values to 14, 18 and 40 respectively. Each instance should have attributes .rows, .cols and .mines, equivalent to the values of the three arguments. It should also have a .board attribute, the board shoud be a 2-D list with rows sublists with cols instances of Cell.
A Cell should have attributes .row and .col, set these to its position on the board. Attributes .mine (either True or False), .flag and .open (set both to False). Finally an attribute .neighbors, indicating how many of its neighboring cells are mined.


[Tests]

___
game = Game()
game.rows ➞ 14
game.cols ➞ 18
game.mines ➞ 40
height of .board ➞ 14
width of .board ➞ 18
Cells in .board ➞ 252
total mined in cells .board ➞ 40
each Cell .row and .col attributes match its position on the board ➞ True
each Cell .flag and .open attributes are set to False ➞ True
each Cell .neighbors attribute matches the actual amount of neighboring mines ➞ True
_____



[Notes]

___
*) Try randomizing the position of the mines.
*) Feel free to add as many other attributes or methods as you need.
___



[arrays] [classes] [games] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Minesweeper (video game)
https://en.wikipedia.org/wiki/Minesweeper_(video_game)
The objective of the game is to clear a rectangular board containing hidden "mines" or bombs without detonating any of them, with help from clues about the number of ne …
_________
_________
Object-Oriented Programming (OOP) in Python
https://realpython.com/python3-object-oriented-programming/
In this article you’ll learn the fundamentals of object-oriented programming (OOP) in Python and how to work with classes, objects, and constructors. The tutorial also …
_________

"""
#Your code should go here:

