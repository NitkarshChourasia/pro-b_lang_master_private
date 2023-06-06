"""
####  Pascal's Triangle  ####

Mubashir was reading about Pascal's triangle on Wikipedia.
In mathematics, Pascal's triangle is a triangular array of the binomial coefficients that arises in probability theory, combinatorics, and algebra.

Formula for Pascal's triangle is given by:

where n denotes a row of the triangle, and k is the position of a term in the row.
Create a function which takes a number n and returns n top rows of Pascal's Triangle flattened into a one-dimensional list.


[Examples]

___
pascals_triangle(1) ➞ [1]

pascals_triangle(2) ➞ [1, 1, 1]

pascals_triangle(4) ➞ [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]
_____



[Notes]

N/A


[algebra] [algorithms] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Pascal's Triangle
https://www.mathsisfun.com/pascals-triangle.html
To build the triangle, start with 1 at the top, then continue placing numbers below it in a triangular pattern. Each number is the numbers directly above it added together.
_________
_________
math.factorial() Function
https://www.geeksforgeeks.org/python-math-factorial-function/
Returns the factorial of desired number.
_________
_________
Perform Append at Beginning of List
https://www.geeksforgeeks.org/python-perform-append-at-beginning-of-list/
The usual append operation of Python list adds the new element at the end of the list. But in certain situations, we need to append each element we add in front of list …
_________

"""
#Your code should go here:

