"""
####  Straight Digital Numbers  ####

In this challenge, you have to establish if the digits of a given number form a straight arithmetic sequence (either increasing or decreasing). A straight sequence has an equal step between every pair of digits.
Given an integer n, implement a function that returns:
___
*) "Not Straight" if n is lower than 100 or if its digits are not an arithmetic sequence.
*) "Trivial Straight" if n has a single repeating digit.
*) An integer being the step of the sequence if the n digits are a straight arithmetic sequence.
___



[Examples]

___
straight_digital(123) ➞ 1
# 2 - 1 = 1 | 3 - 2 = 1

straight_digital(753) ➞ -2
# 5 - 7 = -2 | 3 - 5 = -2

straight_digital(666) ➞ "Trivial Straight"
# There's a single repeating digit (step = 0).

straight_digital(124) ➞ "Not Straight"
# 2 - 1 = 1 | 4 - 2 = 2
# A valid sequence has always the same step between its digits.

straight_digital(99) ➞ "Not Straight"
# The number is lower than 100.
_____



[Notes]

___
*) The step of the sequence can be either positive or negative (see example #2).
*) Trivia: there are infinite straight digital numbers, but only 96 of them are made of at least two different digits.
___



[math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
len() Function
https://www.w3schools.com/python/ref_func_len.asp#:~:text=The%20len()%20function%20returns,of%20characters%20in%20the%20string.
Returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.
_________
_________
all() Function
https://www.w3schools.com/python/ref_func_all.asp
Returns True if all items in an iterable are true, otherwise it returns False. If the iterable object is empty, the all() function also returns True.
_________
_________
Sets
https://www.w3schools.com/python/python_sets.asp
Are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, an …
_________

"""
#Your code should go here:

