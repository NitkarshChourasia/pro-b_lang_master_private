/*
####  Digits Battle!  ####

Starting from the left side of an integer, adjacent digits pair up in "battle" and the larger digit wins. If two digits are the same, they both lose. A lone digit automatically wins.
Create a function that returns the victorious digits.
To illustrate:
___
battleOutcome(578921445) ➞ 7925
// [57]: 7 wins; [89] 9 wins; [21] 2 wins;
// [44] neither wins; 5 (automatically) wins
_____



[Examples]

___
battleOutcome(32531) ➞ 351
// 3 deffeats 2, 5 defeats 3, 1 is a single.

battleOutcome(111) ➞ 1
// 1 and 1 tie, so neither move on, last 1 is a single.

battleOutcome(78925) ➞ 895
_____



[Notes]

___
*) There are no winners in a battle with equal digits (neither should be printed).
*) If the length of the number is odd, the lone digit should be printed at the end of the number.
___



[games] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
How to Get the Seperate Digits of an Int Number
https://stackoverflow.com/questions/3389264/how-to-get-the-separate-digits-of-an-int-number
How do we separate the digits to check them separately?
_________

*/
//Your code should go here:

