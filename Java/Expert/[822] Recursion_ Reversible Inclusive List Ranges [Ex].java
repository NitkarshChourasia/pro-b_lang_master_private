/*
####  Recursion: Reversible Inclusive List Ranges  ####

Write a function that, given the startOfRange and endOfRange values, returns an array containing all the numbers inclusive to that range. See examples below.


[Examples]

___
reversibleInclusiveList(1, 5) ➞ [1, 2, 3, 4, 5]

reversibleInclusiveList(2, 8) ➞ [2, 3, 4, 5, 6, 7, 8]

reversibleInclusiveList(10, 20) ➞ [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

reversibleInclusiveList(24, 17) ➞ [24, 23, 22, 21, 20, 19, 18, 17]
_____



[IMPORTANT]

___
*) The use of IntStream.range and IntStream.rangeClosed is totally unacceptable, hence, recursion is the very purpose of this challenge.
___



[Notes]

___
*) The sort order of the resulting array is dependent of the input values.
*) All inputs provided in the test scenarios are valid.
*) If startOfRange is greater than endOfRange, return an descendingly sorted array, otherwise, ascendingly sorted.
*) You are expected to solve this challenge via a recursive approach.
*) A iterative version of this challenge can be found via this link
*) A collection of challenges in recursion can be found via this link.
___



[logic] [math] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Java.lang.System.arraycopy() Method
https://www.tutorialspoint.com/java/lang/system_arraycopy.htm
Copies an array from the specified source array, beginning at the specified position, to the specified position of the ....
_________
_________
Recursion
https://www.baeldung.com/java-recursion
Learn the fundamental concepts of recursion in Java with examples.
_________
_________
Variable Arguments (Varargs) in Java
https://www.geeksforgeeks.org/variable-arguments-varargs-in-java/
In JDK 5, Java has included a feature that simplifies the creation of methods that need to take a variable number of arguments. This feature is called varargs and it is …
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

*/
//Your code should go here:

