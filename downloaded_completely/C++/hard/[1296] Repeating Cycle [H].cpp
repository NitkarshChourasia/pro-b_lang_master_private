/*
####  Repeating Cycle  ####

Given an integer n, create a function that returns the length of the repeating cycle of the sequence 1/n. If the cycle is non-repetitive, return -1.
___
repeatingCycle(13) ➞ 6
// 1/13 = 0.076923 076923 076923 076923 ...
// length of `076923` is 6.
_____



[Examples]

___
repeatingCycle(5) ➞ -1
// 1/5 = 0.2 (non-repeative)

repeatingCycle(33) ➞ 2
// 1/33 = 0.03 03 03 03 03 03 03 03
// length of `03` is 2

repeatingCycle(197) ➞ 98
_____



[Notes]

Return -1 if the repeating cycle does not start from the first decimal place. As an example, 1/22 = 0.0 45 45 45 45, your function should return -1 in this case.


[algorithms] [control_flow] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Conditions and If Statements
https://www.w3schools.com/cpp/cpp_conditions.asp
C++ supports the usual logical conditions from mathematics. You can use these conditions to perform different actions for different decisions. C++ has the following co …
_________
_________
While Loop
https://www.w3schools.com/cpp/cpp_while_loop.asp
Loops can execute a block of code as long as a specified condition is reached.
_________
_________
Coprime Integers
https://en.wikipedia.org/wiki/Coprime_integers
In number theory, two integers a and b are coprime, relatively prime or mutually prime[1] if the only positive integer that evenly divides (is a divisor of) both of the …
_________

*/
//Your code should go here:

