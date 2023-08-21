/*
####  Back and Forth  ####

In a board game, a player may pick up a card with several left or right facing arrows, with the number of arrows indicating the number of tiles to move. The player should move either left or right, depending on the arrow's direction.
Given an array of the arrows contained on a player's cards, return a singular string of arrowheads that are equivalent to all of the arrowheads.


[Worked Example]

___
calculateArrowhead([">>", "<<", "<<<"]) ➞ "<<<"
// >> means to move 2 places right
// << means to move 2 places left (cancelling out >>)
// <<< means to move a further 3 places left
// overall, the movement can be written as <<<
_____



[Examples]

___
calculateArrowhead([">>>>", "<", "<", "<"]) ➞ ">"

calculateArrowhead([">", "<", ">>", "<", "<<<"]) ➞ "<<"

calculateArrowhead([">>>", "<<<"]) ➞ ""
_____



[Notes]

Return an empty string if all the arrowheads cancel out.


[algorithms] [arrays] [strings] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________
_________
std::string::append
http://www.cplusplus.com/reference/string/string/append/
Extends the string by appending additional characters at the end of its current value.
_________
_________
string::size
http://www.cplusplus.com/reference/string/string/size/
Returns the length of the string, in terms of bytes.
_________
_________
The Conditional Operator (?:)
http://www.cplusplus.com/articles/1AUq5Di1/
Returns one of two values depending on the result of an expression.
_________

*/
//Your code should go here:

