"""
####  Dead End Number Sequence  ####

This number sequence can start with any positive integer n. s is the sum of the individual digits in n. If s divides into n evenly then the next term of the series is n//s. Otherwise the next term is n*s. Eventually the series will reach a dead end with two numbers alternating: 58, 754, 12064, 928, 17632, 928, 17632. This series has a length of 5 with 17632 as the last term.
Compose a function that takes a positive integer and returns its series length and its last term.


[Examples]

___
dead_end(5) ➞ (2, 1)

dead_end(11) ➞ (7, 11440)

dead_end(123456789) ➞ (2, 5555555505)

dead_end(35161) ➞ (39, 154838313273413215779502672965210112000)

dead_end(101) ➞ (9, 136804096)
_____



[Notes]

N/A


[loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
While Loops
https://www.w3schools.com/python/python_while_loops.asp
With the while loop we can execute a set of statements as long as a condition is true.
_________

"""
#Your code should go here:

