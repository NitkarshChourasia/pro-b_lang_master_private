/*
####  Spin Around, Touch the Ground  ####

Given a list of directions to spin, "left" or "right", return an integer of how many full 360° rotations were made. Note that each word in the array counts as a 90° rotation in that direction.


[Worked Example]

___
spinAround(["right", "right", "right", "right", "left", "right"]) ➞ 1
// You spun right 4 times (90 * 4 = 360)
// You spun left once (360 - 90 = 270)
// But you spun right once more to make a full rotation (270 + 90 = 360)
_____



[Examples]

___
spinAround(["left", "right", "left", "right"]) ➞ 0

spinAround(["right", "right", "right", "right", "right", "right", "right", "right"]) ➞ 2

spinAround(["left", "left", "left", "left"]) ➞ 1
_____



[Notes]

___
*) Return a positive number.
*) All tests will only include the words "right" and "left".
___



[arrays] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
std::string::at
http://www.cplusplus.com/reference/string/string/at/
Returns a reference to the character at position pos in the string. The function automatically checks whether pos is the valid position of a character in the string (i …
_________

*/
//Your code should go here:

