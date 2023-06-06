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
Legendre(5, 100) ➞ 24

Legendre(2, 128) ➞ 127

Legendre(3, 50) ➞ 22
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
math.floor() Method
https://docs.microsoft.com/en-us/dotnet/api/system.math.floor?view=net-5.0
Returns the largest integral value less than or equal to the specified number.
_________
_________
Math.pow() Method
https://docs.microsoft.com/en-us/dotnet/api/system.math.pow?view=net-5.0
Returns a specified number raised to the specified power.
_________

*/
//Your code should go here:

