"""
####  Primes Spiral  ####

Create a function that takes a number and a direction of rotation as an argument and returns a spiral of prime number.
Given a number n and a direction of rotation, clockwise cw or counterclockwise ccw, the program must print a n*n matrix where each element of the matrix will be a prime number. The element in coordinates (0, 0) will be the starting point, and based on the informed direction of rotation, each next element will be the next prime number, in an ascending sequence, always running through the matrix in a spiral form.


[Examples]

___
spiral(1, "cw") ➞ "Impossible to obtain a list of primes."

spiral(2, "cw") ➞
  ["2", "3"]
  ["7", "5"]

spiral(3, "cw") ➞
  ["02", "03", "05"]
  ["19", "23", "07"]
  ["17", "13", "11"]

spiral(3, "cw") ➞
  ["02", "03", "05"]
  ["19", "23", "07"]
  ["17", "13", "11"]

spiral(4, "cw") ➞
  ["02", "03", "05", "07"]
  ["37", "41", "43", "11"]
  ["31", "53", "47", "13"]
  ["29", "23", "19", "17"]

spiral(4, "ccw") ➞
  ["02", "37", "31", "29"]
  ["03", "41", "53", "23"]
  ["05", "43", "47", "19"]
  ["07", "11", "13", "17"]
_____



[Notes]

___
*) Add leading zeros when neccesary in order to secure that all elements of the maxtix have the same lenght.
*) Please note that each line of the matrix is printed on a different line. Check the tests section to review this point.
___



[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
gmpy2
https://pypi.org/project/gmpy2/
gmpy2 is an optimized, C-coded Python extension module that supports fast multiple-precision arithmetic. gmpy2 is based on the original gmpy module. gmpy2 adds support …
_________

"""
#Your code should go here:

