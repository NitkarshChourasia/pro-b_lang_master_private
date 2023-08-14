"""
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
simple_increment(1673, 2, 16) ➞ 3673

simple_increment(99, 99, 99) ➞ 198

simple_increment(99, 99, 98) ➞ 4734
_____



[Notes]

N/A


[algorithms] [logic] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
For Loops
https://www.w3schools.com/python/python_for_loops.asp
Used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
_________
_________
len() Method
https://www.w3schools.com/python/ref_func_len.asp#:~:text=The%20len()%20function%20returns,of%20characters%20in%20the%20string.
Returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.
_________
_________
str() Method
https://www.programiz.com/python-programming/methods/built-in/str
Returns the string version of the given object.
_________

"""
#Your code should go here:

