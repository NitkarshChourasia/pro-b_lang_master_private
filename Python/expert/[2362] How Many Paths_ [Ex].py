"""
####  How Many Paths?  ####

This challenge is an extension of Helen Yu's Can You Exit the Maze? and Can You Enter the Cave?. Most of the test cases come from her challenge with a few new ones of my own.
Instead of finding a path through the maze, you must find all connected paths - paths where you can walk from one cell to another either by doing up or down or left or right. Not diagonally.
The maze is represented by a 2D matrix, where 0s represent walkable areas, and 1s represents walls.
Write a function that will return the length of the longest connected path (each cell only counts once even if you must re-enter to fully walk the path) and the number of connected paths as a tuple.


[Examples]

___
how_many_paths([
  [0, 0, 0, 1, 0, 0, 1, 1],
  [0, 1, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 0, 0, 0, 1],
  [1, 1, 1, 1, 0, 0, 0, 1]
]) ➞ (9, 4)

# The longest path is in the lower right and there are
# four paths, upper left with 8, upper right with 5,
# lower left with 1.
_____

___
how_many_paths([
  [0, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 1, 0],
  [0, 1, 1, 0, 0, 1, 1, 0]
]) ➞ (20, 1)
_____

___
how_many_paths([
  [0, 1, 1, 1, 0, 1, 1, 0],
  [0, 0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0],
  [0, 1, 1, 1, 1, 1, 1, 0]
]) ➞ (8, 2)
_____



[Notes]

This is a variation of a problem where I had to find all groups of connected customers (owners of the same account) across a bank's customer database in preparation to split the bank and 'sell' off some of the customers/accounts.


[arrays] [functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
Python If ... Else
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics: Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Gre …
_________

"""
#Your code should go here:

