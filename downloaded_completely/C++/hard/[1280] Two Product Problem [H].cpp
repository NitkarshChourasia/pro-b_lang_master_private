/*
####  Two Product Problem  ####

Create a function that takes an array arr and a number n and returns an array of two integers from arr whose product equals n.


[Examples]

___
twoProduct([1, 2, -1, 4, 5], 20) ➞ [4, 5]

twoProduct([1, 2, 3, 4, 5], 10) ➞ [2, 5]

twoProduct([100, 12, 4, 1, 2], 15) ➞ []
_____



[Note:]

___
*) Try doing this with 0(N) time complexity.
*) No duplicates.
*) In the array, there can be multiple solutions so return the solution with the lowest sum of indexes of product pairs (i.e. N = 10, solutions = [[2, 5], [10, 1]], indexes = [[600, 3000], [800, 900]], return [10, 1]).
*) The array can have multiple solutions that share the lowest sum of indexes, so return the first full match that's found (as described above) that also has the lowest sum of indexes.
___



[conditions] [data_structures] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Vector
https://www.geeksforgeeks.org/vector-in-cpp-stl/
Are same as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automatically by the …
_________

*/
//Your code should go here:

