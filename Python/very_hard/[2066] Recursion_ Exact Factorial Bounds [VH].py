"""
####  Recursion: Exact Factorial Bounds  ####

Create a recursive function that tests if a number is the exact upper bound of the factorial of n. If so, return a list that contains the exact factorial bound and n, or otherwise, the string "Not exact!".


[Examples]

___
is_exact(6) ➞ [6, 3]

is_exact(24) ➞ [24, 4]

is_exact(125) ➞ "Not exact!"

is_exact(720) ➞ [720, 6]

is_exact(1024) ➞ "Not exact!"

is_exact(40320) ➞ [40320, 8]
_____



[Notes]

___
*) It is expected from the challenge-takers to come up with a solution using the concept of recursion or the so-called recursive approach.
*) You can read on more topics about recursion (see Resources tab) if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge.
*) There will be no exceptions to handle. All inputs are positive integers.
*) A non-recursive version of this challenge (of lesser difficulty and which gives you the total liberty of not using the recursive approach) can be found in here.
___



[math] [numbers] [recursion] 



-------------------------------------------------------------------
[Resources]
_________
Thinking Recursively in Python
https://realpython.com/python-thinking-recursively/
Learn how to work with recursion in your Python programs by mastering concepts such as recursive functions and recursive data structures.
_________
_________
Understand Recursion in JavaScript
https://codeburst.io/learn-and-understand-recursion-in-javascript-b588218e87ea
The important part is happening on line 4: return x * factorial(x — 1);. As you can see, the function is actually calling itself again ( factorial(x-1) ), but with a pa …
_________

"""
#Your code should go here:

