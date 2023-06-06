"""
####  Dividing into Chunks of Maximum Sum N  ####

Write a function that divides a list into chunks such that the sum of each chunk is <= n. Start from the left side of the list and move to the right.


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
*) The max of the list will always be smaller than or equal to n.
*) Use the greedy approach when solving the problem (e.g. fit as many elements you can into a chunk as long as you satisfy the sum constraint).
___



[arrays] [functional_programming] 



-------------------------------------------------------------------
[Resources]
_________
Python While Loops
https://www.w3schools.com/python/python_while_loops.asp
With the while loop we can execute a set of statements as long as a condition is true.
_________

"""
#Your code should go here:

