/*
####  XOR Swap Algorithm  ####

This is more informational than a challenge. You can actually switch 2 variables with the XOR operation ^. XOR works with two arguments. It turns both arguments into their binary representations, and for each bit, returns 1 if they are different, 0 otherwise.
The return value is the decimal representation of the new binary string. So, if you don't know how to do it, go play around with it! After some time on paper, you will understand what is going on, and how it works.
Your job is to switch 2 variables using the XOR operator, which means your return statement should be return std::make_pair(a, b), but the variables need to be switched.


[Examples]

___
XOR(10, 41) ➞ (41, 10)

XOR(69, 420) ➞ (420, 69)

XOR(12345, 890412) ➞ (890412, 12345)
_____



[Notes]

___
*) Remember to use std::make_pair() instead of just make_pair() (if you don't put using namespace std after #include <utility>).
*) If you're stuck, or don't have time to test out different cases, check the Resources tab.
___



[bit_operations] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Xor swap algorithm
https://en.wikipedia.org/wiki/XOR_swap_algorithm
Is an algorithm that uses the XOR bitwise operation to swap values of distinct variables having the same data type without using a temporary variable. "Distinct" means …
_________
_________
Swap Two Variables Using XOR
https://betterexplained.com/articles/swap-two-variables-using-xor/
It almost seems like magic – the the same statement is repeated 3 times and voila – the values magically swap? Let’s take a closer look.
_________
_________
std::tuple, std::pair
https://www.geeksforgeeks.org/returning-multiple-values-from-a-function-using-tuple-and-pair-in-c/
There can be some instances where you need to return multiple values (may be of different data types ) while solving a problem. One method to do the same is by using po …
_________

*/
//Your code should go here:

