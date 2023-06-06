/*
####  Smallest Missing Positive Integer  ####

Given an array of integers, return the smallest positive integer not present in the array.
Here is a representative example. Consider the array:
___
{ -2, 6, 4, 5, 7, -1, 7, 1, 3, 6, 6, -2, 9, 10, 2, 2 }
_____

After reordering, the array becomes:
___
{ -2, -2, -1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 7, 9, 10 }
_____

... from which we see that the smallest missing positive integer is 8.


[Examples]

___
MinMissPos({ -2, 6, 4, 5, 7, -1, 1, 3, 6, -2, 9, 10, 2, 2 }) ➞ 8
// After sorting, the array becomes { -2, -2, -1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 9, 10 }
// So the smallest missing positive integer is 8

MinMissPos({ 5, 9, -2, 0, 1, 3, 9, 3, 8, 9 }) ➞ 2
// After sorting, the array becomes [-2, 0, 1, 3, 3, 5, 8, 9, 9, 9 }
// So the smallest missing positive integer is 2

MinMissPos({ 0, 4, 4, -1, 9, 4, 5, 2, 10, 7, 6, 3, 10, 9 }) ➞ 1
// After sorting, the array becomes { -1, 0, 2, 3, 4, 4, 4, 5, 6, 7, 9, 9, 10, 10 }
// So the smallest missing positive integer is 1
_____



[Notes]

For the sake of clarity, recall that 0 is not considered to be a positive number.


[arrays] [math] [numbers] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

