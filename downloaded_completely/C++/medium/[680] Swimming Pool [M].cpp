/*
####  Swimming Pool  ####

Suppose a swimming pool blueprint can be represented as a 2D array, where 1s represent the pool and 0s represent the rest of the backyard.
___
[[0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
// Legitimate
_____

Suppose a pool is considered legitimate if it does not touch any of the four borders in this 2D array.
___
[[1, 1, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]
// Illegitimate! 
// The 1s are touching both the left "fence" and the upper "fence".
_____

Create a function that returns true if the pool plan is legitimate, and false otherwise.


[Examples]

___
isLegitimate([
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]
]) ➞ true

isLegitimate([
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 0, 0],
  [0, 0, 1, 1, 1, 0, 0, 0]
]) ➞ false

isLegitimate([
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0]
]) ➞ true
_____



[Notes]

N/A


[arrays] [higher_order_functions] [validation] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

