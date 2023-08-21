/*
####  Dividing into Chunks of Maximum Sum N  ####

Write a function that divides an array into chunks such that the sum of each chunk is <= n. Start from the left side of the array and move to the right.


[Examples]

___
divide([1, 2, 3, 4, 1, 0, 2, 2], 5)
➞ [[1, 2], [3], [4, 1, 0], [2, 2]]

divide([1, 0, 1, 1, -1, 0, 0], 1)
➞ [[1, 0], [1], [1, -1, 0, 0]]

divide([2, 1, 0, -1, 0, 0, 2, 1, 3], 3)
➞ [[2, 1, 0, -1, 0, 0], [2, 1], [3]]
_____



[Notes]

___
*) The max of the array will always be smaller than or equal to n.
*) Use the greedy approach when solving the problem (e.g. fit as many elements you can into a chunk as long as you satisfy the sum constraint).
___



[arrays] [functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
How to sum up elements of a vector?
https://www.tutorialspoint.com/how-to-sum-up-elements-of-a-cplusplus-vector#:~:text=Sum%20up%20of%20all%20elements,vector%20to%20the%20specified%20sum.
Can be very easily done by std::accumulate method. It is defined in <numeric> header. It accumulates all the values present specified in the vector to the specified sum.
_________

*/
//Your code should go here:

