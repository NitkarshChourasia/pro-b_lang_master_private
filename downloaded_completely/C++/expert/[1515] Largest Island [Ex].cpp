/*
####  Largest Island  ####

An island is a region of contiguous ones. A contiguous one is a 1 that is touched by at least one other 1, either horizontally, vertically or diagonally. Given a piece of the map, represented by a 2-D array, create a function that returns the area of the largest island.
To illustrate, if we were given the following piece of the map, we should return 4.
___
[
  [0, 0, 0],
  [0, 1, 1],
  [0, 1, 1]
]
_____

Our function should yield 2 for the map below:
___
[
  [1, 0, 0],
  [0, 0, 1],
  [0, 0, 1]
]
_____

Our function should yield 4 for the map below: :
___
[
  [1, 0, 0],
  [0, 1, 1],
  [0, 0, 1]
]
_____



[Examples]

___
largestIsland([
  [1, 0, 0],
  [0, 0, 0],
  [0, 0, 1]
])

➞ 1

largestIsland([
  [1, 1, 0],
  [0, 1, 1],
  [0, 0, 1]
])

➞ 5

largestIsland([
  [1, 0, 0],
  [1, 0, 0],
  [1, 0, 1]
])

➞ 3
_____



[Notes]

___
*) Maps can be any m x n dimension.
*) Maps will always have at least 1 element. m >= 1 and n >= 1.
___



[arrays] [data_structures] [games] [logic] 



-------------------------------------------------------------------
[Resources]
_________
2D Vector
https://www.geeksforgeeks.org/2d-vector-in-cpp-with-user-defined-size/
Assuming you are familiar with a normal vector in C++, with the help of an example we demonstrate how a 2D vector differs from a normal vector.
_________
_________
std::pair
https://www.geeksforgeeks.org/pair-in-cpp-stl/
Is a class template that provides a way to store two heterogeneous objects as a single unit.
_________

*/
//Your code should go here:

