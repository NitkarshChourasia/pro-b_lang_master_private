/*
####  Crop Fields  ####

You're given a 2D array / matrix of a crop field. Each crop needs a water source. Each water source hydrates the 8 tiles around it. With "w" representing a water source, and "c" representing a crop, is every crop hydrated?


[Examples]

___
cropHydrated([
  [ "w", "c" ],
  [ "w", "c" ],
  [ "c", "c" ]
]) ➞ true

cropHydrated([
  [ "c", "c", "c" ]
]) ➞ false
// There isn"t even a water source.

cropHydrated([
  [ "c", "c", "c", "c" ],
  [ "w", "c", "c", "c" ],
  [ "c", "c", "c", "c" ],
  [ "c", "w", "c", "c" ]
]) ➞ false
_____



[Notes]

"w" on its own should return true, and "c" on its own should return false.


[arrays] [conditions] [loops] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
2D Vector
https://www.geeksforgeeks.org/2d-vector-in-cpp-with-user-defined-size/
Is a vector of vector. Like 2D arrays, we can declare and assign values to a 2D vector! Assuming you are familiar with a normal vector in C++, with the help of an exam …
_________

*/
//Your code should go here:

