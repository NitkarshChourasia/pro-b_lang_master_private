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
Multidimensional Arrays
https://www.geeksforgeeks.org/multidimensional-arrays-in-java/
Can be defined in simple words as array of arrays. Data in multidimensional arrays are stored in tabular form (in row major order).
_________
_________
How to Loop Over Two Dimensional Array
https://javarevisited.blogspot.com/2015/09/how-to-loop-two-dimensional-array-in-java.html#axzz7UpUiywS8
You can loop over a two-dimensional array in Java by using two for loops, also known as nested loop. Similarly to loop an n-dimensional array you need n loops nested in …
_________
_________
Ternary Operator With Multiple Conditions
https://www.codegrepper.com/code-examples/whatever/ternary+operator+with+multiple+conditions+java
Ternary operator with multiple conditions in java.
_________

*/
//Your code should go here:

