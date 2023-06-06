/*
####  Roll the Dice  ####

Las Vegas style dice have 6 sides numbered 1 to 6. When rolling 2 dice, a six is 5 times more likely than a two because a six can be rolled 5 different ways (1 + 5, 5 + 1, 2 + 4, 4 + 2, 3 + 3), while a two can only be rolled 1 way (1 + 1).
Create a function that accepts two arguments:the number of dice rolled, and the outcome of the roll. The function returns the number of possible combinations that could produce that outcome. The number of dice can vary from 1 to 6.
For the example given above:
___
*) diceRoll(2, 6) would return 5
*) diceRoll(2, 2) would return 1
___



[Examples]

___
diceRoll(1, 3) ➞ 1

diceRoll(2, 5) ➞ 4
// 1 + 4, 4 + 1, 2 + 3, 3 + 2

diceRoll(3, 4) ➞ 3
// 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1

diceRoll(4, 18) ➞ 80

diceRoll(6, 20) ➞ 4221
_____



[Notes]

1 + 5 and 5 + 1 are distinct combinations because die #1 can show 1 while die #2 can show 5, or die #1 can show 5 while die #2 can show 1.


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Number of Ways to Split N as Sum of K Numbers From the Given Range
https://www.geeksforgeeks.org/number-of-ways-to-split-n-as-sum-of-k-numbers-from-the-given-range/
How to split N as sum of K numbers lying in the range [L, R].
_________

*/
//Your code should go here:

