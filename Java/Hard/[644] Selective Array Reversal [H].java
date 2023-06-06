/*
####  Selective Array Reversal  ####

Create a function that takes an array and a number and selectively reverse the order of the array based on the number you're given (second argument). If you're given the arguments [1,2,3,4,5,6] and 2, you would return the array [2,1, 4,3, 6,5].


[Examples]

___
selReverse([1,2,3,4,5,6], 2) ➞ [2,1, 4,3, 6,5]

selReverse([2,4,6,8,10,12,14,16], 3) ➞ [6,4,2, 12,10,8, 16,14]

selReverse([5,7,2,6,0,4,6], 100) ➞ [6,4,0,6,2,7,5]
_____



[Notes]

___
*) If the array you're given can't be broken up into equal parts, just reverse the remaining numbers (see 2nd expample).
*) If len exceeds the array length, reverse everything.
*) If len is zero, return the original array.
___



[algorithms] [arrays] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Collections
https://www.geeksforgeeks.org/collections-in-java-2/
Any group of individual objects which are represented as a single unit is known as the collection of the objects. In Java, a separate framework named the “Collection Fr …
_________

*/
//Your code should go here:

