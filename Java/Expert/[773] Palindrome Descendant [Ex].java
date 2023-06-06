/*
####  Palindrome Descendant  ####

A number may not be a palindrome, but its descendant can be. A number's direct child is created by summing each pair of adjacent digits to create the digits of the next number.
For instance, 123312 is not a palindrome, but its next child 363 is, where: 3 = 1 + 2; 6 = 3 + 3; 3 = 1 + 2.
Create a function that returns true if the number itself is a palindrome or any of its descendants down to the first 2 digit number (a 1-digit number is trivially a palindrome).


[Examples]

___
palindromedescendant(11211230) ➞ true
// 11211230 ➞ 2333 ➞ 56 ➞ 11

palindromeDescendant(13001120) ➞ true
// 13001120 ➞ 4022 ➞ 44

palindromeDescendant(23336014) ➞ true
// 23336014 ➞ 5665

palindromeDescendant(11) ➞ true
// Number itself is a palindrome.
_____



[Notes]

Numbers will always have an even number of digits.
Video Description & Solution


[arrays] [higher_order_functions] [recursion] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Palindrome Number
https://www.javatpoint.com/palindrome-program-in-java#:~:text=Palindrome%20number%20in%20java%3A%20A%20palindrome%20number%20is,and%20check%20whether%20number%20is%20palindrome%20or%20not.
Is a number that is same after reverse. For example 545, 151, 34543, 343, 171, 48984 are the palindrome numbers. It can also be a string like LOL, MADAM etc.
_________
_________
Palindrome Descendant Java Coding Challenge
https://youtu.be/xn0yUBLx16c
Palindrome descendant java coding challenge.
_________

*/
//Your code should go here:

