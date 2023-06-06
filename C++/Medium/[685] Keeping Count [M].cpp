/*
####  Keeping Count  ####

Given a number, create a function which returns a new number based on the following rules:
___
*) For each digit, replace it by the number of times it appears in the number.
*) The final instance of the number will be an integer, not a string.
___

The following is a working example:
___
digitCount(136116) ➞ 312332
// The number 1 appears thrice, so replace all 1s with 3s.
// The number 3 appears only once, so replace all 3s with 1s.
// The number 6 appears twice, so replace all 6s with 2s.
_____



[Examples]

___
digitCount(221333) ➞ 221333

digitCount(136116) ➞ 312332

digitCount(2) ➞ 1
_____



[Notes]

Each test will have a positive whole number in its parameter.


[arrays] [language_fundamentals] [loops] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
std::to_string
http://www.cplusplus.com/reference/string/to_string/
Convert numerical value to string.
_________

*/
//Your code should go here:

