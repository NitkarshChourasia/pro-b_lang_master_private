/*
####  Balancing Scales  ####

Given an array with an odd number of elements, return whether the scale will tip "left" or "right" based on the sum of the numbers. The scale will tip on the direction of the largest total. If both sides are equal, return "balanced".


[Examples]

___
scaleTip([0, 0, -1, 1, 1]) ➞ "right"
// 0 < 2 so it will tip right

scaleTip([1, 2, 3, -1, 4, 0, 0]) ➞ "left"
// 6 > 4 so it will tip left

scaleTip([5, 5, 5, 0, -1, 10, 2, 2, 1]) ➞ "balanced"
// 15 = 15 so it will stay balanced
_____



[Notes]

___
*) The middle element will always be -1 so you can just ignore it.
*) Assume the numbers all represent the same unit.
*) Both sides will have the same number of elements.
*) There are no such things as negative weights in both real life and the tests!
___



[algorithms] [arrays] [conditions] 



-------------------------------------------------------------------
[Resources]
_________
For Loop
https://www.w3schools.com/cpp/cpp_for_loop.asp
When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop.
_________
_________
std::accumulate
https://cplusplus.com/reference/numeric/accumulate/
Returns the result of accumulating all the values in the range [first,last) to init.
_________

*/
//Your code should go here:

