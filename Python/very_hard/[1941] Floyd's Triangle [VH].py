"""
####  Floyd's Triangle  ####

Floyd's triangle is a right-angled triangular array of natural numbers. It's defined by filling the rows of the triangle with consecutive numbers, starting with a 1 in the top left corner:

Write a function that takes an integer n and returns Floyd's triangle's rows as a list of lists. Your function should return one of two possibilities:
___
*) If a value is passed to n_row, return the first n rows.
*) If a value is passed to up_to, return all rows up to, and including, the row that contains n.
___

Expect an argument to be passed to one parameter or the other, but not both.


[Examples]

___
floyd(up_to = 5) ➞ [[1], [2, 3], [4, 5, 6]]
# The third row contains a 5.

floyd(n_row = 5) ➞[[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
# Returns the first five rows.

floyd(up_to = 10) ➞ [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

floyd(n_row = 1) ➞[[1]]
_____



[Notes]

Hint: You can define n_row from up_to using the triangular number sequence. That is, n_row should be x in the equation (x*(x+1))/2 = up_to rounded up. Then, you only need to write a function for n_row.


[algorithms] [conditions] [math] 



-------------------------------------------------------------------
[Resources]
_________
Floyd's Triangle
https://en.wikipedia.org/wiki/Floyd%27s_triangle
A right-angled triangular array of natural numbers, used in computer science education. It is named after Robert Floyd. It is defined by filling the rows of the triangl …
_________
_________
Triangular Number Sequence
https://www.mathsisfun.com/algebra/triangular-numbers.html
Comes from a pattern of dots that form a triangle.
_________
_________
The On-Line Encyclopedia of Integer Sequences (OEIS)
https://oeis.org/A002024
Encyclopedia of Integer Sequences (OEIS)
_________

"""
#Your code should go here:

