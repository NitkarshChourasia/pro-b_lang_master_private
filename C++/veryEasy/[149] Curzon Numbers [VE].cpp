/*
####  Curzon Numbers  ####

In this challenge, establish if a given integer n is a Curzon number. If 1 plus 2 ^ n is exactly divisible by 1 plus 2 * n, then n is a Curzon number.
Given a non-negative integer n, implement a function that returns true if n is a Curzon number, or false otherwise.


[Examples]

___
is_curzon(5) ➞ true
# 1 + 2 ^ 5  = 33
# 1 + 2 * 5  = 11
# 33 is a multiple of 11

is_curzon(10) ➞ false
# 1 + 2 ^ 10  = 1025
# 1 + 2 * 10 = 21
# 1025 is not a multiple of 21

is_curzon(14) ➞ true
# 1 + 2 ^ 14  = 16385
# 1 + 2 * 14  = 29
# 16385 is a multiple of 29
_____



[Notes]

___
*) If you get stuck on a challenge, find help in the Resources tab.
*) If you're really stuck, unlock solutions in the Solutions tab.
___



[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
pow
http://www.cplusplus.com/reference/cmath/pow/
The result of raising base to the power exponent.
_________
_________
Curzon Numbers
https://www.geeksforgeeks.org/curzon-numbers/
Given an integer N, check whether the given number is a Curzon Number or not.
_________
_________
The Conditional Operator (?:)
http://www.cplusplus.com/articles/1AUq5Di1/
Is an operator used in C and C++ (as well as other languages, such as C#). The ?: operator returns one of two values depending on the result of an expression.
_________
_________
fmod
http://www.cplusplus.com/reference/cmath/fmod/
Returns the floating-point remainder of numer/denom (rounded towards zero): fmod = numer - tquot * denom Where tquot is the truncated (i.e., rounded towards zero) res …
_________

*/
//Your code should go here:

