/*
####  Recursion: Right Shift by Division  ####

The right shift operation is similar to floor division by powers of two, thus, the process is repetitive and can be done recursively.
Sample calculation using the right shift operator ( >> ):
___
80 >> 3 = floor(80/2^3) = floor(80/8) = 10
-24 >> 2 = floor(-24/2^2) = floor(-24/4) = -6
-5 >> 1 = floor(-5/2^1) = floor(-5/2) = -3
_____

Write a function that mimics (without the use of >>) the right shift operator and returns the result from the two given integers.


[Examples]

___
shiftToRight(80, 3) ➞ 10

shiftToRight(-24, 2) ➞ -6

shiftToRight(-5, 1) ➞ -3

shiftToRight(4666, 6) ➞ 72

shiftToRight(3777, 6) ➞ 59

shiftToRight(-512, 10) ➞ -1
_____



[Notes]

___
*) There will be no negative values for the second parameter y.
*) This challenge is more like recreating of the right shift operation, thus, the use of the operator directly is prohibited.
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

