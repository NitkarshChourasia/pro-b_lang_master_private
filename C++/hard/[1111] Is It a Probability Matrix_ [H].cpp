/*
####  Is It a Probability Matrix?  ####

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
isProbMatrix([
  [0.5, 0.5, 0.0],
  [0.2, 0.5, 0.3],
  [0.1, 0.2, 0.7]
]) ➞ true

isProbMatrix([
  [0.5, 0.5, 0.0],
  [0.2, 0.5, 0.3]
]) ➞ false

// Not a square matrix.

isProbMatrix([
  [2, -1],
  [-1, 2]
]) ➞ false

// Entries not between 0 and 1.

isProbMatrix([
  [0, 1],
  [1, 0]
]) ➞ true

isProbMatrix([
  [0.5, 0.4],
  [0.5, 0.6]
]) ➞ false

// Rows do not add to 1.
_____



[Notes]

Fun fact: for most probability matrices M (for example, if M has no zero entries), the matrix powers M^n converge (as n increases) to a matrix where all rows are identical.


[arrays] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
std::vector
http://www.cplusplus.com/reference/vector/vector/
Are sequence containers representing arrays that can change in size. Just like arrays, vectors use contiguous storage locations for their elements, which means that th …
_________
_________
std::accumulate
http://www.cplusplus.com/reference/numeric/accumulate/
Returns the result of accumulating all the values in the range [first,last) to init.
_________

*/
//Your code should go here:

