/*
####  Legendre's Formula  ####

Legendre's formula finds the exponent of the largest power of some prime p that divides (is a factor of) the factorial of some number n.
Legendre's formula example (p = 2 and n = 27):

So 2^23 is the largest power of 2 that divides 27!.
The formula returns the sum of many fractions (rounded down) with n as the numerator and a steadily increasing power of p as the denominator, stopping when it exceeds the numerator.
To illustrate:
___
p = 5
n = 100

int(100/5) + int(100/25)
// No 100/125 because 125 > 100.
_____

___
p = 2
n = 128

int(128/2) + int(128/4) + int(128/8) + ... + int(128/128)
_____

Given p and n, return the result of Legendre's formula (see Resources).


[Examples]

___
legendre(5, 100) ➞ 24

legendre(2, 128) ➞ 127

legendre(3, 50) ➞ 22
_____



[Notes]

___
*) p and n will be positive integers.
*) When p exceeds n, the result should be 0.
___



[algebra] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Legendre's Formula
https://en.wikipedia.org/wiki/Legendre%27s_formula
Gives an expression for the exponent of the largest power of a prime p that divides the factorial n!. It is named after Adrien-Marie Legendre. It is also sometimes know …
_________
_________
Ceil and Floor Functions
https://www.geeksforgeeks.org/ceil-floor-functions-cpp/
Map a real number to the greatest preceding or the least succeeding integer, respectively. floor(x) : Returns the largest integer that is smaller than or equal to x (i …
_________
_________
pow
http://www.cplusplus.com/reference/cmath/pow/
Returns base raised to the power exponent.
_________

*/
//Your code should go here:

