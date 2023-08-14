"""
####  No Good Numbers  ####

A positive number's population is the sum of 1's in its binary representation.
___
*) An evil number has an even numbered population.
*) An odious number has an odd numbered population.
*) A number is pernicious if its population is a prime number.
___

Create a function that takes a number as an argument and returns a sorted list of all its descriptors ("Evil", "Odious", or "Pernicious").


[Examples]

___
how_bad(7) ➞ ["Odious", "Pernicious"]
# 7 in binary is "111".
# 1 + 1 + 1 = 3 in "111" means "Odious" should be added to the list answer.
# 3 is a prime number, meaning "Pernicious" should also be added.

how_bad(17) ➞ ["Evil", "Pernicious"]
# 17 in binary is "10001".
# 1 + 1 = 2 in "10001" means "Evil" should be added to the list answer.
# 2 is a prime number, meaning "Pernicious" should also be added.

how_bad(23) ➞ ["Evil"]
# 23 in binary is "10111".
# Four 1's in "10111" means "Evil" should be added to the list answer.
# 4 is not a prime number, meaning "Pernicious" should not be added.
_____



[Notes]

N/A


[conditions] [language_fundamentals] 



-------------------------------------------------------------------
[Resources]
_________
format() Method
https://www.programiz.com/python-programming/methods/string/format
Formats the given string into a nicer output in Python.
_________

"""
#Your code should go here:

