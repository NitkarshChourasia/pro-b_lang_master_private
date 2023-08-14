/*
####  Consecutive Ascending Numbers  ####

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



[Notes]

___
*) A number can consist of any number of digits, so long as the numbers are adjacent to each other, and the string has at least two of them.
*) A recursive version of this challenge can be found via this link.
___



[arrays] [sorting] [strings] [validation] 



-------------------------------------------------------------------
[Resources]
_________
String substring() Method
https://beginnersbook.com/2013/12/java-string-substring-method-example/
Returns the substring of a given string. Substring is returned based on the indexes that we pass while calling this method.
_________
_________
Java Regex - Boundary Matcher [\G] Match
https://www.tutorialspoint.com/javaregex/javaregex_boundary_matcher_previous.htm
The Boundary Matcher [\G] matches the end of previous match.
_________

*/
//Your code should go here:

