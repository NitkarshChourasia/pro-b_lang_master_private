/*
####  Can You Make the Numbers?  ####

You are given an array representing the number of 0s, 1s, 2s, ..., 9s you have. The function will look like:
___
can_build([#0s, #1s, #2s, ..., #9s], [num1, num2, ...])
_____

Write a function that returns true if you can build the following numbers using only the digits you have.


[Examples]

___
canBuild([0, 1, 2, 2, 3, 0, 0, 0, 1, 1], [123, 444, 92]) ➞ true

// You have: one 1, two 2s, two 3s, three 4s, one 8 and one 9
// Using only these digits, you can build 123, 444, and 92

canBuild([10, 2, 3, 8, 5, 8, 5, 5, 3, 1], [11, 2, 22, 49, 444, 998, 87, 44]) ➞ false

canBuild([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], []) ➞ true

canBuild([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3]) ➞ false
_____



[Notes]

N/A


[arrays] [higher_order_functions] [loops] 



-------------------------------------------------------------------
[Resources]
_________
How do I split an int into its digits?
https://stackoverflow.com/questions/4261589/how-do-i-split-an-int-into-its-digits
Given the number 12345 : 5 is 12345 % 10 4 is 12345 / 10 % 10 3 is 12345 / 100 % 10 2 is 12345 / 1000 % 10 1 is 12345 / 10000 % 10
_________

*/
//Your code should go here:

