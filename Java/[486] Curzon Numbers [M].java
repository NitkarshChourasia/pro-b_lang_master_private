/*
####  Curzon Numbers  ####

Given a positive integer n and if 1 plus 2 times n exactly divides 1 plus 2 raised to the power n, then n is said to be a Curzon number.
Write a function that determines whether a number is a Curzon number or not.


[Examples]

___
isCurzon(5) ➞ true
// 2 ** 5 + 1 = 33
// 2 * 5 + 1 = 11
// 33 is a multiple of 11

isCurzon(10) ➞ false
// 2 ** 10 + 1 = 1025
// 2 * 10 + 1 = 21
// 1025 is not a multiple of 21

isCurzon(14) ➞ true
// 2 ** 14 + 1 = 16385
// 2 * 14 + 1 = 29
// 16385 is a multiple of 29
_____



[Notes]

___
*) Use BigInteger or BigDecimal classes to deal with extremely big numbers.
___



[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Curzon Numbers
https://www.geeksforgeeks.org/curzon-numbers/
Given an integer N, check whether the given number is a Curzon Number or not.
_________
_________
BigInteger pow() method
https://www.geeksforgeeks.org/biginteger-pow-method-in-java/
Is used to calculate a BigInteger raise to the power of some other number passed as exponent whose value is equal to (this)exponent.
_________

*/
//Your code should go here:

