/*
####  Switch on the Gravity  ####

Given a 2D array of some suspended blocks (represented as hastags), return another 2D array which shows the end result once gravity is switched on.


[Examples]

___
switchGravityOn([
  ["-", "#", "#", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"]
]) ➞ [
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "#", "#", "-"]
]

switchGravityOn([
  ["-", "#", "#", "-"],
  ["-", "-", "#", "-"],
  ["-", "-", "-", "-"],
]) ➞ [
  ["-", "-", "-", "-"],
  ["-", "-", "#", "-"],
  ["-", "#", "#", "-"]
]

switchGravityOn([
  ["-", "#", "#", "#", "#", "-"],
  ["#", "-", "-", "#", "#", "-"],
  ["-", "#", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-"]
]) ➞ [
  ["-", "-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-"],
  ["-", "#", "-", "#", "#", "-"],
  ["#", "#", "#", "#", "#", "-"]
]
_____



[Notes]

Each block falls individually, meaning there are no rigid objects. Think about it like falling sand in Minecraft as opposed to the rigid blocks in Tetris.


[arrays] [logic] [loops] [physics] 



-------------------------------------------------------------------
[Resources]
_________
2D Vector
https://www.geeksforgeeks.org/2d-vector-in-cpp-with-user-defined-size/
Is a vector of vector. Like 2D arrays, we can declare and assign values to a 2D vector! Assuming you are familiar with a normal vector in C++, with the help of an exam …
_________

*/
//Your code should go here:

