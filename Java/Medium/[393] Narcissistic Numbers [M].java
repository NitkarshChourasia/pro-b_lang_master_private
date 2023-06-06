/*
####  Narcissistic Numbers  ####

A number is narcissistic when the sum of its digits, with each digit raised to the power of digits quantity, is equal to the number itself.
___
153 ➞ 3 digits ➞ 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ➞ Narcissistic
84 ➞ 2 digits ➞ 8² + 4² = 64 + 16 = 80 ➞ Not narcissistic
_____

Given a positive integer n, implement a function that returns true if the number is narcissistic, and false if it's not.


[Examples]

___
isNarcissistic(8208) ➞ true
// 8⁴ + 2⁴ + 0⁴ + 8⁴ = 8208

isNarcissistic(22) ➞ false
// 2² + 2² = 8

isNarcissistic(9) ➞ true
// 9¹ = 9
_____



[Notes]

___
*) Trivially, any number in the 1-9 range is narcissistic and any two-digit number is not.
*) Curious fact: Only 88 numbers are narcissistic.
___



[language_fundamentals] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Narcissistic Number Exercise (Java)
https://coderanch.com/t/708790/java/Narcissistic-number-exercise
Write a class Exercise3 with a method public static boolean isNarcissisticNumber(int number). The aim of the method is to judge a number which is a narcissistic number …
_________
_________
Narcissistic Number Tutorial
https://www.geeksforgeeks.org/narcissistic-number/
The approach will be to count the number of digits and then extract every digit and then by using pow function we can get the power of that digit and then sum it up at …
_________

*/
//Your code should go here:

