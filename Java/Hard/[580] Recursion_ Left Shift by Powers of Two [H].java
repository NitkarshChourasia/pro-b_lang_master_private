/*
####  Recursion: Left Shift by Powers of Two  ####

The left shift operation is similar to multiplication by powers of two, thus, the process is repetitive and can be done recursively.
Sample calculation using the left shift operator (<<):
___
10 << 3 = 10 * 2^3 = 10 * 8 = 80
-32 << 2 = -32 * 2^2 = -32 * 4 = -128
5 << 2 = 5 * 2^2 = 5 * 4 = 20
_____

Write a recursive function that mimics (without the use of <<) the left shift operator and returns the result from the two given integers.


[Examples]

___
shiftToLeft(5, 2) ➞ 20

shiftToLeft(10, 3) ➞ 80

shiftToLeft(-32, 2) ➞ -128

shiftToLeft(-6, 5) ➞ -192

shiftToLeft(12, 4) ➞ 192

shiftToLeft(46, 6) ➞ 2944
_____



[Notes]

___
*) There will be no negative values for the second parameter y.
*) This challenge is more like recreating of the left shift operation, thus, the use of the operator directly is prohibited.
*) You are expected to solve this challenge via recursion.
*) An iterative version of this challenge can be found via this link.
*) A collection of challenges in recursion can be found via this link.
___



[bit_operations] [numbers] [recursion] 



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

*/
//Your code should go here:

