"""
####  Snake Game  ####

Write a function that can simulate a crawling snake.



[Input]

___
*) field — A rectangular matrix, list of lists, consisting of numbers corresponding to: 0 – empty cell, 1 – food, 2 – the head of the snake.
*) moves — A list of tuples.
___

Each tuple represents the following moves:
___
*) (1, 0) — Down
*) (0, 1) — Right
*) (-1, 0) — Up
*) (0, -1) — Left
___



[Output]

The final picture of the field, which consists of the snake as a collection of 2 in certain cells and remaining food 1 that has not been eaten during the snake moves.


[Rules]

The snake’s head moves in the direction specified by the given move. If the head moves into an empty cell, then the whole body moves in an orderly fashion (the length of the snake does not change). If the head moves into a food cell, then the body does not move, the new head takes the position of the food (the length of the snake extends by one). If the head bumps into a wall, then it goes through and the head pops up from the opposite wall (on the same row if the move is horizontal, on the same column if the move is vertical).
If the head has to move into its own body, excluding the tip of the tail, then the snake bites itself and inflicts a mortal injury. In this case, stop the function execution, return the string "Game Over".
The head cannot catch the tail. It is assumed in this game that when the head moves, the tail also moves and vacates the cell.
The food cell can only be eaten once! If the snake crawls around and passes the cell again, then this cell has become an empty cell.


[Examples]

___
f = [
  [0, 0, 0, 0, 0, 1],
  [0, 2, 0, 0, 1, 0],
  [0, 0, 0, 1, 0, 0],
  [0, 1, 0, 0, 0, 0]
]

m = [
  (0, 1), (0, 1), (0, 1), (-1, 0), (0, 1), (0, 1), (0, 1), (1, 0),
  (1, 0), (1, 0), (0, 1), (0, 1), (-1, 0), (0, 1), (-1, 0)
]

snake(f, m) ➞ [
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 2, 0],
  [0, 0, 0, 2, 2, 0],
  [0, 0, 2, 2, 0, 0]
]
_____



[Notes]

___
*) At the beginning of the game, the snake’s body is only the head (total length is one).
*) After the head executes the given list of moves, the happy snake stops and takes a rest. The function output should display the snake’s body's final position in the field.
___



[games] [language_fundamentals] [loops] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

