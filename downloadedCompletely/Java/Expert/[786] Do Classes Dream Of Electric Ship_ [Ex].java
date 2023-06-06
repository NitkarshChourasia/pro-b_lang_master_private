/*
####  Do Classes Dream Of Electric Ship?  ####

Build a Class that will store and manipulate the data of a simplified clone of the popular strategy game, Battleship.
The game is played on a 5x5-sized board. The rows of the grid are identified by the uppercase letters A to E (top to bottom), and the columns are identified by the numbers 1 to 5 (left to right).


[Rules of the Game]

___
*) There are two types of ship: the Patrol and the Cruiser. The Patrol occupies a single cell, the Cruiser occupies two cells, horizontally or vertically.
*) Three Patrols and three Cruisers will be placed randomly in the grid, without ships adjacent in rows and columns (see the notes below).
*) The user calls six different cells, trying to guess if there's a Patrol or a Cruiser in it.
*) Hits and misses are recorded on the board. For every hit Patrol or Cruiser, a point is gained, and if a Cruiser is sunk, two additional points are gained.
___



[Class "Battleship"]

Each instance in the Tests tab will be declared with two variable parameters so the constructor has to be initialized with:
___
*) scheme - an array containing 9 strings being the coordinates indicating where the ships are placed on the grid.
*) target - an array containing 6 strings being the guesses made by the user.
___



[What do you have to implement?]

The Tests will verify the existence and the correctness of the data through an instance of the Battleship Class and will invoke its four different methods:
___
*) board() - returns the final state of the board, based on the placement of the ship and the results of the user guesses, as a 5x5 matrix. The following character set will represent the graphic of the game:

○ = a blank space on the board.
● = a space occupied by a ship.
☼ = a miss (wrong guess).
☀ = a hit (a correct guess).
*) hits() - returns the total number of hits made by the user (correct guesses), either on Patrols or on Cruisers.
*) sunk() - returns the total number of sunk Cruisers (two adjacent guesses, in horizontal or vertical).
*) points() - returns the total number of points gained by the user (1 for every hit, 2 for every sunk Cruiser).
___



[Examples]

___
// scheme = ["A1", "C1", "B2", "B3", "D2", "E2", "E4", "E5", "A5"]

// target = ["A1", "B2", "C3", "D4", "E5", "E4"]

battleship.board() ➞ [
  [☀, ○, ○, ○, ●],
  [○, ☀, ●, ○, ○],
  [●, ○, ☼, ○, ○],
  [○, ●, ○, ☼, ○],
  [○, ●, ○, ☀, ☀]
]

battleship.hits() ➞ 4
// Total hits.

battleship.sunk() ➞ 1
// Sunk Cruisers, not Patrols.

battleship.points() ➞ 6
// Hits + additional points given by Sunk Cruisers.
_____



[Notes]

___
*) If two cruisers are in the same row or the same column, there will be a blank cell between them, so that it will be possible to treat them as different ships.
*) The board is not given, you have to build it.
*) In the Examples above, the symbols of the board are not between quotation marks for readability, but they are strings. The set of characters used for this challenge is already in the Code tab.
___



[arrays] [classes] [data_structures] [games] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

