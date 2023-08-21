/*
####  Look and Say Numbers  ####

Given an integer, return a new string according to the rules below:
___
*) Split the number into groups of two digit numbers. If the number has an odd number of digits, return "invalid".
*) For each group of two digit numbers, concatenate the last digit to a new string the same number of times as the value of the first digit.
*) Return the result as a string.
___

___
lookAndSay(3132) ➞ "111222"

// By reading the number digit by digit, you get three "1" and three "2".
// Therefore, you put three ones and three two's together.
// Remember to return a string.
_____



[Examples]

___
lookAndSay(95) ➞ "555555555"

lookAndSay(120520) ➞ "200"

lookAndSay(231) ➞ "invalid"
_____



[Notes]

___
*) Note that the number 0 can be included (see example #3).
*) Check the Resources tab for a TED-Ed video for extra clarity.
___



[algorithms] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Can you find the next number in this sequence?
https://www.youtube.com/watch?v=LpjX3kHXcR0
Can you find the next number in this sequence?
_________
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Returns a string with the representation of val.
_________
_________
std::stoi
http://www.cplusplus.com/reference/string/stoi/
Convert string to integer Parses str interpreting its content as an integral number of the specified base, which is returned as an int value. If idx is not a null poin …
_________

*/
//Your code should go here:

