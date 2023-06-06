/*
####  Recursion: Consecutive Number Series  ####

Write a function that will return true if a given string (divided and grouped into a size) will contain a set of consecutive numbers (regardless of orientation: whether ascending or descending), otherwise, return false.


[Examples]

___
isConsecutive("121314151617") ➞ true
// Contains a set of consecutive ascending numbers
// if grouped into 2's : 12, 13, 14, 15, 16, 17

isConsecutive("123124125") ➞ true
// Contains a set of consecutive ascending numbers
// if grouped into 3's : 123, 124, 125

isConsecutive("32332432536") ➞ false
// Regardless of the grouping size, the numbers can't be consecutive.

isConsecutive("326325324323") ➞ true
// Contains a set of consecutive descending numbers
// if grouped into 3's : 326, 325, 324, 323

isConsecutive("667666") ➞ true
// Consecutive descending numbers: 667 and 666.

isConsecutive("999897959493") ➞ false
_____



[IMPORTANT]

The expected solution for this challenge is done recursively. Please check out the Resources tab for more details about recursion in Java.


[Notes]

___
*) A number can consist of any number of digits, so long as the numbers are adjacent to each other, and the string has at least two of them.
*) An iterative version of this challenge can be found via this link.
*) A collection of challenges in recursion can be found via this link.
___



[numbers] [recursion] [sorting] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
Recursion
https://www.baeldung.com/java-recursion
Learn the fundamental concepts of recursion in Java with examples.
_________
_________
Recursion
https://introcs.cs.princeton.edu/java/23recursion/
The idea of calling one function from another immediately suggests the possibility of a function calling itself. The function-call mechanism in Java supports this possi …
_________
_________
Recursion
https://www.geeksforgeeks.org/recursion-in-java/
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function. Using recursive …
_________
_________
String substring() Method
https://beginnersbook.com/2013/12/java-string-substring-method-example/
Returns the substring of a given string. Substring is returned based on the indexes that we pass while calling this method.
_________

*/
//Your code should go here:

