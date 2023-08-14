"""
####  Recursive Digit  ####

We define super digit of an integer x using the following rules:
___
*) If x has only 1 digit, then its super digit is x.
*) Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
___

For example, the super digit of x will be calculated as:
___
  super_digit(9875)    9+8+7+5 = 29
  super_digit(29)      2 + 9 = 11
  super_digit(11)      1 + 1 = 2
  super_digit(2) = 2
_____

You are given two numbers n and k. The number p is created by concatenating the string n, k times. Continuing the above example where n = 9875, assume your value k=4. Your initial p = 9875 9875 9875 9875 (spaces added for clarity).
___
super_digit(p) = super_digit(9875987598759875)
  5+7+8+9+5+7+8+9+5+7+8+9+5+7+8+9 = 116

super_digit(p) = super_digit(116)
  1+1+6 = 8

super_digit(p) = super_digit(8)
_____

All of the digits of p sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it's the super digit.
Complete the super_digit() method. It must return the calculated super digit as an integer.
superDigit has the following parameter(s):
___
*) n: a string representation of an integer.
*) k: an integer, the times to concatenate n to make p.
___



[Examples]

___
super_digit("148", 3) ➞ 3

super_digit("123", 3) ➞ 9

super_digit("99999999999999999999999999", 104500) ➞ 9
_____



[Notes]

N/A


[algorithms] [math] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Map, Filter, Reduce
https://www.learnpython.org/en/Map,_Filter,_Reduce
Are paradigms of functional programming. They allow the programmer (you) to write simpler, shorter code, without neccessarily needing to bother about intricacies like l …
_________
_________
int() Method
https://www.programiz.com/python-programming/methods/built-in/int
Returns an integer object from any number or string.
_________
_________
sum() Function
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum. In this tutorial, we will learn about the sum() function with the help of examples.
_________

"""
#Your code should go here:

