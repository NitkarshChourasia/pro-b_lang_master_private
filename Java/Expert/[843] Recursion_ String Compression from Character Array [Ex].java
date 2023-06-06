/*
####  Recursion: String Compression from Character Array  ####

The function is given an array of characters. Recursively compress the array into a string using the following rules. For each group of consecutively repeating characters:
___
*) If the number of repeating characters is one, append the string with only this character.
*) If the number n of repeating characters x is greater than one, append the string with "x" + n.
___



[Examples]

___
compress(["t", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "s", "s", "s", "h"]) ➞ "te14s3h"

compress(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"

compress(["a"]) ➞ "a"

compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) ➞ "ab12"

compress(["a", "a", "a", "b", "b", "a", "a"]) ➞ "a3b2a2"
_____



[Notes]

___
*) You are expected to solve this challenge using the concept of recursion.
*) Check out the Resources tab for details about recursion in Java.
*) An iterative version of this challenge can be found via this link.
*) A collection of challenges of this nature can be found via this link.
___



[arrays] [recursion] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Recursion in Java
https://www.baeldung.com/java-recursion
Learn the fundamental concepts of recursion in Java with examples.
_________
_________
Recursion
https://introcs.cs.princeton.edu/java/23recursion/
The idea of calling one function from another immediately suggests the possibility of a function calling itself. The function-call mechanism in Java supports this possi …
_________
_________
Recursion in Java
https://www.geeksforgeeks.org/recursion-in-java/
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function. Using recursive …
_________

*/
//Your code should go here:

