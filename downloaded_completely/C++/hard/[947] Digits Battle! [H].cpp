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
How can I extract pairs of values from a string?
https://stackoverflow.com/questions/44146034/how-can-i-extract-pairs-of-values-from-a-string-in-c
I have a string with this format: "name1":1234 " name2 " : 23456 "name3" : 12345 and so on... I have tried using nested while loops and two integers to store th …
_________

*/
//Your code should go here:

