/*
####  A Simple Dance  ####

You will be given an array of dancing couples, with the woman first and man second, as well as a parameter "men" or "women".
___
*) If the parameter is "men", the men reverse their positions (first moves to last, last moves to first, etc), while women keep their positions.
*) If the parameter is "women", the women reverse their positions, while men keep their positions.
___



[Examples]

___
dance([
  [Ana, Bob],
  [Amy, Josh],
  [Lisa, Tim]
], "men") ➞ [
  [Ana, Tim],
  [Amy, Josh],
  [Lisa, Bob]
]

dance([
  [Ana, Bob],
  [Amy, Josh],
  [Lisa, Tim]
], "women") ➞ [
  [Lisa, Bob],
  [Amy, Josh],
  [Ana, Tim]
]
_____



[Notes]

Input arrays will always be the same length.


[arrays] [sorting] 



-------------------------------------------------------------------
[Resources]
_________
Vector of Vectors in C++
https://www.geeksforgeeks.org/vector-of-vectors-in-c-stl-with-examples/
Vectors are known as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatical …
_________

*/
//Your code should go here:

