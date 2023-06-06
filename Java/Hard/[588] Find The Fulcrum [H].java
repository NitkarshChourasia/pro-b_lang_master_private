/*
####  Find The Fulcrum  ####

A fulcrum of a list is an integer such that all elements to the left of it and all elements to the right of it sum to the same value. Write a function that finds the fulcrum of a list.
To illustrate:
___
findFulcrum([3, 1, 5, 2, 4, 6, -1]) ➞ 2
// Since [3, 1, 5] and [4, 6, -1] both sum to 9
_____



[Examples]

___
findFulcrum([1, 2, 4, 9, 10, -10, -9, 3]) ➞ 4

findFulcrum([9, 1, 9]) ➞ 1

findFulcrum([5, 4, 4, 4, 6, 6, 6]) ➞ -1

findFulcrum([7, -1, 0, -1, 1, 1, 2, 3]) ➞ 0

findFulcrum([8, 8, 8, 8]) ➞ -1
_____



[Notes]

___
*) If the fulcrum does not exist, return -1 (see example #3).
*) Exclude the leftmost and rightmost elements when computing the fulcrum (it doesn't make sense to sum zero values).
*) If a list has multiple fulcrums, return the one that occurs first.
___



[arrays] [loops] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

