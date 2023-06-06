/*
####  Hold Your Breath!  ####

You will be given an array of numbers which represent your character's altitude above sea level at regular intervals:
___
*) Positive numbers represent height above the water.
*) 0 is sea level.
*) Negative numbers represent depth below the water's surface.
___

Create a function which returns whether your character survives their unsupervised diving experience, given an array of integers.



[Worked Example]

___
divingMinigame([-5, -15, -4, 0, 5]) ➞ true

// Breath meter starts at 10.
// -5 is below water, so breath meter decreases to 8.
// -15 is below water, so breath meter decreases to 6.
// -4 is below water, so breath meter decreases to 4.
// 0 is at sea level, so breath meter increases to 8.
// 5 is above sea level and breath meter is capped at 10 (would've been 12 otherwise).
// Character survives!
_____



[Examples]

___
divingMinigame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ true

divingMinigame([-3, -6, -2, -6, -2]) ➞ false

divingMinigame([2, 1, 2, 1, -3, -4, -5, -3, -4]) ➞ false
_____



[Notes]

___
*) Lists may be of any length.
*) All arrays are valid.
___



[arrays] [conditions] [games] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

