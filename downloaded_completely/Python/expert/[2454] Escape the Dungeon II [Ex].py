"""
####  Escape the Dungeon II  ####

Ogmo has been imprisoned in a dungeon (again). He needs your help (again). Clearly, Ogmo has many enemies who like dungeons.
Create a function that takes the map of a dungeon as an argument and prints a new map that indicates the shortest path to escape from the dungeon, as well as the minimum number of steps to reach the exit and the escape sequence. This time, in order to escape from the dungeon, Ogmo must recover a key to unlock the exit door (in case you wonder, Ogmo could cast some spells over the lock, but the exit door is cursed and can only be unlocked by the hidden key inside the dungeon).
___
*) Ogmo starts inside the dungeon in the position indicated with O.
*) The exit is indicated with X. There will always be an exit from the dungeon and the exit can be anywhere inside the dungeon (not only in the borders of the map).
*) In order to open the exit door, Ogmo must recover a key ~. There will always be a key in the dungeon, so we can infer the enemies from Ogmo are quite dumb.
*) Ogmo can only move in four directions: Right R, Left L, Up U, Down D.
*) Each step that Ogmo needs to do to escape from the dungeon must be indicated in the solution map with 1. If Ogmo walks two times over the same tile, we must indicate this with 2.
*) The walls of the dungeon are indicated with #. Ogmo can only move through the empty spaces " ".
*) Check the Tests to understand how to print the solution.
___



[Examples]

___
escape([
  ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
  ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
  ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
  ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
  ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#"],
  ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
  ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
  ["#", " ", "#", "#", "#", " ", "#", "#", " ", "#"],
  ["#", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
  ["#", " ", "#", "#", "O", "#", "#", "#", " ", "#"],
  ["#", " ", "#", "#", "#", "#", "#", "#", " ", "#"],
  ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
  ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
  ["#", " ", "#", " ", "#", "~", "#", "#", " ", "#"],
  ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#"],
  ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
  ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
  ["#", " ", "#", "#", "#", " ", "#", "#", " ", "#"],
  ["#", " ", " ", " ", " ", " ", "X", "#", " ", "#"],
  ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]) ➞
  ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
  ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"]
  ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"]
  ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"]
  ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#"]
  ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#"]
  ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#"]
  ["#", " ", "#", "#", "#", " ", "#", "#", " ", "#"]
  ["#", "1", "1", "1", "1", " ", " ", "#", " ", "#"]
  ["#", "1", "#", "#", "O", "#", "#", "#", " ", "#"]
  ["#", "1", "#", "#", "#", "#", "#", "#", " ", "#"]
  ["#", "1", "1", "2", "2", "2", " ", " ", " ", "#"]
  ["#", " ", "#", "1", "#", "2", "#", "#", " ", "#"]
  ["#", " ", "#", "1", "#", "1", "#", "#", " ", "#"]
  ["#", " ", "#", "1", "#", "#", "#", "#", "#", "#"]
  ["#", " ", "#", "1", "1", "1", " ", " ", " ", "#"]
  ["#", " ", "#", " ", "#", "1", "#", "#", " ", "#"]
  ["#", " ", "#", "#", "#", "1", "#", "#", " ", "#"]
  ["#", " ", " ", " ", " ", "1", "1", "#", " ", "#"]
  ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]

# Number of steps to escape from the dungeon: 27
# Escape sequence: ULLLDDDRRRRDDUULLDDDDRRDDDR
_____



[Notes]

Check out the first part of this challenge: Escape the Dungeon I


[arrays] [games] 



-------------------------------------------------------------------
[Resources]
_________
Array Data Structure
https://www.geeksforgeeks.org/array-data-structure/
An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculat …
_________

"""
#Your code should go here:

