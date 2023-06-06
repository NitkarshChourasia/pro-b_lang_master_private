/*
####  Profitable Gamble  ####

Create a function that takes three arguments prob, prize, pay and returns true if prob * prize > pay; otherwise return false.
To illustrate:
___
ProfitableGamble(0.2, 50, 9)
_____

... should yield true, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.


[Examples]

___
ProfitableGamble(0.2, 50, 9) ➞ true

ProfitableGamble(0.9, 1, 2) ➞ false

ProfitableGamble(0.9, 3, 2) ➞ true
_____



[Notes]

A profitable gamble is a game that yields a positive net profit, where net profit is calculated in the following manner: net_outcome = probability_of_winning * prize - cost_of_playing.


[conditions] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Type Conversion
https://code-maze.com/csharp-basics-type-conversion/
In C#, data can be converted from one type to another by using an implicit conversion (automatic) or an explicit conversion (we can choose how it’s done).
_________

*/
//Your code should go here:

