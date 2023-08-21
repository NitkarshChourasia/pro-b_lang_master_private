/*
####  Powerful Numbers  ####

Given a positive number x:
___
p = (p1, p2, …)
// Set of *prime* factors of x
_____

If the square of every item in p is also a factor of x, then x is said to be a powerful number.
Create a function that takes a number and returns true if it's powerful, false if it's not.


[Examples]

___
isPowerful(36) ➞ true
// p = (2, 3) (prime factors of 36)
// 2^2 = 4 (factor of 36)
// 3^2 = 9 (factor of 36)

isPowerful(27) ➞ true

isPowerful(674) ➞ false
_____



[Notes]

N/A


[conditions] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Guide to Powerful Numbers
https://www.geeksforgeeks.org/powerful-number/
The idea is based on the fact that if a number n is powerful, then all prime factors of it and their squares should be divisible by n. We find all prime factors of give …
_________
_________
Powerful Number
https://en.wikipedia.org/wiki/Powerful_number
A positive integer m such that for every prime number p dividing m, p2 also divides m. Equivalently, a powerful number is the product of a square and a cube, that is, a …
_________

*/
//Your code should go here:

