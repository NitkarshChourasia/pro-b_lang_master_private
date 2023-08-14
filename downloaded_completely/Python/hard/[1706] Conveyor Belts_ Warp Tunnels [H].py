"""
####  Conveyor Belts, Warp Tunnels  ####

In this challenge, you have to deal with a matrix that is moving from the left to the right by a given amount of times, shifting its items as in a conveyor belt. At the end of the last list inside the matrix, there's a warp tunnel. The warp tunnel made appear the elements pushed through by the shifts at the beginning of the matrix, in the same order as they were before the shift. Look at the example below:
___
# Before the movement.
mtx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 2

# After the movement (2 shifts to the right).
mtx = [[8, 9, 1], [2, 3, 4], [5, 6, 7]]

# Shifting 2 times to the right, "8" and "9" are pushed through the warp tunnel.
# The warped elements appear at the start.
_____

Given a matrix mtx and an integer n, implement a function that returns the same matrix with its elements shifted n times.


[Examples]

___
warp_tunnel([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2) ➞ [[8, 9, 1], [2, 3, 4], [5, 6, 7]]

warp_tunnel([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 8) ➞ [[2, 3, 4], [5, 6, 7], [8, 9, 1]]

warp_tunnel([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) ➞ [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

warp_tunnel([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 18) ➞ [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
_____



[Notes]

___
*) The given matrices are regular (each list shares the same number of elements contained) with variable lengths and the number of lists contained.
*) The returned matrix must have the same dimensions as the original.
*) The given n can be greater than the total number of elements inside the matrix (see example #4). Each time you reach a complete shift cycle (so that every element is back in its original position, see example #3), you have to start again.
___



[arrays] [data_structures] [loops] 



-------------------------------------------------------------------
[Resources]
_________
Rotate a List
https://www.geeksforgeeks.org/python-ways-to-rotate-a-list/
Shorthands and various short techniques to achieve this in one-liners or one word. This operation is quite essential in a programmer's life to achieve various tasks.
_________

"""
#Your code should go here:

