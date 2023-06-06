/*
####  Oddly or Evenly Positioned from Last  ####

Create a function that extracts the items from a unique array, given as parameter arr, filtered by positional parity (odd or even), given as parameter par. Return an array of items on odd positions (... 5, 3, 1) and on even positions (... 6, 4, 2) starting from the last item in the array.


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
*) The sequence of the items in the resulting array should be retained (i.e. Example #1 - 8 should come after 4 and not otherwise, example #2 - 'B' should come after 'D' and before 'T').
*) A recursive version of this challenge can be found via this link.
___



[algorithms] [arrays] [logic] 



-------------------------------------------------------------------
[Resources]
_________
The Remainder or Modulus Operator
http://www.cs.ukzn.ac.za/~hughm/java/intro/week2/21.html
Java has one important arithmetical operator you may not be familiar with, %, also known as the modulus or remainder operator. The % operator returns the remainder of t …
_________

*/
//Your code should go here:

