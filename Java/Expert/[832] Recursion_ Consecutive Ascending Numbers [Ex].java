/*
####  Recursion: Consecutive Ascending Numbers  ####

Write a function that will return true if a given string (divided and grouped into a size) will contain a set of consecutive ascending numbers, otherwise, return false.


[Examples]

___
ascending("123124125") ➞ true
// Contains a set of consecutive ascending numbers
// if grouped into 3's : 123, 124, 125

ascending("101112131415") ➞ true
// Contains a set of consecutive ascending numbers
// if grouped into 2's : 10, 11, 12, 13, 14, 15

ascending("32332432536") ➞ false
// Regardless of the grouping size, the numbers can't be consecutive.

ascending("326325324323") ➞ false
// Though the numbers (if grouped into 3's) are consecutive but descending.

ascending("666667") ➞ true
// Consecutive numbers: 666 and 667.
_____



[IMPORTANT]

The expected solution for this challenge is done recursively. Please check out the Resources tab for more details about recursion in Java.


[Notes]

___
*) A number can consist of any number of digits, so long as the numbers are adjacent to each other, and the string has at least two of them.
*) An iterative version of this challenge can be found via this link.
*) A collection of challenges in recursion can be found via this link.
___



[arrays] [numbers] [recursion] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Recursion
https://introcs.cs.princeton.edu/java/23recursion/
The idea of calling one function from another immediately suggests the possibility of a function calling itself. The function-call mechanism in Java supports this possi …
_________
_________
Recursion
https://www.baeldung.com/java-recursion
Learn the fundamental concepts of recursion in Java with examples.
_________
_________
Recursion
https://www.geeksforgeeks.org/recursion-in-java/
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function. Using recursive …
_________

*/
//Your code should go here:

