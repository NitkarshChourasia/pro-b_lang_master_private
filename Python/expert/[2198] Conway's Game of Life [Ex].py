"""
####  Conway's Game of Life  ####


The goal of this challenge is to implement the logic used in Conway's Game of Life. Wikipedia will give a better understanding of what it is and how it works (check the resources tab above).


[Rules]

___
*) For a space that's "populated":
Each cell with 0 or 1 neighbours dies, as if by solitude.
Each cell with 2 or 3 neighbours survives.
Each cell with 4 or more neighbours dies, as if by overpopulation.
*) For a space that's "empty" or "unpopulated":
Each cell with 3 neighbours becomes populated.
___



[Parameters]

board: a 2-dimensional list of values 0 to 1.
___
*) 0 means that the cell is empty.
*) 1 means the cell is populated.
___



[Return Value]

A string containing the board's state after the game logic has been applied once.
___
On character: I
Off character: _
_____



[Notes]

___
*) The string should be divided by newlines \n to signal the end of each row.
*) A cell's "neighbours" are the eight cells that are vertically, horizontally and diagonally adjacent to it.
___



[arrays] [conditions] [games] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Conway's Game of Life Online Simulation
https://bitstorm.org/gameoflife/
Play John Conway's Game of Life right now in your browser.
_________
_________
The Coding Train: The Game of Life
https://www.youtube.com/watch?v=FWSR_7kZuYg
Video tutorial of an implementation using the p5.js library by The Coding Train
_________
_________
Conway's Game of Life
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
_________

"""
#Your code should go here:

