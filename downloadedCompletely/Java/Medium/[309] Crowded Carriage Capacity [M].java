/*
####  Crowded Carriage Capacity  ####

A train has a maximum capacity of n passengers overall, which means each carriage's capacity will share an equal proportion of the maximum capacity.
Create a function which returns the index of the first carriage which holds 50% or less of its maximum capacity. If no such carriage exists, return -1.


[Worked Examples]

___
findSeat(200, [35, 23, 18, 10, 40]) ➞ 2
// There are 5 carriages which each have a maximum capacity of 40 (200 / 5 = 40).
// Index 0's carriage is too full (35 is 87.5% of the maximum).
// Index 1's carriage is too full (23 is 57.5% of the maximum).
// Index 2's carriage is good enough (18 is 45% of the maximum).
// Return 2.
_____



[Examples]

___
findSeat(20, [3, 5, 4, 2]) ➞ 3

findSeat(1000, [50, 20, 80, 90, 100, 60, 30, 50, 80, 60]) ➞ 0

findSeat(200, [35, 23, 40, 21, 38]) ➞ -1
_____



[Notes]

___
*) If a train can hold 200 passengers, and has 5 carriages, then that means that each carriage can hold a maximum of 40 passengers each.
*) All carriage numbers will be positive integers, which will be able to divide evenly.
*) Remember to return -1 if no carriage is empty enough.
___



[interview] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Percentage Calculator
https://www.bing.com/search?q=calculate+percentage+of+percentage&cvid=f31dcdf2b29a4ab4b38ce9e54a7fd31a&aqs=edge.1.69i57j0l8.16677j0j1&pglt=417&FORM=ANNTA1&PC=VALBAN
In mathematics, a percentage (from Latin per centum "by a hundred") is a number or ratio expressed as a fraction of 100. It is often denoted using the percent sign, "%" …
_________

*/
//Your code should go here:

