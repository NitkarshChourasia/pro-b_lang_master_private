/*
####  Print Grid  ####

Write a method that accepts two integer parameters rows and cols. The output is a comma-separated grid of numbers displayed in column-major order, meaning the numbers shown increase sequentially down each column and wrap to the top of the next column to the right once the bottom of the current column is reached.


[Examples]

___
printGrid(3, 6) ➞ "
  1, 4, 7, 10, 13, 16
  2, 5, 8, 11, 14, 17
  3, 6, 9, 12, 15, 18
"

printGrid(5, 3) ➞ "
  1, 6, 11
  2, 7, 12
  3, 8, 13
  4, 9, 14
  5, 10, 15
"

printGrid(4, 1) ➞ "
  1
  2
  3
  4
"
_____



[Notes]

___
*) Each row ends with "\n" e.g. "1, 6, 11\n" rather then a space "1, 6, 11 " (=wrong)
*) Last line "\n" should be trimed.
___



[language_fundamentals] [loops] 



-------------------------------------------------------------------
[Resources]
_________
StringBuilder Class
https://www.geeksforgeeks.org/stringbuilder-class-in-java-with-examples/
Represents a mutable sequence of characters. Since the String Class in Java creates an immutable sequence of characters, the StringBuilder class provides an alternative …
_________
_________
String trim() Method
https://www.tutorialspoint.com/java/java_string_trim.htm
Returns a copy of the string, with leading and trailing whitespace omitted.
_________

*/
//Your code should go here:

