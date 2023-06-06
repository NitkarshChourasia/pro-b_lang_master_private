"""
####  Sum of Factors of Factors  ####

Create a function that takes a number and returns the sum of factors of factors of the given number.


[Examples]

___
sum_ff(69) ➞ 3, 23 ➞ 0
# Both 3 and 23 are prime numbers and have no factors
# other than 1 and themselves so the result is 0.

sum_ff(12) ➞ 2, 3, 4, 6 ➞ (0) + (0) + (2) + (2+3) ➞ 7

sum_ff(420) ➞ 2,4, 6, 10, 12 ... ➞ (2) + (2+3) + (2+5) + (2+3+4+6) ... ➞ 1175

sum_ff(619) ➞ ___ ➞ 0
# 619 doesn't have any factors (other than 1 and 619).
_____



[Notes]

___
*) The number will always be greater than 0.
*) Factors that are equal to the number or 1, don't count (see example #1).
___



[loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Prime Number
https://en.wikipedia.org/wiki/Prime_number
Is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. …
_________
_________
Determine the Type of an Object
https://note.nkmk.me/en/python-type-isinstance/
Use type() or isinstance() to determine whether an object is of a specific type.
_________

"""
#Your code should go here:

