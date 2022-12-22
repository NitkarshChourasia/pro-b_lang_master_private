/*
####  Puzzle Pieces  ####

Write a function that takes two arrays and adds the first element in the first array with the first element in the second array, the second element in the first array with the second element in the second array, etc, etc. Return true if all element combinations add up to the same number. Otherwise, return false.


[Examples]

___
puzzlePieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ true
// 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
// Both arrays sum to [5, 5, 5, 5]

puzzlePieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ true

puzzlePieces([1, 2], [-1, -1]) ➞ false

puzzlePieces([9, 8, 7], [7, 8, 9, 10]) ➞ false
_____



[Notes]

___
*) Each array will have at least one element.
*) Return false if both arrays are of different length.
___



[arrays] [higher_order_functions] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________
_________
Sum of Elements of a Vector
https://www.geeksforgeeks.org/how-to-find-the-sum-of-elements-of-a-vector-using-stl-in-c/
Given a vector, find the sum of the elements of this vector using STL in C++.
_________

*/
//Your code should go here:

