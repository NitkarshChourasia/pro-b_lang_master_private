"""
####  Find the Lowest Neighbor of a 2D Vector Element  ####

Create a function that returns the lowest neighbor of a given (x, y) coordinate element in a 2D list. The function will be passed three parameters.
___
 vec,  x,  y
_____

___
*) vec will be a 2D list holding integer values and will always be symmetrical in size (e.g. 2x2, 3x3, 4x4).
*) x will hold the row coordinate, while y will hold the column coordinate.
___

You will have to check the horizontal, vertical and diagonal neighbor elements. If there isn't any lower neighbors, return the value of the given (x, y) coordinate.


[Examples]

___
lowest_element([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
], 1, 1) ➞ 1


[
  [1, 2, 3]
  [4, 5, 6]  # (1, 1) holds the integer 5. Check the surrounding neighbors.
  [7, 8, 9]
]
_____

___
lowest_element([
  [9, 8, 7],
  [0, -1, -3],
  [-5, -9, 54]
], 0, 0) ➞ -1


[
  [9, 8, 7]   # (0, 0) holds the integer 9. Check the surrounding neighbors.
  [0, -1, -3]
  [-5, -9, 54]
]
_____



[Notes]

N/A


[algorithms] [arrays] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Find Lowest Neighbor Matlab
https://stackoverflow.com/questions/13311848/find-lowest-neighbor-matlab
That for each pixel in a map finds the eight neighbors to the pixel, and returns two matrices with both the row and column offsets to the lowest neighbor (uses the numb …
_________

"""
#Your code should go here:

