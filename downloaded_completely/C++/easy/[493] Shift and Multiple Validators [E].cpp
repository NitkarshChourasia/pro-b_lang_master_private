/*
####  Shift and Multiple Validators  ####

For this task, you will write two validators.

A few examples to illustrate these respective functions:


[Examples]

___
isShifted([1, 2, 3], [2, 3, 4]) ➞ true
// Each element is shifted +1

isShifted([1, 2, 3], [-9, -8, -7]) ➞ true
// Each element is shifted -10

isMultiplied([1, 2, 3], [10, 20, 30]) ➞ true
// Each element is multiplied by 10

isMultiplied([1, 2, 3], [-0.5, -1, -1.5]) ➞ true
// Each element is multiplied by -1/2

isMultiplied([1, 2, 3], [0, 0, 0]) ➞ true
// Each element is multiplied by 0
_____



[Notes]

___
*) The given arrays are the same length.
*) Keep in mind one special case: if the second array is an array of only zeroes, then the first array can be anything (the multiplier will be 0).
___



[higher_order_functions] [validation] 



-------------------------------------------------------------------
[Resources]
_________
What is the most effective way for float and double comparison?
https://www.tutorialspoint.com/what-is-the-most-effective-way-for-float-and-double-comparison-in-c-cplusplus
Here we will see how to compare two floating point data or two double data using C or C++. The floating point / double comparison is not similar to the integer comparis …
_________
_________
Relational Operators and Floating Point Comparisons
https://www.learncpp.com/cpp-tutorial/relational-operators-and-floating-point-comparisons/
You have already seen how most of these work, and they are pretty intuitive. Each of these operators evaluates to the boolean value true (1), or false (0). Here’s some …
_________

*/
//Your code should go here:

