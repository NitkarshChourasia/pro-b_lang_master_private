/*
####  Happy Numbers  ####

Given any number, we can create a new number by adding the sums of squares of digits of that number. For example, given 203, our new number is 4 + 0 + 9 = 13. If we repeat this process, we get a sequence of numbers:
___
203 -> 13 -> 10 -> 1 -> 1
_____

Sometimes, like with 203, the sequence reaches (and stays at) 1. Numbers like this are called happy.
Not all numbers are happy. If we started with 11, the sequence would be:
___
11 -> 2 -> 4 -> 16 -> ...
_____

This sequence will never reach 1, and so the number 11 is called unhappy.
Given a positive whole number, you have to determine whether that number is happy or unhappy.


[Examples]

___
isHappy(203) ➞ true

isHappy(11) ➞ false

isHappy(107) ➞ false
_____



[Notes]

___
*) You can assume (and it is actually true!) that all positive whole numbers are either happy or unhappy. Any happy number will have a 1 in its sequence, and every unhappy number will have a 4 in its sequence.
*) The only numbers passed to your function will be positive whole numbers.
___



[loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Happy Number
https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy%20number%20is%20a,For%20instance%2C%2013%20is%20a%20happy%20number%20because
Is a number which eventually reaches 1 when replaced by the sum of the square of each digit. For instance, 13 is a happy number because …
_________

*/
//Your code should go here:

