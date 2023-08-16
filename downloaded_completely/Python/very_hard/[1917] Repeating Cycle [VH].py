"""
####  Repeating Cycle  ####

Given an integer n, create a function that returns the length of the repeating cycle of the sequence 1/n. If the cycle is non-repetitive, return -1.
___
repeating_cycle(13) ➞ 6
# 1/13 = 0.076923 076923 076923 076923 ...
# length of `076923` is 6.
_____



[Examples]

___
repeating_cycle(5) ➞ -1
# 1/5 = 0.2 (non-repeative)

repeating_cycle(33) ➞ 2
# 1/33 = 0.03 03 03 03 03 03 03 03
# length of `03` is 2

repeating_cycle(197) ➞ 98
_____



[Notes]

Return -1 if the repeating cycle does not start from the first decimal place. As an example, 1/22 = 0.0 45 45 45 45, your function should return -1 in this case.


[algorithms] [control_flow] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Coprime Integers
https://en.wikipedia.org/wiki/Coprime_integers
In number theory, two integers a and b are coprime, relatively prime or mutually prime[1] if the only positive integer that evenly divides (is a divisor of) both of the …
_________
_________
pow() Method
https://www.w3schools.com/python/ref_func_pow.asp
Return the value of 4 to the power of 3 (same as 4 * 4 * 4).
_________
_________
While Loops
https://www.w3schools.com/python/python_while_loops.asp
With the while loop we can execute a set of statements as long as a condition is true.
_________
_________
Conditions and If Statements
https://www.w3schools.com/python/python_conditions.asp
Python supports the usual logical conditions from mathematics. These conditions can be used in several ways, most commonly in "if statements" and loops. An "if stateme …
_________
_________
Find Recurring Sequence in a Fraction
https://www.geeksforgeeks.org/find-recurring-sequence-fraction/
Given a fraction, find a recurring sequence of digits if exists, otherwise, print “No recurring sequence”.
_________
_________
Cyclic Numbers Properties
https://www.ese.iitb.ac.in/~santanu/RM3.pdf
A cyclic number has an unusually interesting property. If you multiply a cyclic number, by 1 through n (where n is the number of digits of the cyclic number), these pro …
_________

"""
#Your code should go here:

