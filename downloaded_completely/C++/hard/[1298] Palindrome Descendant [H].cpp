/*
####  Palindrome Descendant  ####

A number may not be a palindrome, but its descendant can be. A number's direct child is created by summing each pair of adjacent digits to create the digits of the next number.
For instance, 123312 is not a palindrome, but its next child 363 is, where: 3 = 1 + 2; 6 = 3 + 3; 3 = 1 + 2.
Create a function that returns true if the number itself is a palindrome or any of its descendants down to the first 2 digit number (a 1-digit number is trivially a palindrome).


[Examples]

___
palindromeDescendant(11211230) ➞ false
// 11211230 ➞ 2333 ➞ 56

palindromeDescendant(13001120) ➞ true
// 13001120 ➞ 4022 ➞ 44

palindromeDescendant(23336014) ➞ true
// 23336014 ➞ 6565

palindromeDescendant(11) ➞ true
// Number itself is a palindrome.
_____



[Notes]

Numbers will always have an even number of digits.


[arrays] [higher_order_functions] [recursion] [validation] 



-------------------------------------------------------------------
[Resources]


[No Resources]


*/
//Your code should go here:

