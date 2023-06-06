/*
####  Gold Distribution  ####

Mubashir and his friend Matt found some gold piles. They decided to follow simple rules to distribute the gold among them.
___
*) Gold will be divided into n piles.
*) Each person will choose bigger gold pile either from far left or far right.
*) If the weight of both piles is equal then the person will choose left pile.
___

Help them by creating a function that takes an array of gold piles gold and returns a two-element array with [Mubashir's Gold, Matt's Gold].


[Examples]

___
goldDistribution([4, 2, 9, 5, 2, 7]) ➞ [14, 15]
// Mubashir will choose 7, Remaining piles = [4, 2, 9, 5, 2]
// Matt will choose 4, Remaining piles = [2, 9, 5, 2]
// Mubashir will choose 2, Remaining piles = [9, 5, 2]
// Matt will choose 9, Remaining piles = [5, 2]
// Mubashir will choose 5, Remaining piles = [2]
// Matt will choose 2
// Mubashir = 7+2+5 = 14, Matt = 4+9+2 = 15

goldDistribution([10, 1000, 2, 1]) ➞ [12, 1001]

goldDistribution([10, 9, 1, 2, 8, 4]) ➞ [16, 18]
_____



[Notes]

Mubashir gets to pick his gold first!


[algorithms] [arrays] [logic] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::vector::erase
http://www.cplusplus.com/reference/vector/vector/erase/
Removes from the vector either a single element (position) or a range of elements ([first, last)).
_________
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Vectors are sequence containers representing arrays that can change in size.
_________

*/
//Your code should go here:

