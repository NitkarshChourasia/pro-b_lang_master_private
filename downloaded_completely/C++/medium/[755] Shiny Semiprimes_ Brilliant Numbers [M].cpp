/*
####  Shiny Semiprimes: Brilliant Numbers  ####

In this challenge, you have to establish if a given number is Brilliant. A Brilliant number is a semiprime that can be obtained only by multiplicating two, and only two, different primes with the same number of digits.
A semiprime can be:
___
*) A composite number equal to the product of two different primes.
*) A composite number equal to the square of a prime.
___

Given an integer n, implement a function that returns true if n is a Brilliant number, or false if it's not.


[Examples]

___
isBrilliant(11) ➞ false
// 11 is a prime.

isBrilliant(9) ➞ true
// 9 is equal to the square of a prime: 3²

isBrilliant(21) ➞ true
// 21 is equal to the product of two different primes: 3 x 7
// 3 and 7 have the same digital length.

isBrilliant(22) ➞ false
// 22 is equal to the product of two different primes: 2 x 11
// 2 and 11 have different digital lengths.
_____



[Notes]

___
*) The given n will be a positive integer greater than 0.
*) Remember that a Brilliant number is a semiprime that can be obtained only with a single combination of different primes having the same digital length.
___



[higher_order_functions] [loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Prime Number
https://en.wikipedia.org/wiki/Prime_number#:~:text=The%20first%2025%20prime%20numbers,sequence%20A000040%20in%20the%20OEIS).&text=as%20the%20product-,.,is%20called%20an%20odd%20prime.
A natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. Fo …
_________
_________
log10
http://www.cplusplus.com/reference/cmath/log10/
Returns the common (base-10) logarithm of x.
_________

*/
//Your code should go here:

