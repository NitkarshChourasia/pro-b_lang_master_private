"""
####  Fibonacci Recursion  ####

The Fibonacci sequence is a classic use case for recursive functions since the value of the sequence at a given index is dependent on the last two values. More precisely, it's dependent on the sum of the previous two values.
Write a function named fib that takes an integer n as its input. It should return the Fibonacci sequence's value at index n.


[Examples]

___
fib(6) ➞ 8
# 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

fib(1) ➞ 1

fib(2) ➞ 1
_____



[Notes]

___
*) You should throw a ValueError if n is less than 0.
*) Assume the Fibonacci sequence's first two values (at indices 0 and 1) are 0 and 1.
*) You must make fib a recursive function.
___



[Tips]

___
*) You can call a function within itself to get the value a different iteration returns. This is called a "recursive function".
*) If you're getting stuck, try looking up the math behind the Fibonacci sequence to see if that inspires you.
*) Check the Resources tab for relevant information!
___



[math] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Python Exceptions: An Introduction
https://realpython.com/python-exceptions/
In this beginner tutorial you'll learn what exceptions are good for in Python. You'll see how to raise exceptions and how to handle them with "try/except" blocks.
_________
_________
Thinking Recursively
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Fibonacci Number
https://en.wikipedia.org/wiki/Fibonacci_number#Sequence_properties
Form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is...
_________

"""
#Your code should go here:

