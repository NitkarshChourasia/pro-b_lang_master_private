/*
####  Persistence  ####

The additive persistence of an integer, n, is the number of times you have to replace n with the sum of its digits until n becomes a single digit integer.
The multiplicative persistence of an integer, n, is the number of times you have to replace n with the product of its digits until n becomes a single digit integer.
Create two functions that take an integer as an argument and:



[Examples: Additive Persistence]

___
additivePersistence(1679583) ➞ 3
// 1 + 6 + 7 + 9 + 5 + 8 + 3 = 39
// 3 + 9 = 12
// 1 + 2 = 3
// It takes 3 iterations to reach a single-digit number.

additivePersistence(123456) ➞ 2
// 1 + 2 + 3 + 4 + 5 + 6 = 21
// 2 + 1 = 3

additivePersistence(6) ➞ 0
// Because 6 is already a single-digit integer.
_____



[Examples: Multiplicative Persistence]

___
multiplicativePersistence(77) ➞ 4
// 7 x 7 = 49
// 4 x 9 = 36
// 3 x 6 = 18
// 1 x 8 = 8
// It takes 4 iterations to reach a single-digit number.

multiplicativePersistence(123456) ➞ 2
// 1 x 2 x 3 x 4 x 5 x 6 = 720
// 7 x 2 x 0 = 0

multiplicativePersistence(4) ➞ 0
// Because 4 is already a single-digit integer.
_____



[Notes]

The input n is never negative.


[loops] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
While Loop
https://www.geeksforgeeks.org/java-while-loop-with-examples/
Is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement. …
_________
_________
Stream.reduce Method
https://docs.oracle.com/javase/tutorial/collections/streams/reduction.html#reduce
A general-purpose reduction operation. Consider the following pipeline, which calculates the sum of the male members' ages in the collection roster. It uses the Stream. …
_________

*/
//Your code should go here:

