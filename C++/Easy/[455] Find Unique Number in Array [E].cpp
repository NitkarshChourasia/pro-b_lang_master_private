/*
####  Find Unique Number in Array  ####

Create a function that takes an array of integers as an argument and returns a unique number from that array. All numbers except unique ones have the same number of occurrences in the array.


[Examples]

___
findSingleNumber([2, 2, 2, 3, 4, 4, 4]) ➞ 3

findSingleNumber([2]) ➞ 2

findSingleNumber([]) ➞ -1

findSingleNumber([7, 13, 3, 6, 5, 4, 4, 13, 5, 3, 6, 7, 6, 5, 3, 13, 4, 7, 13, 5, 7, 4, 3, 6, 8, 4, 3, 7, 5, 6, 13]) ➞ 8

findSingleNumber([1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 101, 4, 3, 1, 5, 6, 2]) ➞ 101
_____



[Notes]

___
*) Don't forget to return the result.
*) Be aware this challenge includes two validations:
Empty input should return -1 (example #3).
Single item arrays should return that item (example #2).
*) There are always 1 or 0 unique numbers in the input. No two or three+ uniques.
*) If you're stuck or your solution is over complicated check the Resources tab.
___



[arrays] [language_fundamentals] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::sort()
https://www.geeksforgeeks.org/sort-c-stl/
Sorts the element in ascending order.
_________
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Vectors are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means …
_________
_________
std::count
https://www.geeksforgeeks.org/std-count-cpp-stl/
Returns the number of occurrences of an element in a given range. Returns the number of elements in the range [first, last) that compare equal to val.
_________

*/
//Your code should go here:

