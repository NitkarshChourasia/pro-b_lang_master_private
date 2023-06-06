"""
####  The Perrin Sequence  ####

Each number in the Perrin sequence is created by summing the numbers two positions and three positions before it. The first three numbers are (3, 0, 2), and the sequence is extended as follows:
___
P(0) P(1) P(2) P(3) P(4) P(5) P(6) P(7) ... P(n)
3, 0, 2, 3, 2, 5, 5, 7, ...
_____

Given a value for n, return the Perrin number P(n).


[Examples]

___
perrin(1) ➞ 0

perrin(8) ➞ 10

perrin(26) ➞ 1497
_____



[Notes]

Check the Resources tab for a further explanation of the Perrin sequence.


[algorithms] [arrays] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Program for Perrin numbers
https://www.geeksforgeeks.org/program-perrin-numbers/
Are the numbers in the following integer sequence. 3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39 … In mathematical terms, the sequence p(n) of Perrin numbers is defin …
_________
_________
matrix raised to power
https://stackoverflow.com/questions/5018552/how-to-raise-a-numpy-array-to-a-power-corresponding-to-repeated-matrix-multipl
numpy matrix raised to power.
_________
_________
How to Use Python Lists
http://openbookproject.net/thinkcs/python/english3e/lists.html
A list is an ordered collection of values. The values that make up a list are called its elements, or its items. We will use the term element or item to mean the same t …
_________
_________
Data Structures
https://docs.python.org/3/tutorial/datastructures.html
This chapter describes some things you’ve learned about already in more detail, and adds some new things as well.
_________
_________
Perrin Numbers
https://everything2.com/title/Perrin+numbers
The Perrin numbers are a sequence of numbers similar to the Fibonacci numbers in that successive numbers are derived from two previous adjacent numbers, only in this ca …
_________
_________
Perrin Number
https://en.wikipedia.org/wiki/Perrin_number
In mathematics, the Perrin numbers are defined by the recurrence relation P(n) = P(n − 2) + P(n − 3) for n > 2, with initial values P(0) = 3, P(1) = 0, P(2) = 2. The se …
_________

"""
#Your code should go here:

