/*
####  Solve a Linear Equation  ####

The function is given a string representing a linear equation with one unknown. Find the value of x that is a valid solution of the equation. Return the sting x=val. Three outcomes are possible:
___
*) x_val is an integer or a float (round x_val to 2 decimals)
*) "Infinite solutions" for situations 0*x=0
*) "No solution" for situations 0*x=num, (num != 0)
___



[Examples]

___
FindX("4x-7=x+11") ➞ "x=6"

FindX("3x=2x+x") ➞ "Infinite solutions"

FindX("3x=3x+2") ➞ "No solution"

FindX("-1-2x=15+x") ➞ "x=-5.33"
_____



[Notes]

___
*) It is a good exercise for using Regex to find all numbers and coefficients of x.
*) All numbers have at most 3 digits.
___



[algorithms] [math] [regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Regex
https://regex101.com/
An explanation of your regex will be automatically generated as you type.
_________

*/
//Your code should go here:

