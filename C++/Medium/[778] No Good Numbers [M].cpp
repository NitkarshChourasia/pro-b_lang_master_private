/*
####  No Good Numbers  ####

A positive number's population is the sum of 1's in its binary representation.
___
*) An evil number has an even numbered population.
*) An odious number has an odd numbered population.
*) A number is pernicious if its population is a prime number.
___

Create a function that takes a number as an argument and returns a sorted array of all its descriptors ("Evil", "Odious", or "Pernicious").


[Examples]

___
howBad(7) ➞ ["Odious", "Pernicious"]
// 7 in binary is "111".
// 1 + 1 + 1 = 3 in "111" means "Odious" should be added to the array answer.
// 3 is a prime number, meaning "Pernicious" should also be added.

howBad(17) ➞ ["Evil", "Pernicious"]
// 17 in binary is "10001".
// 1 + 1 = 2 in "10001" means "Evil" should be added to the array answer.
// 2 is a prime number, meaning "Pernicious" should also be added.

howBad(23) ➞ ["Evil"]
// 23 in binary is "10111".
// Four 1's in "10111" means "Evil" should be added to the array answer.
// 4 is not a prime number, meaning "Pernicious" should not be added.
_____



[Notes]

N/A


[conditions] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
Program for Decimal to Binary Conversion
https://www.geeksforgeeks.org/program-decimal-binary-conversion/
Program for decimal to binary conversion.
_________
_________
Prime Number
https://en.wikipedia.org/wiki/Prime_number#:~:text=The%20first%2025%20prime%20numbers,sequence%20A000040%20in%20the%20OEIS).&text=as%20the%20product-,.,is%20called%20an%20odd%20prime.
Is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. …
_________
_________
Prime Number Program in C++
https://www.javatpoint.com/prime-number-program-in-cpp
Prime number is a number that is greater than 1 and divided by 1 or itself. In other words, prime numbers can't be divided by other numbers than itself or 1. For exampl …
_________

*/
//Your code should go here:

