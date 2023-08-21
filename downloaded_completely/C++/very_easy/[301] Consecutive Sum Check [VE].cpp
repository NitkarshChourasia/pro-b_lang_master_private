/*
####  Consecutive Sum Check  ####

Create a function that takes a number n as an argument and checks whether the given number can be expressed as a sum of two or more consecutive positive numbers.


[Examples]

___
consecutiveSum(9) ➞ true
// 9 can be expressed as a sum of (2 + 3 + 4) or (4 + 5).

consecutiveSum(10) ➞ true
// 10 can be expressed as a sum of 1 + 2 + 3 + 4.

consecutiveSum(64) ➞ false
_____



[Notes]

N/A


[bit_operations] [logic] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Modulo Operation
https://en.wikipedia.org/wiki/Modulo_operation#:~:text=Given%20two%20positive%20numbers%20a,and%20n%20is%20the%20divisor.&text=Although%20typically%20performed%20with%20a,other%20types%20of%20numeric%20operands.
In computing, the modulo operation returns the remainder or signed remainder of a division, after one number is divided by another (called the modulus of the operation).
_________
_________
Binary Logarithm
https://en.wikipedia.org/wiki/Binary_logarithm
In mathematics, the binary logarithm (log2 n) is the power to which the number 2 must be raised to obtain the value n. That is, for any real number x, {\displaystyle x …
_________
_________
Bit Twiddling Hacks
http://www.graphics.stanford.edu/~seander/bithacks.html
Alternatively, if you prefer the result be either -1 or +1, then use: sign = +1 | (v >> (sizeof(int) * CHAR_BIT - 1)); // if v < 0 then -1, else +1...
_________

*/
//Your code should go here:

