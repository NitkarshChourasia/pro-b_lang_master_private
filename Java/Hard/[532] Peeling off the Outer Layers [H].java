/*
####  Peeling off the Outer Layers  ####

Given an array of object arrays, return a new array of object arrays containing every element, except for the outer elements.


[Examples]

___
peelLayer([
  ['a', 'b', 'c', 'd'],
  ['e', 'f', 'g', 'h'],
  ['i', 'j', 'k', 'l'],
  ['m', 'n', 'o', 'p']
]) ➞ [
  ['f', 'g'],
  ['j', 'k']
]

peelLayer([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
  [26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35]
]) ➞ [
  [7, 8, 9],
  [12, 13, 14],
  [17, 18, 19],
  [22, 23, 24],
  [27, 28, 29]
]

peelLayer([
  [true, false, true],
  [false, false, true],
  [true, true, true]
]) ➞ [[false]]

peel_layer_off([
  ["hello", "world"],
  ["hello", "world"]
]) ➞ []
_____



[Notes]

___
*) The 2D grid is always a rectangular/square shape.
*) Always return some form of nested array, unless there are no elements. In that case, return an empty array.
___



[arrays] [language_fundamentals] [loops] 



-------------------------------------------------------------------
[Resources]
_________
copyOfRange
https://docs.oracle.com/javase/7/docs/api/java/util/Arrays.html#copyOfRange(T[],%20int,%20int)
Copies the specified range of the specified array into a new array. The initial index of the range (from) must lie between zero and original.length, inclusive. The valu …
_________
_________
stream(T[] array) Method
https://www.geeksforgeeks.org/arrays-stream-method-in-java/
Is used to get a Sequential Stream from the array passed as the parameter with its elements. It returns a sequential Stream with the elements of the array, passed as pa …
_________

*/
//Your code should go here:

