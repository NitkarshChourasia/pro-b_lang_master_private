/*
####  Wrong Number  ####

Mubashir needs your help to find out a wrong number in a 2D array.
Imagine a 2D array of numbers given below:
___
var arr = [
  [1, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]
_____

You can notice that:
___
*) The end number of each row is the sum of each row's previous numbers.
*) The end number of each column is the sum of each column's previous numbers.
___

See below examples for a better understanding:
___
arr1 = [
  [2, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]

// 2 is incorrect in first row and first column.
// Replace it with 1.

arr2 = [
  [1, 2, 3, 7 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,45]
]

// 7 is incorrect in first row and fourth column.
// Replace it with 6.

arr3 = [
  [1, 2, 3, 6 ],
  [4, 5, 6, 15],
  [7, 8, 9, 24],
  [12,15,18,46]
]

// 46 is incorrect in fourth row and fourth column.
// Replace it with 45.
_____



[Examples]

___
wrongNumber(arr1) ➞ 1

wrongNumber(arr2) ➞ 6

wrongNumber(arr3) ➞ 45
_____



[Notes]

N/A


[algorithms] [loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
2D Vector with User Defined Size
https://www.geeksforgeeks.org/2d-vector-in-cpp-with-user-defined-size/
A 2D vector is a vector of vector. Like 2D arrays, we can declare and assign values to a 2D vector! Assuming you are familiar with a normal vector in C++, with the hel …
_________
_________
accumulate() and partial_sum()
https://www.geeksforgeeks.org/accumulate-and-partial_sum-in-c-stl-numeric-header/
We usually find out the sum of elements in a particular range or a complete array using a linear operation which requires adding all the elements in the range one by on …
_________

*/
//Your code should go here:

