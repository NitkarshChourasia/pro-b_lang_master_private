/*
####  Not a Simple Increment  ####

Create a function that takes three integer parameters: a number n, number of iterations, and step. You have to implement an algorithm, which increases the given number as explained below:
___
n = 143726, iterations = 16, step = 3
simpleIncrement(n, iterations, step) ➞ 243826
_____

Step 1: We start from the first digit and increment the 4th digit because the step is 3.
___
s - Starting Position
* - current increased position

Position: s - - - - - ➞ - - - * - -
Number:   1 4 3 7 2 6 ➞ 1 4 3 8 2 6
_____

Step 2: Repeat step #1 with the updated starting position.
___
s - Starting Position
* - current increased position

Position: - - - s - - ➞ * - - - - -
Number:   1 4 3 8 2 6 ➞ 2 4 3 8 2 6
_____

___
*) Remember, if the number overflows, the current position gets shifted to the right.
___

___
9 9 9 ➞ - - p   // before overflow position will be at 3rd digit
1 0 0 0 ➞ - - - p   // after overflow position will be at 4th digit
_____

___
*) More examples on overflow:
___

___
9 ➞ 10
799 ➞ 800 (If you increased the second 9) or 809 (if you increased the first 9)
99000 ➞ 100000 (If you increased the second 9) or 109000 (if you increased the first 9)
_____



[Examples]

___
simpleIncrement(1673, 2, 16) ➞ 3673

simpleIncrement(99, 99, 99) ➞ 198

simpleIncrement(99, 99, 98) ➞ 4734
_____



[Notes]

N/A


[algorithms] [logic] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
pow
http://www.cplusplus.com/reference/cmath/pow/
Returns base raised to the power exponent: base^exponent.
_________
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Returns a string with the representation of val.
_________
_________
std::stoi
http://www.cplusplus.com/reference/string/stoi/
Parses str interpreting its content as an integral number of the specified base, which is returned as an int value. If idx is not a null pointer, the function also set …
_________
_________
For Loop
https://www.w3schools.com/cpp/cpp_for_loop.asp
When you know exactly how many times you want to loop through a block of code, use the for loop instead of a while loop.
_________

*/
//Your code should go here:

