/*
####  Truncatable Primes  ####

A left-truncatable prime is a prime number that contains no 0 digits and, when the first digit is successively removed, the result is always prime.
A right-truncatable prime is a prime number that contains no 0 digits and, when the last digit is successively removed, the result is always prime.
Create a function that takes an integer as an argument and:
___
*) If the integer is only a left-truncatable prime, return "left".
*) If the integer is only a right-truncatable prime, return "right".
*) If the integer is both, return "both".
*) Otherwise, return "none".
___



[Examples]

___
truncatable(9137) ➞ "left"
// Because 9137, 137, 37 and 7 are all prime.

truncatable(5939) ➞ "right"
// Because 5939, 593, 59 and 5 are all prime.

truncatable(317) ➞ "both"
// Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.

truncatable(5) ➞ "both"
// The trivial case of single-digit primes is treated as truncatable from both directions.

truncatable(139) ➞ "none"
// 1 and 9 are non-prime, so 139 cannot be truncatable from either direction.

truncatable(103) ➞ "none"
// Because it contains a 0 digit (even though 103 and 3 are primes).
_____



[Notes]

The input integers will not exceed 10^6.


[loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Truncatable Prime
https://en.wikipedia.org/wiki/Truncatable_prime
A left-truncatable prime is a prime number which, in a given base, contains no 0, and if the leading ("left") digit is successively removed, then all resulting numbers …
_________
_________
AKS Primality Test
https://en.wikipedia.org/wiki/AKS_primality_test
A deterministic primality-proving algorithm created and published by Manindra Agrawal, Neeraj Kayal, and Nitin Saxena, computer scientists at the Indian Institute of Te …
_________
_________
Program to Check if a Number Is Prime or Not
https://www.geeksforgeeks.org/java-program-to-check-if-a-number-is-prime-or-not/
Given a positive integer, check if the number is prime or not. A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Example …
_________

*/
//Your code should go here:

