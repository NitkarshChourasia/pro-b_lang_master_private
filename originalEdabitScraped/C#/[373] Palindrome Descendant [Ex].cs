/*
####  Palindrome Descendant  ####

A number may not be a palindrome, but its descendant can be. A number's direct child is created by summing each pair of adjacent digits to create the digits of the next number.
For instance, 123312 is not a palindrome, but its next child 363 is, where: 3 = 1 + 2; 6 = 3 + 3; 3 = 1 + 2.
Create a function that returns true if the number itself is a palindrome or any of its descendants down to the first 2 digit number (a 1-digit number is trivially a palindrome).


[Examples]

___
PalindromeDescendant(11211230) ➞ false
// 11211230 ➞ 2333 ➞ 56

palindromeDescendant(13001120) ➞ true
// 13001120 ➞ 4022 ➞ 44

PalindromeDescendant(23336014) ➞ true
// 23336014 ➞ 5665

PalindromeDescendant(11) ➞ true
// Number itself is a palindrome.
_____



[Notes]

Numbers will always have an even number of digits.


[arrays] [higher_order_functions] [recursion] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Recursive Functions in C#
https://www.c-sharpcorner.com/UploadFile/955025/C-Sharp-interview-questions-part4what-is-a-recursive-function-in/
Question: What is a recursive function in C#? Give an example.Answer: A recursive function is a function that calls itself.A function that calls another function is nor …
_________

*/
//Your code should go here:

