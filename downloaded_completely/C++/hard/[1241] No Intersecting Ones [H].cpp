/*
####  No Intersecting Ones  ####

A no-intersecting ones matrix is one where no two ones exist on the same row or column.
To illustrate:
___
[
  [1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0]
]
_____

The array below is not a non-intersecting ones matrix:
___
[
  [1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

// Column 2 has two 1s.
_____

Write a function that returns true if a 2D matrix is a no-intersecting ones matrix and false otherwise.


[Examples]

___
noIntersectingOnes([
  [0, 1],
  [1, 0]
]) ➞ true

noIntersectingOnes([
  [1, 1],
  [0, 0]
]) ➞ false

noIntersectingOnes([
  [0, 0, 0, 1],
  [1, 0, 0, 0],
  [0, 1, 0, 0]
]) ➞ true
_____



[Notes]

N/A


[arrays] [higher_order_functions] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________
_________
2D Vector In C++ With User Defined Size
https://www.geeksforgeeks.org/2d-vector-in-cpp-with-user-defined-size/
A 2D vector is a vector of vector. Like 2D arrays, we can declare and assign values to a 2D vector! Assuming you are familiar with a normal vector in C++, with the hel …
_________

*/
//Your code should go here:

