"""
####  Pascal's Triangle  ####

The goal of this challenge is to return Pascal's triangle up to number 29. Pascal's triangle is the sum of the two upper corners.
___
   1 1
  1 2 1
 1 3 3 1

# There will always be the 1 in the first
# place and the row in the second.
_____


Create a function that returns a row from Pascal's triangle. To find the row and column you can use n!/(k!*(n-k)!) where n is the row down and k is the column.


[Examples]

___
pascals_triangle(1) ➞ "1 1"

pascals_triangle(4) ➞ "1 4 6 4 1"

pascals_triangle(6) ➞ "1 6 15 20 15 6 1"

pascals_triangle(8) ➞ "1 8 28 56 70 56 28 8 1"
_____



[Notes]

N/A


[algebra] [algorithms] [loops] [math] 



-------------------------------------------------------------------
[Resources]
_________
Pascal Triangle in Python
https://www.101computing.net/pascal-triangle/
To build a Pascal Triangle we start with a “1” at the top. We then place numbers below each number in a triangular pattern: Each number is the result of adding the two …
_________
_________
Combination
https://en.wikipedia.org/wiki/Combination
Is a selection of items from a collection, such that (unlike permutations) the order of selection does not matter. A k-combination of a set S is a subset of k distinct …
_________
_________
Factorial
https://en.wikipedia.org/wiki/Factorial
The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n.
_________
_________
Pascal's Triangle
https://en.wikipedia.org/wiki/Pascal%27s_triangle
A triangular array of the binomial coefficients. In much of the Western world, it is named after the French mathematician Blaise Pascal, although other mathematicians s …
_________
_________
Guide to Pascal’s Triangle
https://www.geeksforgeeks.org/pascal-triangle/
Pascal’s triangle is a triangular array of the binomial coefficients. Write a function that takes an integer value n as input and prints first n lines of the Pascal’s t …
_________

"""
#Your code should go here:

