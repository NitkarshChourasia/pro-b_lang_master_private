/*
####  Recursive Digit  ####

We define super digit of an integer x using the following rules:
___
*) If x has only 1 digit, then its super digit is x.
*) Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
___

For example, the super digit of x will be calculated as:
___
  superDigit(9875)    9+8+7+5 = 29 
  superDigit(29)      2 + 9 = 11
  superDigit(11)      1 + 1 = 2
  superDigit(2) = 2
_____

You are given two numbers n and k. The number p is created by concatenating the string n, k times. Continuing the above example where n = 9875, assume your value k=4. Your initial p = 9875 9875 9875 9875 (spaces added for clarity).
___
superDigit(p) = superDigit(9875987598759875)
 // 5+7+8+9+5+7+8+9+5+7+8+9+5+7+8+9 = 116

superDigit(p) = superDigit(116)
  // 1+1+6 = 8

superDigit(p) = superDigit(8)
_____

All of the digits of p sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it's the super digit.
Complete the superDigit() method. It must return the calculated super digit as an integer.
superDigit has the following parameter(s):
___
*) n: a string representation of an integer.
*) k: an integer, the times to concatenate n to make p.
___



[Examples]

___
superDigit("148", 3) ➞ 3

superDigit("123", 3) ➞ 9

superDigit("99999999999999999999999999", 104500) ➞ 9
_____



[Notes]

N/A


[algorithms] [math] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
std::stoi
http://www.cplusplus.com/reference/string/stoi/
Parses str interpreting its content as an integral number of the specified base, which is returned as an int value. If idx is not a null pointer, the function also set …
_________

*/
//Your code should go here:

