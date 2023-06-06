/*
####  Oddly Or Evenly Positioned  ####

Write a function that returns the items from an array (given as parameter r) on odd or even positions, depending on it's specifier (given as parameters) as being the parity. The final array will contain "odd" items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).


[Examples]

___
charAtPos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
// 4 & 8 occupy the 4th & 2nd positions from right.

charAtPos(['E', 'D', 'A', 'B', 'I', 'T'], "odd") ➞ ['D', 'B', 'T']
// D, B and T occupy the 5th, 3rd and 1st positions from right.

charAtPos([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "odd") ➞ ["(", "&", "%", "#", "!"]
_____



[Notes]

___
*) Arrays are zero-indexed, so, index+1 = position or position-1 = index.
*) There will not be an empty string or an empty array.
*) The sequence of the items in the resulting array should be retained (i.e. example #1 - 8 should come after 4 and not otherwise, example #2 - 'B' should come after 'D' and before 'T').
___



[arrays] [functional_programming] [validation] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

