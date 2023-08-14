"""
####  Untouchable Numbers  ####

A positive number greater than 1 can be defined untouchable when it's not equal to the sum of the proper divisors (called also aliquot sum) of any other positive number, in a range starting from 2 and ending with the square of the given number (bounds included).
Given an integer number, implement a function that returns:
___
*) True if the given number is untouchable.
*) A list containing the numbers whose proper divisors sum is equal to the number, if the given number is not untouchable.
*) A string "Invalid Input" if the given number is lower than 2.
___



[Examples]

___
is_untouchable(2) ➞ True
# Range: 2 to 4
# 2 = 1  |  3 = 1  |  4 = 1+2 = 3
# No sum is equal to the given number

is_untouchable(3) ➞ [4]
# Range: 2 to 9
# As in the example above, 4 = 1+2 = 3

is_untouchable(6) ➞ [6, 25]
# Range: 2 to 36
# 6 = 1+2+3 = 6  |  25 = 1+5 = 6

is_untouchable(1) ➞ "Invalid Input"
# The given number is lower than 2
_____



[Notes]

___
*) The proper divisors of a number are, merely, all its divisors less the number itself.
*) More than a number can have a proper divisors sum equal to the given number, with given number included (see example #3).
*) Trivia: As far as we know, numbers 2 and 5 are the only two primes present in the sequence, with 5 being the only odd number present; by the way, these two assertions are still unproofed.
___



[algorithms] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
range() Method
https://www.programiz.com/python-programming/methods/built-in/range
Returns an immutable sequence of numbers between the given start integer to the stop integer.
_________
_________
sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
Aliquot Sum
https://en.wikipedia.org/wiki/Aliquot_sum
The aliquot sum s(n) of a positive integer n is the sum of all proper divisors of n, that is, all divisors of n other than n itself. It can be used to characterize the …
_________
_________
Untouchable Number
https://en.wikipedia.org/wiki/Untouchable_number
A positive integer that cannot be expressed as the sum of all the proper divisors of any positive integer (including the untouchable number itself). That is, these numb …
_________

"""
#Your code should go here:

