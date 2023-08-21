/*
####  Additive Number  ####

Write a function that checks if a given string contains an additive sequence or not. A string contains an additive sequence if its digits can make a sequence of numbers in which every number is the sum of the previous two numbers. A valid additive sequence should contain at least three numbers.


[Examples]

___
isAdditive("112358") ➞ true
// The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
// 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

isAdditive("129881000") ➞ true
// Each number can contain 1 or more digits: 12, 988, 1000.
// 12 + 988 = 1000

isAdditive("12988110101891") ➞ true
// 129 + 881 = 1010, 881 + 1010 = 1891

isAdditive("123456789") ➞ false

isAdditive("300045007500") ➞ true
_____



[Notes]

___
*) The string will contain only digits 0 ➞ 9
*) Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
___



[algebra] [algorithms] [math] [numbers] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Vector
https://www.geeksforgeeks.org/vector-in-cpp-stl/
Vectors are same as dynamic arrays with the ability to resize itself automatically when an element is inserted or deleted, with their storage being handled automaticall …
_________

*/
//Your code should go here:

