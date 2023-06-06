/*
####  Eight Sums Up  ####

Create a function that gets every pair of numbers from an array that sums up to eight and returns it as an array of pairs (sorted ascendingly). See the following examples for more details.


[Examples]

___
sumsUp({1, 2, 3, 4, 5}) ➞ {{3, 5}}

sumsUp({1, 2, 3, 7, 9}) ➞ {1, 7}}

sumsUp({10, 9, 7, 2, 8}) ➞ {}

sumsUp({1, 6, 5, 4, 8, 2, 3, 7}) ➞ {{2, 6}, {3, 5}, {1, 7}}
// [6, 2] first to complete the cycle (to sum up to 8)
// [5, 3] follows
// [1, 7] lastly
// the pair that completes the cycle is always found on the left
// [2, 6], [3, 5], [1, 7] sorted according to cycle completeness, then pair-wise.
_____



[Notes]

___
*) Remember the idea of "completes the cycle first" when getting the sort order of the pairs.
*) Only unique numbers are present in the array.
*) Return an empty array if nothing sums up to eight.
___



[algorithms] [arrays] [numbers] [objects] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

