"""
####  Escape the Dungeon I  ####

Ogmo is a wizard that has been imprisoned in a dungeon. He needs your help.
Create a function that takes the map of a dungeon as an argument and prints a new map that indicates the shortest path to escape from the dungeon, as well as the minimum number of steps to reach the exit and the escape sequence.
___
*) Ogmo starts inside the dungeon in the position indicated with O.
*) The exit is indicated with X. There will always be an exit from the dungeon and the exit can be anywhere inside the dungeon (not only in the borders of the map).
*) Ogmo can only move in four directions: Right R, Left L, Up U, Down D.
*) Each step that Ogmo needs to do to escape from the dungeon must be indicated in the solution map with +.
*) The walls of the dungeon are indicated with #. Ogmo can only move through the empty spaces " ".
*) Check the tests section to understand how to print the solution.
___



[Examples]

___
escape([
  ["#", "#", "#", "#", "#"],
  ["#", "O", " ", " ", "#"],
  ["#", "#", " ", "#", "#"],
  ["#", " ", " ", " ", "X"],
  ["#", "#", "#", "#", "#"]
]) ➞
  ["#", "#", "#", "#", "#"]
  ["#", "O", "+", " ", "#"]
  ["#", "#", "+", "#", "#"]
  ["#", " ", "+", "+", "+"]
  ["#", "#", "#", "#", "#"]

# Number of steps to escape from the dungeon: 5
# Escape sequence: RDDRR

escape([
  ["#", "#", "#", "#", "#"],
  ["#", "O", " ", "X", "#"],
  ["#", "#", " ", "#", "#"],
  ["#", " ", " ", " ", "#"],
  ["#", "#", "#", "#", "#"]
]) ➞
  ["#", "#", "#", "#", "#"]
  ["#", "O", "+", "+", "#"]
  ["#", "#", " ", "#", "#"]
  ["#", " ", " ", " ", "#"]
  ["#", "#", "#", "#", "#"]

# Number of steps to escape from the dungeon: 2
# Escape sequence: RR
_____



[Notes]

Check out the second part of this challenge: Escape the Dungeon II


[arrays] [games] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

