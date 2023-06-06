"""
####  Digital Division  ####

In this challenge, you have to verify if a number is exactly divisible by a combination of its digits. There are three possible conditions to test:
___
*) The given number is exactly divisible by each of its digits excluding the zeros.
*) The given number is exactly divisible by the sum of its digits.
*) The given number is exactly divisible by the product of its digits.
___

Given an integer n, implement a function that returns:
___
*) If every test is true, a string "Perfect".
*) If some test is true, the number of true tests (1 or 2).
*) If every test is false, a string "Indivisible".
___



[Examples]

___
digital_division(21) ➞ 1
# Exactly divisible only by the sum of its digits (2 + 1 = 3).

digital_division(128) ➞ 2
# Exactly divisible by each of its digits.
# Exactly divisible by the product of its digits (1 * 2 * 8 = 16).

digital_division(100) ➞ 2
# Exactly divisible by each of its digits (excluding zeros).
# Exactly divisible by the sum of its digits (1 + 0 + 0 = 1).

digital_division(12) ➞ "Perfect"
# Exactly divisible by each of its digits.
# Exactly divisible by 3 (sum of digits = 1 + 2).
# Exactly divisible by 2 (product of digits = 1 * 2).

digital_division(31) ➞ "Indivisible"
# Every testing condition is false.
_____



[Notes]

___
*) Remember to exclude any 0-digit when testing if the given n is divisible by each of its digits (see example #3).
*) A number containing at least a 0-digit can't be exactly divided by the product of its digits (division by 0).
*) Trivially, every single-digit positive number greater than 0 is Perfect
*) Any given number will be a positive integer greater than 0.
___



[conditions] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Multiply All Numbers in the List
https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
Initialize the value of the product to 1(not 0 as 0 multiplied with anything returns zero). Traverse till the end of the list, multiply every number with the product. T …
_________

"""
#Your code should go here:

