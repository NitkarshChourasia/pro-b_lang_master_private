/*
####  Number of Squares in an N * N Grid  ####

Create a function that calculates the number of different squares in an n * n square grid. Check the Resources tab.


[Examples]

___
numberSquares(2) ➞ 5

numberSquares(4) ➞ 30

numberSquares(5) ➞ 55
_____



[Explanation]

___
*) If n = 0 then the number of squares is 0
*) If n = 1 then the number of squares is 1 + 0 = 1
*) If n = 2 then the number of squares is 2^2 + 1 = 4 + 1 = 5
*) If n = 3 then the number of squares is 3^2 + 5 = 9 + 5 = 14
___

As you can see, for each value of n the number of squares is n squared + the number of squares from the previous value of n.


[Notes]

___
*) Input is a positive integer.
*) Square pyramidal number.
___



[math] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Square Pyramidal Number
https://en.wikipedia.org/wiki/Square_pyramidal_number
Is a figurate number that represents the number of stacked spheres in a pyramid with a square base. Square pyramidal numbers also solve the problem of counting the numb …
_________
_________
Square Pyramidal Number
https://math.wikia.org/wiki/Square_pyramidal_number
Is a figurate number that represents a pyramid with a base and four sides. These numbers can be expressed in a formula as...
_________

*/
//Your code should go here:

