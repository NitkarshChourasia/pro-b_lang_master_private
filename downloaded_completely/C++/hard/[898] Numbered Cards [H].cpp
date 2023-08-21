/*
####  Numbered Cards  ####

You have a pack of 5 randomly numbered cards, which can range from 0-9. You can win if you can produce a higher two-digit number from your cards than your opponent. Return true if your cards win that round.


[Worked Example]

___
winRound([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ true
// Your cards can make the number 96
// Your opponent can make the number 73
// You win the round since 96 > 73
_____



[Examples]

___
winRound([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ true

winRound([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]) ➞ false

winRound([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]) ➞ false
_____



[Notes]

Return false if you and your opponent reach the same maximum number (see example #3).


[arrays] [games] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________
_________
std::sort()
https://www.geeksforgeeks.org/sort-c-stl/
It generally takes two parameters , the first one being the point of the array/vector from where the sorting needs to begin and the second parameter being the length up …
_________

*/
//Your code should go here:

