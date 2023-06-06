/*
####  Multi-division  ####

Create a function, that will for a given a, b, c, do the following:
___
*) Add a to itself b times.
*) Check if the result is divisible by c.
___



[Examples]

___
abcmath(42, 5, 10) ➞ false
// 42+42 = 84,84+84 = 168,168+168 = 336,336+336 = 672, 672+672 = 1344
// 1344 is not divisible by 10

abcmath(5, 2, 1) ➞ true

abcmath(1, 2, 3) ➞ false
_____



[Notes]

___
*) In the first step of the function, a doesn't always refer to the original a.
*) "if the result is divisible by c", means that if you divide the result and c, you will get an integer (5, and not 4.5314).
*) The second test is correct.
___



[algebra] [loops] [math] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Bitset Operators
http://www.cplusplus.com/reference/bitset/bitset/operators/
Performs the proper bitwise operation using the contents of the bitset.
_________

*/
//Your code should go here:

