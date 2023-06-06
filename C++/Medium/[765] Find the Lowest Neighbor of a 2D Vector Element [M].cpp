/*
####  Find the Lowest Neighbor of a 2D Vector Element  ####

Create a function that returns the lowest neighbor of a given (x, y) coordinate element in a 2D vector. The function will be passed three parameters.
___
vector<vector<int>> vec, int x, int y
_____

___
*) vec will be a 2D vector holding integer values and will always be symmetrical in size (e.g. 2x2, 3x3, 4x4).
*) int x will hold the row coordinate, while int y will hold the column coordinate.
___

You will have to check the horizontal, vertical and diagonal neighbor elements. If there isn't any lower neighbors, return the value of the given (x, y) coordinate.


[Examples]

___
 lowestElement({
   {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
}, 1, 1) ➞ 1


{
  {1, 2, 3}
  {4, 5, 6}  // (1, 1) holds the integer 5. Check the surrounding neighbors.
  {7, 8, 9}
}
_____

___
lowestElement({
  {9, 8, 7},
  {0, -1, -3},
  {-5, -9, 54}
}, 0, 0) ➞ -1


{
  {9, 8, 7}  // (0, 0) holds the integer 9. Check the surrounding neighbors.
  {0, -1, -3}
  {-5, -9, 54}
}
_____



[Notes]

N/A


[algorithms] [arrays] [loops] [math] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

