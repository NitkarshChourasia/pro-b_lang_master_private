"""
####  Arithmetic and Geometric Sequence Function Generator  ####

Write a function that takes an integer sequence represented by a list of integers as a parameter and return a function of that sequence. This function should take an index (starting at 1, not zero), and return the sequence term at that index.
The test sequences given will have at least five terms and will start at the beginning of the sequence. They will be either arithmetic or geometric sequences of the following forms:

___
f(n) = a*n + c
_____


___
f(n) = a^n * c
_____



[Examples:]

___
sequence_generator([1, 2, 3, 4, 5])(3) ➞ 3

sequence_generator([2, 4, 6, 8, 10, 12])(7) ➞ 14

sequence_generator([2, 4, 8, 16, 32, 64])(4) ➞ 16
_____



[Notes]

N/A


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Geometric Sequences
https://www.mathsisfun.com/algebra/sequences-sums-geometric.html
Is a set of things (usually numbers) that are in order. In a Geometric Sequence each term is found by multiplying the previous term by a constant.
_________
_________
Arithmetic Sequences
https://www.mathsisfun.com/algebra/sequences-sums-arithmetic.html
Is a set of things (usually numbers) that are in order. Each number in the sequence is called a term (or sometimes "element" or "member"), read Sequences and Series for …
_________
_________
Returning Functions From Functions
https://realpython.com/lessons/returning-functions-functions/
The code example in the lesson uses a function called parent() that contains two inner functions that return a string of text.
_________

"""
#Your code should go here:

