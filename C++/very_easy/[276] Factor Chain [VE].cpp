/*
####  Factor Chain  ####

A factor chain is an array where each previous element is a factor of the next consecutive element. The following is a factor chain:
___
[3, 6, 12, 36]

// 3 is a factor of 6
// 6 is a factor of 12
// 12 is a factor of 36
_____

Create a function that determines whether or not an array is a factor chain.


[Examples]

___
factorChain([1, 2, 4, 8, 16, 32]) ➞ true

factorChain([1, 1, 1, 1, 1, 1]) ➞ true

factorChain([2, 4, 6, 7, 12]) ➞ false

factorChain([10, 1]) ➞ false
_____



[Notes]

N/A


[arrays] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Find All Divisors of a Natural Number
https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
A naive solution would be to iterate all the numbers from 1 to n, checking if that number divides n and printing it. Below is program for the same. If we look carefully …
_________

*/
//Your code should go here:

