/*
####  Closing in Sum  ####

Create a function that returns the sum of the digits formed from the first and last digits, all the way to the center of the number.


[Worked Example]

___
closingInSum("2520") ➞ 72

// The first and last digits are 2 and 0.
// 2 and 0 form 20.
// The second digit is 5 and the second to last digit is 2.
// 5 and 2 form 52.

// 20 + 52 = 72
_____



[Examples]

___
closingInSum("121") ➞ 13
// 11 + 2

closingInSum("1039") ➞ 22
// 19 + 3

closingInSum("22225555") ➞ 100
// 25 + 25 + 25 + 25
_____



[Notes]

___
*) If the number has an odd number of digits, simply add on the single-digit number in the center (see example #1).
*) Any number which is zero-padded counts as a single digit (see example #2).
___



[algorithms] [loops] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
std::stoi
http://www.cplusplus.com/reference/string/stoi/
Parses str interpreting its content as an integral number of the specified base, which is returned as an int value. If idx is not a null pointer, the function also set …
_________
_________
string::substr
https://www.cplusplus.com/reference/string/string/substr/
Returns a newly constructed string object with its value initialized to a copy of a substring of this object.
_________

*/
//Your code should go here:

