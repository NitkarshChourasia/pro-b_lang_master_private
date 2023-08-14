"""
####  Can You Make the Numbers?  ####

You are given a list representing the number of 0s, 1s, 2s, ..., 9s you have. The function will look like:
___
can_build([#0s, #1s, #2s, ..., #9s], [num1, num2, ...])
_____

Write a function that returns True if you can build the following numbers using only the digits you have.


[Examples]

___
can_build([0, 1, 2, 2, 3, 0, 0, 0, 1, 1], [123, 444, 92]) ➞ True

# You have: one 1, two 2s, two 3s, three 4s, one 8 and one 9
# Using only these digits, you can build 123, 444, and 92

can_build([10, 2, 3, 8, 5, 8, 5, 5, 3, 1], [11, 2, 22, 49, 444, 998, 87, 44]) ➞ False

can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], []) ➞ True

can_build([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3]) ➞ False
_____



[Notes]

N/A


[arrays] [higher_order_functions] [loops] [validation] 



-------------------------------------------------------------------
[Resources]
_________
String join() Method
https://www.w3schools.com/python/ref_string_join.asp
Takes all items in an iterable and joins them into one string. A string must be specified as the separator.
_________

"""
#Your code should go here:

