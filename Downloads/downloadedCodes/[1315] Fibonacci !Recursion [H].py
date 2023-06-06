"""
####  Fibonacci !Recursion  ####

The Fibonacci sequence is a classic use case for recursive functions since the value of the sequence at a given index is dependent on the sum of the last two values. However, the recursion tree created by solving the Fibonacci sequence recursively can grow quite fast. Therefore it can be important to think about the implications of running a function recursively. Depending on the size of n needed and the capabilities of the system in question you might want to take a different approach.
Write a non-recursive function that takes an integer n and returns the Fibonacci sequence's value at index n.


[Examples]

___
fib(6) ➞ 8
# 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

fib(1) ➞ 1

fib(2) ➞ 1
_____



[Notes]

Inputs will be whole numbers >= 0


[algebra] [math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
Efficient Calculation of Fibonacci Series
https://stackoverrun.com/es/q/4953400
Efficient calculation of Fibonacci series.
_________
_________
A Closed Form of the Fibonacci Sequence
http://mathonline.wikidot.com/a-closed-form-of-the-fibonacci-sequence
The formula above is recursive relation and in order to compute $f_n$ we must be able to computer $f_{n-1}$ and $f_{n-2}$. For large $n$, the computation of both of the …
_________
_________
Fast Doubling Method to Find the Nth Fibonacci Number
https://www.geeksforgeeks.org/fast-doubling-method-to-find-the-nth-fibonacci-number/
We can implement iterative version of above method, by initializing array with two elements f = [F(0), F(1)] = [0, 1] and iteratively constructing F(n), on every step w …
_________
_________
Linear Difference Equation
https://en.wikipedia.org/wiki/Linear_difference_equation#Solution_of_homogeneous_case
In mathematics and in particular dynamical systems, a linear difference equation :ch. 17:ch. 10 or linear recurrence relation sets equal to 0 a polynomial that is linea …
_________
_________
Fibonacci Number
https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression
Commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
_________

"""
#Your code should go here:

