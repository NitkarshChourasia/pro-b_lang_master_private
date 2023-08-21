/*
####  The Jumping Frog  ####

A frog wants to cross a river. Unfortunately, he can't jump across in a single leap. Luckily, there are n stones in the river.
The frog can jump from the near bank to stone 1 and from stone n to the far bank. He can also jump from stone to stone, forward and backward. However, on each stone, a number j is written and he must only jump exactly j stones backward or forward.
Return the minimum number of jumps to cross the river (including jumps to the first stone and from the last stone (or any other stone, if possible) to the far bank) or 0 if it's not possible to cross the river.


[Examples]

___
jumpingFrog(5, [1, 1, 1, 1, 1]) ➞ 6

jumpingFrog(5, [1, 3, 1, 1, 1]) ➞ 4

jumpingFrog(5, [1, 1, 0, 1, 1]) ➞ 0
_____



[Notes]

___
*) The frog may also reach the far bank from another stone than n if a large enough number is written on it.
*) n is at least 2.
___



[algorithms] [arrays] [conditions] [loops] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Vectors are sequence containers representing arrays that can change in size.
_________

*/
//Your code should go here:

