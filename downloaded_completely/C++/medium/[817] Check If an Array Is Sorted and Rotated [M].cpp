/*
####  Check If an Array Is Sorted and Rotated  ####

Given an array of distinct integers, create a function that checks if the array is sorted and rotated clockwise. If so, return "YES"; otherwise return "NO".


[Examples]

___
check([3, 4, 5, 1, 2]) ➞ "YES"
// The above array is sorted and rotated.
// Sorted array: [1, 2, 3, 4, 5].
// Rotating this sorted array clockwise
// by 3 positions, we get: [3, 4, 5, 1, 2].

check([1, 2, 3]) ➞ "NO"
// The above array is sorted but not rotated.

check([7, 9, 11, 12, 5]) ➞ "YES"
// The above array is sorted and rotated.
// Sorted array: [5, 7, 9, 11, 12].
// Rotating this sorted array clockwise
// by 4 positions, we get: [7, 9, 11, 12, 5].
_____



[Notes]

N/A


[algorithms] [arrays] [conditions] 



-------------------------------------------------------------------
[Resources]
_________
std::sort()
https://www.geeksforgeeks.org/sort-c-stl/
Provides a similar function sort that sorts a vector or array (items with random access). It generally takes two parameters , the first one being the point of the array …
_________

*/
//Your code should go here:

