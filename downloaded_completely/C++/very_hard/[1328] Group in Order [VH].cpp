/*
####  Group in Order  ####

Create a function that groups an array of numbers based on a size parameter. The size represents the maximum length of each sub-array.
___
[1, 2, 3, 4, 5, 6], 3
[[1, 3, 5], [2, 4, 6]]
// Divide array into groups of size 3.

[1, 2, 3, 4, 5, 6], 2
[[1, 4], [2, 5], [3, 6]]
// Divide array into groups of size 2.

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4
[[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9]]
// "Leftover" arrays are okay.
_____



[Examples]

___
group([1, 2, 3, 4], 2) ➞ [[1, 3], [2, 4]]

group([1, 2, 3, 4, 5, 6, 7], 4) ➞ [[1, 3, 5, 7], [2, 4, 6]]

group([1, 2, 3, 4, 5], 1) ➞ [[1], [2], [3], [4], [5]]

group([1, 2, 3, 4, 5, 6], 4) ➞ [[1, 3, 5], [2, 4, 6]]
_____



[Notes]

___
*) The size parameter represents the maximum size for each sub-array (see ex.4). You should try to fill each sub-array evenly. In other words, ex.4 should be [[1, 3, 5], [2, 4, 6]], not [[1, 3, 5, 6], [2, 4]].
*) Keep the relative order of the numbers in each sub-array the same as the order in the original array.
*) When distributing the numbers into the sub-arrays, each sub-array should have a number in it prior to receiving a new number (e.g. for example 1, your sub-arrays will be of size 2, and because there are 4 numbers, you will need 2 sub-arrays. When interating through the original array to fill the sub-arrays it should go [[],[]] -> [[1],[]] -> [[1],[2]] -> [[1, 3], [2]] -> [[1, 3], [2, 4]]).
___



[arrays] [closures] [scope] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________

*/
//Your code should go here:

