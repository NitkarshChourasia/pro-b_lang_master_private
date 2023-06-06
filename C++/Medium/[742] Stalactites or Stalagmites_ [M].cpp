/*
####  Stalactites or Stalagmites?  ####

Stalactites hang from the ceiling of a cave while stalagmites grow from the floor.
Create a function that determines whether the input represents "stalactites" or "stalagmites". If it represents both, return "both". Input will be a 2D array, with 1 representing a piece of rock, and 0 representing air space.


[Examples]

___
mineralFormation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]) ➞ "stalactites"

mineralFormation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "stalagmites"

mineralFormation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "both"
_____



[Notes]

___
*) There won't be any examples where both stalactites and stalagmites meet (because those are called pillars).
*) There won't be any example of neither stalactites nor stalagmites.
*) In other words, if the first array has 1s, return "stalactites". If the last array has 1s, return "stalagmites". If both have them, return "both".
___



[arrays] [validation] 



-------------------------------------------------------------------
[Resources]
_________
What is the difference between a stalactite and a stalagmite?
https://oceanexplorer.noaa.gov/facts/stalactite.html#:~:text=A%20stalactite%20is%20an%20icicle,dripping%20through%20the%20cave%20ceiling.&text=A%20stalagmite%20is%20an%20upward,the%20floor%20of%20a%20cave.
Stalactites hang from the ceiling of a cave while stalagmites grow from the cave floor.
_________

*/
//Your code should go here:

