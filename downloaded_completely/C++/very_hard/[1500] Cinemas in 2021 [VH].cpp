/*
####  Cinemas in 2021  ####

Given an array of seats, return the maximum number of new people which can be seated, as long as there is at least a gap of 2 seats between people.
___
*) Empty seats are given as 0.
*) Occupied seats are given as 1.
*) Don't move any seats which are already occupied, even if they are less than 2 seats apart. Consider only the gaps between new seats and existing seats.
___



[Examples]

___
maximumSeating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) ➞ 2
// [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]

maximumSeating([0, 0, 0, 0]) ➞ 2
// [1, 0, 0, 1]

maximumSeating([1, 0, 0, 0, 0, 1]) ➞ 0
// There is no way to have a gap of at least 2 chairs when adding someone else.
_____



[Notes]

___
*) Notice how there may be several possibilities for assigning seats to people, but these cases won't affect the results.
*) All seats will be valid.
___



[algorithms] [arrays] [interview] [loops] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

