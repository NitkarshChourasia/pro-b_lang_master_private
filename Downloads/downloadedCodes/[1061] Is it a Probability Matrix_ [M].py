"""
####  Is it a Probability Matrix?  ####

In probability theory, a probability matrix is a matrix such that:
___
*) The matrix is a square matrix (same number of rows as columns).
*) All entries are probabilities, i.e. numbers between 0 and 1.
*) All rows add up to 1.
___

The following is an example of a probability matrix:
___
[
  [0.5, 0.5, 0.0],
  [0.2, 0.5, 0.3],
  [0.1, 0.2, 0.7]
]
_____

Note that though all rows add up to 1, there is no restriction on the columns, which may or may not add up to 1.
Write a function that determines if a matrix is a probability matrix or not.


[Examples]

___
is_prob_matrix([
  [0.5, 0.5, 0.0],
  [0.2, 0.5, 0.3],
  [0.1, 0.2, 0.7]
]) ➞ True

is_prob_matrix([
  [0.5, 0.5, 0.0],
  [0.2, 0.5, 0.3]
]) ➞ False

# Not a square matrix.

is_prob_matrix([
  [2, -1],
  [-1, 2]
]) ➞ False

# Entries not between 0 and 1.

is_prob_matrix([
  [0, 1],
  [1, 0]
]) ➞ True

is_prob_matrix([
  [0.5, 0.4],
  [0.5, 0.6]
]) ➞ False

# Rows do not add to 1.
_____



[Notes]

Fun fact: for most probability matrices M (for example, if M has no zero entries), the matrix powers M^n converge (as n increases) to a matrix where all rows are identical.


[arrays] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
len() Function
https://www.programiz.com/python-programming/methods/built-in/len
Returns the number of items (length) in an object.
_________
_________
all() Method
https://www.programiz.com/python-programming/methods/built-in/all
Returns True when all elements in the given iterable are true. If not, it returns False.
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________
_________
How to check if a matrix is square?
https://stackoverflow.com/questions/22870734/check-if-a-matrix-is-square-python
I want to test a 2x2 matrix of [[5, 6], [7, 8]] to see if it's a square. I run my code and I'm supposed to get True but I got False instead...
_________

"""
#Your code should go here:

