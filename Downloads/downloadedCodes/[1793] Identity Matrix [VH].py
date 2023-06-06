"""
####  Identity Matrix  ####

An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right. The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.
Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the mirror image is left-right or top-bottom.


[Examples]

___
id_mtrx(2) ➞ [
  [1, 0],
  [0, 1]
]

id_mtrx(-2) ➞ [
  [0, 1],
  [1, 0]
]

id_mtrx(0) ➞ []
_____



[Notes]

Incompatible types passed as n should return the string "Error".


[arrays] 



-------------------------------------------------------------------
[Resources]
_________
Generating a Numpy Identity Matrix
https://numpy.org/doc/stable/reference/generated/numpy.identity.html
Numpy arrays are useful and easily generated. Here, an identity matrix making a square of n-length sides can be generated as easily as numpy.identity(n). For numbers ot …
_________
_________
Rotating Arrays Using numpy.rot90
https://docs.scipy.org/doc/numpy-1.9.2/reference/generated/numpy.rot90.html
Rotating arrays is hard... unless you're using the numpy module, where rot90 really shines. You can also specify how many times you want the array to rotate 90 degrees, …
_________
_________
Intro to Identity Matrices
https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:properties-of-matrix-multiplication/a/intro-to-identity-matrices
A matrix is a rectangular arrangement of numbers into rows and columns. The dimensions of a matrix tell the number of rows and columns of the matrix in that order. Sinc …
_________
_________
Identity Matrix and Its Properties
https://www.mathbootcamps.com/the-identity-matrix-and-its-properties/
The identity matrix is a square matrix that has 1’s along the main diagonal and 0’s for all other entries. This matrix is often written simply as I, and is special in t …
_________
_________
Identity Matrix
https://en.wikipedia.org/wiki/Identity_matrix
In linear algebra, the identity matrix, or sometimes ambiguously called a unit matrix, of size n is the n × n square matrix with ones on the main diagonal and zeros els …
_________

"""
#Your code should go here:

