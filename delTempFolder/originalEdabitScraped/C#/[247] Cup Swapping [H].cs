/*
####  Cup Swapping  ####

There are three cups on a table, at positions A, B, and C. At the start, there is a ball hidden under the cup at position B.

However, I perform several swaps on the cups, which is notated as two letters. For example, if I swap the cups at positions A and B, I could notate this as AB or BA.
Create a function that returns the letter position that the ball is at, once I finish swapping the cups. The swaps will be given to you as an array.


[Worked Example]

___
cupSwapping(["AB", "CA", "AB"]) ➞ "C"

// Ball begins at position B.
// Cups A and B swap, so the ball is at position A.
// Cups C and A swap, so the ball is at position C.
// Cups A and B swap, but the ball is at position C, so it doesn't move.
_____



[Examples]

___
cupSwapping(["AB", "CA"]) ➞ "C"

cupSwapping(["AC", "CA", "CA", "AC"]) ➞ "B"

cupSwapping(["BA", "AC", "CA", "BC"]) ➞ "A"
_____



[Notes]

___
*) A swap could be notated in two different ways, since both ways end up with the same outcome.
*) All swaps will be notated as capital letters and will be valid.
*) You cannot swap a cup with itself.
___



[algorithms] [interview] [logic] 



-------------------------------------------------------------------
[Resources]
_________
contains() Method
https://docs.microsoft.com/en-us/dotnet/api/system.string.contains?view=net-5.0
Returns a value indicating whether a specified substring occurs within the string.
_________

*/
//Your code should go here:

