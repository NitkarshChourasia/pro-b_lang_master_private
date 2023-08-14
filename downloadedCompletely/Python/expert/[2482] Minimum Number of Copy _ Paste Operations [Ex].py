"""
####  Minimum Number of Copy / Paste Operations  ####

Initially, the string consists of a single character. There are two operations:
___
*) Copy the entire string into a buffer. It is not allowed to copy a part of the current string.
*) Paste the buffer content at the end of the string. The string length increases.
___

Each operation counts as one.
The function is given n the length of the required string. Determine the minimum number of operations needed to make the resulting string exactly of length n.


[Examples]

___
min_ops(1) ➞ 0
# The string is already of the required length

min_ops(2) ➞ 2
# Copy, Paste -> 2 operations

min_ops(3) ➞ 3
# Copy, Paste, Paste -> 3 operations

min_ops(5) ➞ 5
# Copy, Paste, Paste, Paste, Paste -> 5 operations

min_ops(8) ➞ 6
# Copy, Paste, Copy, Paste, (the length is 4), Copy, Paste -> 6 operations

min_ops(9) ➞ 6
# Copy, Paste, Paste, (the length is 3), Copy, Paste, (the length is 6), Paste -> 6 operations
_____



[Notes]

The given range is 1 <= n < 2**21.


[algorithms] [conditions] [logic] [math] 



-------------------------------------------------------------------
[Resources]


[No Resources]


"""
#Your code should go here:

