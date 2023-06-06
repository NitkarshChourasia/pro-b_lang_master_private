/*
####  Dead End Number Sequence  ####

This number sequence can start with any positive integer n. s is the sum of the individual digits in n. If s divides into n evenly then the next term of the series is n//s. Otherwise the next term is n*s. Eventually the series will reach a dead end with two numbers alternating: 58, 754, 12064, 928, 17632, 928, 17632. This series has a length of 5 with 17632 as the last term.
Compose a function that takes a positive integer and returns its series length and its last term.


[Examples]

___
DeadEnd(5) ➞ [2, 1]

DeadEnd(11) ➞ [7, 11440]

DeadEnd(123456789) ➞ [2, 5555555505]

DeadEnd(101) ➞ [9, 136804096]
_____



[Notes]

All numbers in the sequence will be integers within the range 0 < n <= Int64.MaxValue


[loops] [numbers] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

